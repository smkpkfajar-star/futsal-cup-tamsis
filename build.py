"""Bangun semua halaman: pages/*.html + layout.html -> index.html, about.html, dst.
Jalankan:  python3 build.py"""
import re, pathlib
root = pathlib.Path(__file__).parent
CSS = ["base","nav","hero","stepper","form","info","footer","pages","timeline","prizes","faq","responsive"]  # urutan penting
layout = (root / "layout.html").read_text(encoding="utf-8")
def inc(t):
    return re.sub(r"<!-- @include (.+?) -->", lambda m: inc((root / m.group(1)).read_text(encoding="utf-8").rstrip()), t)
css = "\n".join(f'<link rel="stylesheet" href="css/{c}.css">' for c in CSS)
for f in sorted((root / "pages").glob("*.html")):
    src = f.read_text(encoding="utf-8")
    title = re.search(r"<!-- title: (.+?) -->", src).group(1)
    scripts = ["js/menu.js"] + re.findall(r"<!-- script: (.+?) -->", src)
    body = re.sub(r"<!-- (title|script): .+? -->\n?", "", src)
    page = (layout.replace("{{title}}", title).replace("{{css}}", css).replace("{{content}}", body)
            .replace("{{scripts}}", "\n".join(f'<script src="{s}"></script>' for s in scripts)))
    page = inc(page)
    out = "index.html" if f.stem == "home" else f.stem + ".html"
    page = page.replace(' class="on" href', " href").replace(f'<a href="{out}">', f'<a class="on" href="{out}">')
    (root / out).write_text(page, encoding="utf-8")
    print("dibuat:", out)
