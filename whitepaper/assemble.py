#!/usr/bin/env python3
"""FCL System ONE 설계 백서 조립기 (stdlib만).

사용
  python3 -I assemble.py            # sections/*.html → site/index.html 조립 + 검사
  python3 -I assemble.py --strict   # 링크된 pages/*.html 이 없으면 실패로 본다(기본은 WARN)
  python3 -I assemble.py --quiet    # 요약만 출력

동작
  1. sections/ 의 조각을 파일명 순으로 읽어 template.html 의 자리표시자에 넣는다. 없는 조각은 건너뛰고 WARN.
  2. data-part 가 바뀌는 곳마다 부 제목 머리(.wp-part)를 넣는다. 표지(cover)는 부 머리 없이 맨 앞에 두고,
     '들어가며'의 부 머리는 표지 바로 다음(첫 번째 비표지 조각 앞)에 넣는다.
  3. 번호: 표지를 뺀 h2 에 1, 2, 3 … , 그 아래 h3 에 3.1, 3.2 … 를 붙인다(span.h-num).
     그림은 figcaption 안 .fig-no 에 '그림 N.', 표는 caption 안 .tab-no 에 '표 N.' 을 문서 순서로 채운다.
     조각을 HTML 파서로 다시 직렬화하지 않는다. 위치 기반 문자열 삽입만 쓰므로 인라인 SVG·MathML 의
     대소문자 속성(viewBox 등)이 그대로 남는다.
  4. 목차(<nav aria-label="목차">): 부 · h2(#SLUG) · h3(#h3-id) 링크, 동반 페이지 링크. 현재 위치 강조는 template 의 스크립트가 한다.
  5. site/ 를 지우고 새로 만든다: index.html · style.css · assets/ · pages/(vendor/ 포함).

검사(실패하면 종료 코드 1)
  - 합본 id 중복
  - 깨진 내부 앵커(아직 없는 조각의 #SLUG·#sec-SLUG 를 가리키면 WARN)
  - 누락 asset(img src 등이 site/ 기준 실제 파일인가)
  - 외부 리소스 로드(src=http·//, <link href=http>, @import, url(http) — index.html·style.css·pages/*.html·assets/*.svg)
  - site/ 전체의 '/home/' 문자열·이메일
  - 링크된 pages/*.html 이 없으면 WARN(--strict 면 FAIL)
"""
from __future__ import annotations

import argparse
import datetime
import re
import shutil
import sys
from html.parser import HTMLParser
from pathlib import Path

W = Path(__file__).resolve().parent
BASE_COMMIT = "2ecf3e0"
REPO_URL = "https://github.com/jimmylegendary/full-continual-learning"

