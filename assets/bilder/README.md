# Bilder

Hier liegen die echten Fotos. Sie ersetzen die gerechneten Platzhalter-Zeichnungen,
ohne dass am Code etwas geaendert werden muss.

## Ein Foto einsetzen

1. Datei hier ablegen, z. B. `assets/bilder/beer-beats-01.jpg`
2. Am zugehoerigen `<canvas>` in `richtung-h-aushang.html` das Attribut setzen:

   ```html
   <canvas data-bild="assets/bilder/beer-beats-01.jpg" data-szene="abend" ...>
   ```

Das war alles. Das Foto laeuft durch dieselbe Halbton-Funktion wie die Zeichnung
und bekommt damit denselben Druck-Look: 45°-Punktraster, Punktflaeche proportional
zur Deckung, Tonwerte auf 4-92 % gestaucht. Auf den Tinte-Boegen laeuft es negativ
(Papierpunkte auf Tinte), auf dem Gelb-Bogen zweifarbig.

`data-szene` bleibt stehen: schlaegt das Laden fehl, faellt die Seite auf die
gerechnete Zeichnung zurueck statt ein Loch zu zeigen.

## Was ein gutes Bild ausmacht

- **Kontrast schlaegt Aufloesung.** Das Raster zerstoert Feindetails ohnehin.
  1080 px reichen, ein Handyfoto reicht, ein Instagram-Download reicht.
- **Klares Motiv, wenig Gewusel.** Eine Silhouette gegen Licht traegt, ein
  gleichmaessig ausgeleuchteter Raum nicht.
- **Dunkel und koernig ist kein Mangel**, sondern hilft dem Druckbild.
- Das Bild wird formatfuellend eingepasst (cover, mittig) — das Motiv sollte also
  die Bildmitte vertragen.

## Wohin welches Bild gehoert

| Sektion        | data-szene | Format | Motiv                                  |
|----------------|-----------|--------|-----------------------------------------|
| Ueber VIBEON   | `raum`    | 4:5    | Ort ohne Leute: Leerstand, Galerie, Licht |
| Exodus         | `nacht`   | 16:9   | Club, dunkel, Licht ueber der Menge      |
| Beer & Beats   | `abend`   | 5:4    | Leute im Raum, warmes Licht, Glaeser     |
| Live-Act       | `act`     | 4:5    | Portrait, moeglichst Gegenlicht          |

## Rechte

Nur Bilder, an denen VIBEON die Rechte hat oder eine Freigabe vorliegt. Fremde
Event-Grafiken (Festival-Plakate o. Ae.) gehoeren nicht hierher — sie tragen
fremdes Branding.
