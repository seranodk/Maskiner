# Maskiner

Et landbrugsspil ovenfra til mobil og browser, hvor du kører mejetærsker, traktor og gummiged på gården. Lavet, så en 6-årig kan spille det. v1.2.

**Spil:** https://seranodk.github.io/Maskiner/ — eller åbn `index.html`. På mobilen kan siden føjes til hjemmeskærmen og kører så i fuld skærm som en app.

## Indhold
| Maskine | Opgave | Sådan gør du |
|---|---|---|
| Mejetærsker | Høst kornet | Kør gennem kornmarken. Når korntanken er fuld, kører du hen til kornvognen ved vejen, så tømmes den af sig selv. Klaret når 90 % er høstet og tanken er tom. |
| Traktor | Pløj marken | Ploven bag traktoren pløjer stubmarken brun, når du kører fremad. Mågerne følger efter. Klaret når 90 % er pløjet. |
| Kran | Byg huset | Kør kranvognen hen på den gule P-plads på byggepladsen. Støttebenene kommer ud, og så drejer du kranarmen med styrepinden. Tryk LØFT over byggeklodserne og SÆT over huset. Tre etager og et tag, så er huset færdigt. KØR-knappen gør kranen klar til at køre igen. |
| Gummiged | Grav jorden | Kør skovlen ind i jordbunken i grusgraven. Når skovlen er fuld, kører du hen til lastbilen og tømmer den. Fyld 3 lastbiler. |

- En gul pil og en ring viser, hvor du skal hen, når tanken eller skovlen er fuld
- De to andre maskiner holder parkeret i gården, og man kan køre rundt på hele gården
- Træer, huse og siloer stopper bare maskinen blødt – man kan ikke køre galt
- Stjerne og antal gange klaret på hver maskine i menuen. Lyd kan slås fra

## Styring
Skærmen drejer med maskinen, så den altid kører opad på skærmen.

| Mobil | Tastatur | Handling |
|---|---|---|
| Styrepind (nederst til venstre) – skub til venstre eller højre | ← → · A D | Drej til venstre eller højre |
| GAS | ↑ · W | Kør frem |
| BAK | ↓ · S | Bak |
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
| v1.2 | 2026-11-03 | Ny maskine: kran, der løfter etager og tag op på et hus på byggepladsen. |
| v1.1 | 2026-11-03 | Enklere styring: styrepinden drejer kun til venstre eller højre. Skærmen drejer med maskinen, så den altid kører opad. |
| v1.0 | 2026-11-03 | Første udgave: mejetærsker, traktor med plov og gummiged med lastbil. Joystick, GAS og BAK. |