# (파일, slug, data-part) — CONTRACT.txt 2절
SECTIONS = [
    ("00-cover.html", "cover", "들어가며"),
    ("01-executive-summary.html", "summary", "들어가며"),
    ("02-reading-guide.html", "reading-guide", "들어가며"),
    ("10-purpose.html", "purpose", "1부 · 왜, 어디서 왔나"),
    ("11-lineage.html", "lineage", "1부 · 왜, 어디서 왔나"),
    ("12-traceability.html", "traceability", "1부 · 왜, 어디서 왔나"),
    ("13-literature.html", "literature", "1부 · 왜, 어디서 왔나"),
    ("20-architecture.html", "architecture", "2부 · 어떻게 동작하나"),
    ("21-math.html", "math", "2부 · 어떻게 동작하나"),
    ("22-state.html", "state", "2부 · 어떻게 동작하나"),
    ("30-evaluation.html", "evaluation", "3부 · 어떻게 검증하고 나아가나"),
    ("31-roadmap.html", "roadmap", "3부 · 어떻게 검증하고 나아가나"),
    ("32-evolution.html", "evolution", "3부 · 어떻게 검증하고 나아가나"),
    ("33-open.html", "open", "3부 · 어떻게 검증하고 나아가나"),
    ("40-expert-delta.html", "expert-delta", "4부 · 다른 눈으로 보기"),
    ("41-graph.html", "graph", "4부 · 다른 눈으로 보기"),
    ("90-appendix.html", "appendix", "부록"),
]
# 조각이 아직 없을 때 목차에 자리만 보이는 이름
DEFAULT_TITLES = {
    "cover": "표지", "summary": "2분 요약", "reading-guide": "읽는 법", "purpose": "목적과 헌장",
    "lineage": "계보", "traceability": "사용자 진술의 추적", "literature": "문헌 검토",
    "architecture": "통합 아키텍처", "math": "수학적 명세", "state": "상태와 저장",
    "evaluation": "평가", "roadmap": "로드맵", "evolution": "자기 진화 정책", "open": "열린 질문",
    "expert-delta": "전문가용 델타", "graph": "지식 그래프", "appendix": "부록",
}
# 부 머리에 보이는 한 줄 설명(저장소 문서의 구성을 말할 뿐, 새 주장을 담지 않는다)
PART_DESC = {
    "들어가며": "이 백서가 무엇이고, 지금 어디까지 와 있으며, 어떻게 읽으면 되는지.",
    "1부 · 왜, 어디서 왔나": "설계의 목적, Melete 에서 이어진 계보, 사용자 진술이 설계에 반영된 정도, 문헌이 말하는 것.",
    "2부 · 어떻게 동작하나": "통합 아키텍처, 수학적 명세, 상태·저장 계약. 모두 제안 수준의 설계이며 구현은 없다.",
    "3부 · 어떻게 검증하고 나아가나": "평가 계획, P1–P5 로드맵, 자기 진화 정책, 열린 결정과 질문.",
    "4부 · 다른 눈으로 보기": "분야 전문가용 델타와, 설계의 연결을 탐색하는 지식 그래프.",
    "부록": "용어집, 문서 지도, 이 백서를 만든 방법, 변경 기록.",
}
PAGES = [  # (파일, 목차에 보이는 이름)
    ("brief.html", "결정권자용 한 장"),
    ("intuition.html", "처음 보는 사람용"),
    ("expert.html", "분야 전문가용"),
    ("graph.html", "연결 탐색 그래프"),
    ("ledger.html", "피드백 원장 탐색기"),
]
KNOWN_SLUGS = {s for _, s, _ in SECTIONS}
KNOWN_ANCHORS = KNOWN_SLUGS | {"sec-" + s for s in KNOWN_SLUGS}

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}\b")
EXT_ATTR_RE = re.compile(r"""\b(src|srcset|poster|data)\s*=\s*["']?\s*(https?:)?//""", re.I)
EXT_LINK_RE = re.compile(r"""<link\b[^>]*\bhref\s*=\s*["']?\s*(https?:)?//""", re.I)
EXT_IMPORT_RE = re.compile(r"""@import\s+(url\()?\s*["']?\s*(https?:)?//""", re.I)
EXT_URL_RE = re.compile(r"""url\(\s*["']?\s*(https?:)?//""", re.I)
TEXT_SUFFIXES = {".html", ".htm", ".css", ".js", ".mjs", ".svg", ".json", ".txt", ".xml"}

HEAD_RE = re.compile(r"(<h([23])\b([^>]*)>)(.*?)(</h\2\s*>)", re.S | re.I)
FIGNO_RE = re.compile(r"""(<span\s+class="fig-no"\s*>)(\s*)(</span>)""")
TABNO_RE = re.compile(r"""(<span\s+class="tab-no"\s*>)(\s*)(</span>)""")
SECTION_OPEN_RE = re.compile(r"<section\b([^>]*)>", re.I)
ATTR_RE = re.compile(r"""([A-Za-z_:][\w:.-]*)\s*=\s*("([^"]*)"|'([^']*)')""")


class Log:
    def __init__(self, quiet: bool) -> None:
        self.warns = 0
        self.fails = 0
        self.quiet = quiet

    def info(self, msg: str) -> None:
        if not self.quiet:
            print(msg)

    def warn(self, msg: str) -> None:
        self.warns += 1
        print(f"WARN {msg}")

    def fail(self, msg: str) -> None:
        self.fails += 1
        print(f"FAIL {msg}")


class Frag:
    def __init__(self, fname: str, slug: str, part: str, html: str) -> None:
        self.fname, self.slug, self.part, self.html = fname, slug, part, html
        self.heads: list[tuple[int, str, str, str]] = []  # (level, id, number, text)


def attrs_of(tag_attrs: str) -> dict[str, str]:
    return {m.group(1).lower(): (m.group(3) if m.group(3) is not None else m.group(4)) for m in ATTR_RE.finditer(tag_attrs)}


def strip_tags(s: str) -> str:
    return " ".join(re.sub(r"<[^>]+>", "", s).split())


