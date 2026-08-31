# Videos

Selbst gehostete Videos. Sie ersetzen die 2-Klick-Instagram-Kacheln — und zwar
vollstaendig: kein Request an Meta, keine Einwilligung noetig, das Video ist
einfach da.

## Ein Video einsetzen

1. Datei hier ablegen, z. B. `assets/video/nima-01.mp4`
2. In `richtung-h-aushang.html` die Kachel ersetzen. Aus dem 2-Klick-Knopf

   ```html
   <div class="reel">
     <button class="reel-laden" type="button" data-reel="PLATZHALTER_NIMA_1"> ... </button>
   </div>
   ```

   wird

   ```html
   <div class="reel">
     <video class="reel-video" src="assets/video/nima-01.mp4"
            playsinline muted loop preload="metadata"></video>
     <button class="ton" type="button" aria-pressed="false">Ton</button>
   </div>
   ```

Das Verhalten kommt von selbst: Das Video startet stumm, sobald die Kachel im
Blick ist, pausiert wieder, sobald sie es nicht mehr ist, und laeuft in Schleife.
Der Ton-Knopf schaltet den Ton an — immer nur bei einem Video gleichzeitig.
Bei `prefers-reduced-motion` startet nichts von allein, das Video bekommt dann
seine eigenen Bedienelemente.

## Format

- **MP4 mit H.264.** Nicht WebM: das spielt auf aelteren iPhones nicht.
- **9:16 hochkant**, passend zur Kachel. Andere Formate werden formatfuellend
  beschnitten (`object-fit:cover`), das Motiv sollte die Mitte vertragen.
- **5 bis 15 Sekunden**, in Schleife. Laenger schaut am Handy niemand.
- **Unter 3 MB je Datei.** 720x1280 reicht voellig; die Kachel ist auf dem
  Handy rund 220 px breit.
- Ton ist erlaubt, aber nicht noetig: gestartet wird ohnehin stumm.

## Woher

Eigene Reels bei Instagram herunterladen (eigene Beitraege lassen sich in der
App speichern) oder gleich die Originaldatei vom Dreh verwenden — die ist besser.
Fremde Videos nur mit Freigabe.
