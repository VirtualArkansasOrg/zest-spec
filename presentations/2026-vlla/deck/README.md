# Deck build

`zest-vlla-2026.pptx` is built from a copy of the Geometric VA Template (exported as .pptx; the template itself is not in the repo).

1. `structure.py` duplicates the template slides used as layouts, in order.
2. `build.py` fills them with the copy and images and writes the speaker notes from `content.py`.

Images come from `../media/`. Rebuild after changing the copy, then upload the .pptx to Google Drive (it converts to Google Slides).

The copy here has "QR code (link coming)" boxes on the four zest slides. The deck Kyle presents (in his Drive) has QR codes to the zests on his server; `build.py` adds them when `qr-<slug>.png` files sit next to it. Those links are kept out of the repository.
