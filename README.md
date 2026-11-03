# Maskiner

Et landbrugsspil ovenfra til mobil og browser, hvor du kører mejetærsker, traktor og gummiged på gården. Lavet, så en 6-årig kan spille det. v1.0.

**Spil:** https://seranodk.github.io/maskiner/ — eller åbn `index.html`. På mobilen kan siden føjes til hjemmeskærmen og kører så i fuld skærm som en app.

## Indhold
| Maskine | Opgave | Sådan gør du |
|---|---|---|
| Mejetærsker | Høst kornet | Kør gennem kornmarken. Når korntanken er fuld, kører du hen til kornvognen ved vejen, så tømmes den af sig selv. Klaret når 90 % er høstet og tanken er tom. |
| Traktor | Pløj marken | Ploven bag traktoren pløjer stubmarken brun, når du kører fremad. Mågerne følger efter. Klaret når 90 % er pløjet. |
| Gummiged | Grav jorden | Kør skovlen ind i jordbunken i grusgraven. Når skovlen er fuld, kører du hen til lastbilen og tømmer den. Fyld 3 lastbiler. |

- En gul pil og en ring viser, hvor du skal hen, når tanken eller skovlen er fuld
- De to andre maskiner holder parkeret i gården, og man kan køre rundt på hele gården
- Træer, huse og siloer stopper bare maskinen blødt – man kan ikke køre galt
- Stjerne og antal gange klaret på hver maskine i menuen. Lyd kan slås fra

## Styring
| Mobil | Tastatur | Handling |
|---|---|---|
| Joystick (nederst til venstre) | ← → · A D | Peg den vej maskinen skal køre |
| GAS | ↑ · W | Kør frem |
| BAK | ↓ · S | Bak (maskinen bakker den vej, du peger) |
| Pauseknappen | P · Esc | Pause |

## Filer
- `index.html` – hele spillet i én fil
- `manifest.webmanifest`, `icon-*.png`, `apple-touch-icon.png` – app-ikon og fuld skærm på mobil

## Udvikling
Kilden ligger i `src/game.html`. `python3 build.py` bygger `index.html` (GitHub-versionen) og artifakt-versionen ud fra den. Versionsnummeret står ét sted: `VERSION` i `src/game.html`.

## Versioner
Hver udgave gemmes også som `versions/maskiner-vX.Y.html`, og versionen står i titlen og på startskærmen.

| Version | Dato | Ændringer |
|---|---|---|
| v1.0 | 2026-11-03 | Første udgave: mejetærsker, traktor med plov og gummiged med lastbil. Joystick, GAS og BAK. |