def read_fragments(log: Log) -> list[Frag]:
    frags: list[Frag] = []
    present = set()
    missing_names: list[str] = []
    for fname, slug, part in SECTIONS:
        p = W / "sections" / fname
        if not p.exists():
            missing_names.append(fname)
            continue
        html = p.read_text(encoding="utf-8").strip()
        m = SECTION_OPEN_RE.search(html)
        if not m or not html.lower().startswith("<section"):
            log.fail(f"sections/{fname}: 최상위가 <section> 이 아님")
            continue
        a = attrs_of(m.group(1))
        if a.get("id") != f"sec-{slug}":
            log.fail(f'sections/{fname}: section id 는 "sec-{slug}" (지금 {a.get("id")!r})')
        dpart = a.get("data-part", part)
        if dpart != part:
            log.warn(f"sections/{fname}: data-part {dpart!r} ≠ 계약 {part!r} — 조각의 값을 쓴다")
        frags.append(Frag(fname, slug, dpart, html))
        present.add(fname)
    if missing_names:
        log.warn(f"조각 {len(missing_names)}개 없음(건너뜀): {' '.join(missing_names)}")
    known = {f for f, _, _ in SECTIONS}
    for p in sorted((W / "sections").glob("*.html")):
        if p.name not in known:
            log.warn(f"계약 표에 없는 조각(무시): sections/{p.name}")
    return frags


def number_and_collect(frags: list[Frag]) -> tuple[int, int]:
    """h2·h3 번호와 목차 항목, 그림·표 번호를 채운다(위치 기반 문자열 치환)."""
    n2 = 0
    figs = 0
    tabs = 0
    for f in frags:
        is_cover = f.slug == "cover"
        n3 = 0
        if not is_cover:
            n2 += 1  # 이 조각의 h2 번호 (h2 는 조각당 하나)
        cur2 = n2

        def repl(m: re.Match) -> str:
            nonlocal n3
            open_tag, level, attrs, inner, close = m.group(1), int(m.group(2)), m.group(3), m.group(4), m.group(5)
            hid = attrs_of(attrs).get("id", "")
            text = strip_tags(inner)
            if is_cover:
                num = ""
            elif level == 2:
                num = str(cur2)
            else:
                n3 += 1
                num = f"{cur2}.{n3}"
            f.heads.append((level, hid, num, text))
            if not num:
                return m.group(0)
            return f'{open_tag}<span class="h-num">{num}</span> {inner}{close}'

        html = HEAD_RE.sub(repl, f.html)

        def fig(m: re.Match) -> str:
            nonlocal figs
            figs += 1
            return f"{m.group(1)}그림 {figs}.{m.group(3)}"

        def tab(m: re.Match) -> str:
            nonlocal tabs
            tabs += 1
            return f"{m.group(1)}표 {tabs}.{m.group(3)}"

        html = FIGNO_RE.sub(fig, html)
        html = TABNO_RE.sub(tab, html)
        f.html = html
    return figs, tabs


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def part_label_title(part: str) -> tuple[str, str]:
    if " · " in part:
        a, b = part.split(" · ", 1)
        return a.strip(), b.strip()
    return "", part


def part_head(part: str, idx: int) -> str:
    label, title = part_label_title(part)
    desc = PART_DESC.get(part, "")
    lab = f'<p class="wp-part-label">{esc(label)}</p>\n' if label else ""
    d = f'\n<p class="wp-part-desc">{esc(desc)}</p>' if desc else ""
    return (f'<header class="wp-part" id="wp-part-{idx}" aria-label="{esc(part)}">\n{lab}'
            f'<p class="wp-part-title">{esc(title)}</p>{d}\n</header>')


def build_toc(frags: list[Frag]) -> str:
    by_slug = {f.slug: f for f in frags}
    out = ['<nav class="wp-toc" id="wp-toc" aria-label="목차">', '<p class="wp-toc-title">목차</p>', "<ol>"]
    cur_part = None
    open_part = False
    for fname, slug, part in SECTIONS:
        if part != cur_part:
            if open_part:
                out.append("</ol></li>")
            label, title = part_label_title(part)
            nm = f"{label} {title}".strip() if label else title
            out.append(f'<li class="wp-toc-part"><span class="wp-toc-part-name">{esc(nm)}</span><ol>')
            cur_part = part
            open_part = True
        f = by_slug.get(slug)
        if not f:
            out.append(f'<li><span class="wp-toc-missing">{esc(DEFAULT_TITLES.get(slug, slug))} (준비 중)</span></li>')
            continue
        h2 = next((h for h in f.heads if h[0] == 2), None)
        if not h2:
            out.append(f'<li><a class="toc-h2" href="#{slug}">{esc(DEFAULT_TITLES.get(slug, slug))}</a></li>')
            continue
        _, hid, num, text = h2
        nspan = f'<span class="toc-n">{num}</span>' if num else ""
        li = [f'<li><a class="toc-h2" href="#{esc(hid)}">{nspan}{text}</a>']
        h3s = [h for h in f.heads if h[0] == 3 and h[1]]
        if h3s:
            li.append('<ol class="wp-toc-sub">')
            for _, i3, n3, t3 in h3s:
                ns = f'<span class="toc-n">{n3}</span>' if n3 else ""
                li.append(f'<li><a class="toc-h3" href="#{esc(i3)}">{ns}{t3}</a></li>')
            li.append("</ol>")
        li.append("</li>")
        out.append("".join(li))
    if open_part:
        out.append("</ol></li>")
    out.append("</ol>")
    out.append('<div class="wp-toc-pages"><span class="wp-toc-part-name">동반 페이지</span><ol>')
    for fn, nm in PAGES:
        out.append(f'<li><a class="toc-h2" href="pages/{fn}">{esc(nm)}</a></li>')
    out.append("</ol></div>")
    out.append("</nav>")
    return "\n".join(out)


class IdCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.refs: list[tuple[str, str]] = []  # (tag, url)

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a" and a.get("href"):
            self.hrefs.append(a["href"])
        for k in ("src", "poster", "data"):
            if a.get(k):
                self.refs.append((tag, a[k]))
        if tag == "link" and a.get("href"):
            self.refs.append((tag, a["href"]))
        if tag in ("image", "use"):
            h = a.get("href") or a.get("xlink:href")
            if h:
                self.refs.append((tag, h))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


def run_checks(site: Path, log: Log, strict: bool, missing_slugs: set[str]) -> None:
    idx = (site / "index.html").read_text(encoding="utf-8")
    col = IdCollector()
    col.feed(idx)
    # 1. id 중복
    seen: dict[str, int] = {}
    for i in col.ids:
        seen[i] = seen.get(i, 0) + 1
    dup = sorted(i for i, n in seen.items() if n > 1)
    if dup:
        log.fail(f"합본 id 중복 {len(dup)}: {dup[:15]}")
    idset = set(col.ids)
    # 2. 깨진 앵커(아직 없는 조각의 #SLUG·#sec-SLUG 는 WARN 한 줄로 모은다)
    pending = []
    for h in sorted({h for h in col.hrefs if h.startswith("#") and len(h) > 1}):
        t = h[1:]
        if t in idset:
            continue
        if t in KNOWN_ANCHORS:
            pending.append(h)
        else:
            log.fail(f"깨진 내부 앵커 {h}")
    if pending:
        log.warn(f"앵커 {len(pending)}개가 아직 없는 조각을 가리킴(조각이 오면 해소): {' '.join(pending)}")
    # 3. 누락 asset·페이지
    for tag, ref in col.refs:
        if re.match(r"^(https?:)?//|^data:|^#|^mailto:|^blob:", ref):
            continue
        if not (site / ref.split("#")[0].split("?")[0]).exists():
            log.fail(f"누락 asset <{tag}> {ref}")
    nopage = []
    for h in sorted(set(col.hrefs)):
        if h.startswith("assets/"):
            if not (site / h.split("#")[0]).exists():
                log.fail(f"누락 asset 링크 {h}")
        elif h.startswith("pages/"):
            if not (site / h.split("#")[0]).exists():
                nopage.append(h)
    if nopage:
        (log.fail if strict else log.warn)(f"링크된 페이지 {len(nopage)}개 없음: {' '.join(nopage)}")
    for css in site.rglob("*.css"):
        for m in re.finditer(r"url\(\s*['\"]?([^)'\"]+)", css.read_text(encoding="utf-8", errors="replace")):
            u = m.group(1)
            if not re.match(r"^(https?:)?//|^data:|^#", u) and not (css.parent / u).exists():
                log.fail(f"{css.name}: 누락 url({u})")
    # 4. 외부 리소스 로드: index.html · style.css · pages/*.html · assets/*.svg
    targets = [site / "index.html", site / "style.css", *sorted((site / "pages").glob("*.html")), *sorted((site / "assets").glob("*.svg"))]
    for p in targets:
        s = p.read_text(encoding="utf-8", errors="replace")
        for rx, label in ((EXT_ATTR_RE, "src/data 외부"), (EXT_LINK_RE, "<link href> 외부"),
                          (EXT_IMPORT_RE, "@import 외부"), (EXT_URL_RE, "url() 외부")):
            n = len(rx.findall(s))
            if n:
                log.fail(f"{p.relative_to(site)}: {label} {n}건")
    # 5. site/ 전체 '/home/' · 이메일
    for p in sorted(site.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES:
            continue
        s = p.read_text(encoding="utf-8", errors="replace")
        if "/home/" in s:
            log.fail(f"{p.relative_to(site)}: '/home/' {s.count('/home/')}건")
        em = sorted(set(EMAIL_RE.findall(s)))
        if em:
            log.fail(f"{p.relative_to(site)}: 이메일 {len(em)}종 {em[:3]}")
    if "@@" in idx:
        log.fail("index.html 에 풀리지 않은 자리표시자(@@)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true", help="링크된 pages/*.html 이 없으면 실패")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()
    log = Log(args.quiet)

    tpl_path = W / "template.html"
    css_path = W / "style.css"
    for need in (tpl_path, css_path):
        if not need.exists():
            print(f"FAIL 필요한 파일 없음: {need.name}")
            return 1
    tpl = tpl_path.read_text(encoding="utf-8")
    for ph in ("<!--@@TOC@@-->", "<!--@@BODY@@-->", "<!--@@FOOT@@-->", "<!--@@COMMIT@@-->"):
        if ph not in tpl:
            print(f"FAIL template.html 에 자리표시자 {ph} 없음")
            return 1

    frags = read_fragments(log)
    missing = {s for _, s, _ in SECTIONS} - {f.slug for f in frags}
    n_figs, n_tabs = number_and_collect(frags)

    # 본문: 부 머리 + 조각
    body: list[str] = []
    prev_part = None
    part_idx = 0
    for i, f in enumerate(frags):
        if f.slug == "cover" and i == 0:
            body.append(f.html)  # 표지는 부 머리 없이
            continue
        if f.part != prev_part:
            part_idx += 1
            body.append(part_head(f.part, part_idx))
            prev_part = f.part
        body.append(f.html)
    toc = build_toc(frags)

    today = datetime.date.today().isoformat()
    commit_link = f'<a href="{REPO_URL}/commit/{BASE_COMMIT}">{BASE_COMMIT}</a>'
    foot = (
        f"<p>기준 저장소 커밋 {commit_link}(2026-11-12) · 조립 {today} · 본문 조각 {len(frags)}/{len(SECTIONS)}개 ·"
        f" 그림 {n_figs}개 · 표 {n_tabs}개</p>\n"
        f'<p>이 백서는 <a href="{REPO_URL}">full-continual-learning</a> 저장소의 설계 문서를 한곳에 모은 읽기용 지도다. '
        "원본은 저장소 문서이며, 통합 모델의 구현·학습·효용 검증은 아직 없다. 인터넷 없이 열리도록 외부 글꼴·스크립트·이미지를 쓰지 않았다.</p>"
    )
    out = (tpl.replace("<!--@@TOC@@-->", toc)
              .replace("<!--@@BODY@@-->", "\n\n".join(body))
              .replace("<!--@@FOOT@@-->", foot)
              .replace("<!--@@COMMIT@@-->", BASE_COMMIT))

    # site/ 새로 만들기
    site = W / "site"
    if site.exists():
        if site.resolve().parent != W.resolve():
            print("FAIL site 경로가 예상 밖")
            return 1
        shutil.rmtree(site)
    site.mkdir()
    (site / "index.html").write_text(out, encoding="utf-8")
    shutil.copy2(css_path, site / "style.css")
    for d in ("assets", "pages"):
        src = W / d
        if src.exists():
            # 작업 중 임시 파일(_tmp*)·숨김 파일·캐시는 옮기지 않는다
            shutil.copytree(src, site / d, ignore=shutil.ignore_patterns("_tmp*", ".*", "__pycache__", "node_modules"))
        else:
            (site / d).mkdir()

    toc_h2 = len(re.findall(r'<a class="toc-h2" href="#', toc))
    log.info(f"목차: h2 링크 {toc_h2}/{len(SECTIONS)} · h3 링크 {len(re.findall('class=.toc-h3.', toc))}")
    log.info(f"조립: 조각 {len(frags)}/{len(SECTIONS)} · 부 머리 {part_idx}개 · 목차 항목 {sum(len(f.heads) for f in frags)}개 · site/index.html {len(out) // 1024} KB")
    run_checks(site, log, args.strict, missing)
    print(f"assemble: 조각 {len(frags)}/{len(SECTIONS)}, WARN {log.warns}, FAIL {log.fails}")
    return 1 if log.fails else 0


if __name__ == "__main__":
    sys.exit(main())
