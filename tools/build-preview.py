#!/usr/bin/env python3
"""Baut aus einer Seite + assets/ EINE self-contained HTML-Datei.

Hintergrund: Zum Ansehen am Handy wird die Seite als Artifact veroeffentlicht.
Dort gibt es nur eine einzelne Datei — relative Pfade wie assets/... laufen ins
Leere, und die CSP blockt externe Requests. Dieses Skript bettet deshalb alle
Schriften und Bilder als data:-URIs ein und entfernt die Dokumenthuelle
(doctype/html/head/body), die das Artifact selbst mitbringt.

    python3 tools/build-preview.py <ziel.html> [quelle.html] [Titel]

Beispiele:
    python3 tools/build-preview.py /tmp/vorschau.html
    python3 tools/build-preview.py /tmp/aushang.html richtung-h-aushang.html "VIBEON Aushang"
"""
import base64, mimetypes, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ZIEL = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "preview.html"
QUELLE = ROOT / (sys.argv[2] if len(sys.argv) > 2 else "index.html")
TITEL = sys.argv[3] if len(sys.argv) > 3 else "VIBEON One-Pager"

html = QUELLE.read_text(encoding="utf-8")


def data_uri(rel, mime=None):
    p = ROOT / rel
    mime = mime or mimetypes.guess_type(str(p))[0] or "application/octet-stream"
    return "data:%s;base64,%s" % (mime, base64.b64encode(p.read_bytes()).decode())


style = re.search(r"<style>.*?</style>", html, re.S).group(0)
nosc = re.search(r"<noscript>.*?</noscript>", html, re.S)
body = re.search(r"<body>(.*)</body>", html, re.S).group(1)

# Schriften einbetten (die Seite laedt bewusst nichts von fremden Hosts)
for treffer in sorted(set(re.findall(r"assets/fonts/[\w.-]+\.woff2", style))):
    style = style.replace("'%s'" % treffer, "'%s'" % data_uri(treffer, "font/woff2"))

# Bilder einbetten — sowohl klassische <img src> als auch die Fotos der
# Halbton-Engine, die ueber data-bild am <canvas> haengen.
for attr in ("src", "data-bild"):
    muster = r'%s="(assets/[\w./-]+)"' % attr
    for treffer in sorted(set(re.findall(muster, body))):
        # Der Skriptblock steht mit im Body, dort stehen Beispielpfade in
        # Kommentaren. Nur einbetten, was es wirklich gibt.
        if not (ROOT / treffer).is_file():
            print("  uebersprungen (nicht vorhanden): %s" % treffer)
            continue
        # Alles wird als data:-URI eingebettet und dabei um rund ein Drittel
        # groesser. Ein Artifact darf 16 MB haben - bei Videos wird das schnell eng.
        kb = (ROOT / treffer).stat().st_size / 1024
        if kb > 2048:
            print("  WARNUNG: %s ist %.1f MB - eingebettet rund %.1f MB" % (treffer, kb / 1024, kb * 1.34 / 1024))
        body = body.replace('%s="%s"' % (attr, treffer),
                            '%s="%s"' % (attr, data_uri(treffer)))

ZIEL.write_text(
    "<title>%s</title>\n%s\n%s\n%s" % (TITEL, style, nosc.group(0) if nosc else "", body.strip()),
    encoding="utf-8",
)
print("%s  %.1f KB" % (ZIEL, ZIEL.stat().st_size / 1024))
