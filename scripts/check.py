"""Validate local profile links and image assets without network dependencies."""

import re
import struct
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
RAW_PREFIX = "https://raw.githubusercontent.com/try-auroraview/.github/main/"
errors = []

for document in sorted(ROOT.rglob("*.md")):
    if ".git" in document.parts:
        continue
    text = document.read_text(encoding="utf-8")
    links = re.findall(r"\]\(([^ )]+)(?:\s+[^)]*)?\)", text)
    links += re.findall(r'(?:src|href)="([^"]+)"', text)
    for link in links:
        if link.startswith(RAW_PREFIX):
            target = ROOT / unquote(link[len(RAW_PREFIX):])
        elif not urlsplit(link).scheme and not link.startswith("#"):
            target = document.parent / unquote(link.split("#", 1)[0])
        else:
            continue
        if not target.exists():
            errors.append("{}: missing {}".format(document.relative_to(ROOT), link))
    for image in re.findall(r"<img\b[^>]*>", text):
        if not re.search(r'\balt="[^"]+"', image):
            errors.append("{}: image needs alt text".format(document.relative_to(ROOT)))

for asset in (ROOT / "profile/assets").glob("*.png"):
    data = asset.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        errors.append("{}: invalid PNG".format(asset.name))
    elif min(struct.unpack(">II", data[16:24])) == 0:
        errors.append("{}: empty PNG".format(asset.name))

if errors:
    raise SystemExit("\n".join(errors))
print("English and Chinese profile links, alt text and local assets are valid.")

