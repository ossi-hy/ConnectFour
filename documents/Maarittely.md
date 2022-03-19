# Määrittelydokumentti
## Ohjelmointikielet

Projektin ohjelmointikielenä toimii Python 3. Muita kieliä vertaisarviontia varten ovat
- C
- C#
- Java

## Algoritmit ja tietorakenteet

Projektissa käytetään [negamax](https://en.wikipedia.org/wiki/Negamax)-algoritmiä alpha beta karsinnalla. Pelilaudan tietorakenteena toimii [bitboard](https://en.wikipedia.org/wiki/Bitboard). Nämä on valittu, koska ne ovat tehokkaita löytämään voittavia siirtoja.

## Syötteet

Ohjelma saa syötteenä hiiren sijainnin, sekä painallukset. Näitä käytetään tietokonetta vastaan pelatessa, sekä muun sovellusloogikan ohjauksessa.

## O-analyysi 

Pelilaudan tarkistus: $O(1)$
Negamax worst-case: $O(b^d)$, missä $b$ on mahdollisten siirtojen määrä ja $d$ hakupuun syvyys.

## Opinto-ohjelma

Matemaattisten tieteiden kandiohjelma, tietojenkäsittelyteorian opintosuunta.

## Kieli
Projektin dokumentoinnissa, koodissa ja kommenteissa käytetty kieli on englanti.