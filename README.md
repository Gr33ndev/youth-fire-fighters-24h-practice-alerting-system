# youth-fire-fighters-24h-practice-alerting-system

Browser-based alarm simulator for the youth fire fighters' "Tag der Berufsfeuerwehr" (24-hour practice day).
Configure scheduled "operations" (Einsätze), then the system alarms automatically at each set time — siren sound, indicator lights, address, map, and spoken announcement (text-to-speech in German).

## Run

Double-click `index.html`. That's it. No install, no server.

Works in any modern browser (Chrome, Edge, Firefox, Safari). Recommended: open in fullscreen (`F11`) on the laptop running the practice. Keep the tab in foreground — background tabs throttle timers and may delay alarms.

**Offline behavior:** the alarm core (sound, indicators, description, address) works fully offline. The map is the only online-dependent feature — it uses Leaflet + OpenStreetMap loaded from a CDN. If the CDN or tile server can't be reached, the map silently falls back to a placeholder icon; the alarm itself is unaffected. For guaranteed offline use, run the page once while online so the browser caches Leaflet.

**Text-to-speech:** during an alarm, the system speaks the alarmed vehicles, Stichwort and Einsatzort in German (e.g. *"Einsatz für 1/42 und 2/42, B3 - Gebäudebrand, Mustergasse 1 Stuttgart."*). Vehicle codes containing `/` or `-` between digits (e.g. `1/42`, `1-19`) are normalized to spaces before speaking so the voice reads them as numbers, not dates. Choose under **Einstellungen → Alarmierungsart** between: siren + speech alternating, siren + speech at the same time, siren only, or speech only. Uses the browser's built-in Web Speech API. Works fully offline on macOS, Windows, and most Chrome/Edge installs. On Linux/Firefox a German voice may need to be installed separately.

## Setup

1. Open `index.html` — opens directly in the setup view.
2. Add operations with description, address, date, time, and which vehicles/units are alarmed.
3. Adjust **Einstellungen** if needed (sleep window, alarm duration, default texts, alarm options). Enable **Automatischer Blackscreen während Schlafzeit** if you want the screen to dim automatically during the configured sleep window.
4. Click **Alarmierung starten →** to switch to the live display.
5. Click **System starten** once (browser audio gate).

Config persists in browser `localStorage`. Use **Export JSON** / **Import JSON** to back up or transfer between machines. The Import button also accepts the legacy `config.json` array format from the old PHP setup.

## Assets

Bundled, ready to use:

- `sounds/audio.wav` — default alarm sound (looped during alarm). Optional: replace with any browser-supported audio file. Keep the filename or update the `<audio>` src in `index.html`.
- `images/JF_Logo.png` — default logo. Optional: replace with your own youth fire fighter logo.

## Keyboard shortcuts (display view)

| Key   | Action                                  |
|-------|-----------------------------------------|
| `F11` | Toggle fullscreen                       |
| `F12` | Force blackscreen on/off                |
| `F9`  | Disable automatic sleep-time blackscreen|
| `Esc` | Back to setup                           |

## Alarm options (indicators)

Defaults: `1-19`, `1-42`, `2-42`, `3-48`, `ÖL-A`, `SW-A`, `Zug 1`, `Zug 2`. Fully editable under **Einstellungen → Alarmoptionen**: add, rename, reorder, or remove. Each operation can light any combination.

## Credits

Map: [Leaflet](https://leafletjs.com/) + [OpenStreetMap](https://www.openstreetmap.org/copyright). Geocoding: [Nominatim](https://nominatim.openstreetmap.org/).

Sound: [Martinshorn (Siren) 2](https://freesound.org/people/TitanKaempfer/sounds/811916/) by [TitanKaempfer](https://freesound.org/people/TitanKaempfer/), released under [Creative Commons 0](http://creativecommons.org/publicdomain/zero/1.0/).

## License

See [LICENSE](LICENSE).
