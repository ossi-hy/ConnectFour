# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelma on jaettu kolmeen osaan. *Main.py* on ohjelman aloituskohta, jonka avulla voi testata ratkaisijan toimintaa komentoriviltä. *Board*-luokka huolehtii pelilaudasta ja tarjoaa metodeja siirtojen tekemiseen ja voittajan määrittämiseen. *Solver*-luokka toteuttaa negamax-algoritmin alpha-beta karsinnalla. Se tarjoaa myös metodin parhaan siirron löytämiseen.

## Aika- ja tilavaativuudet

Ohjleman aikavaativuus on $O(b^d)$, missä $b$ on mahdollisten siirtojen määrä (yleensä pelilaudan leveys, eli 7) ja $d$ on hakupuun syvyys, eli jäljellä olevien mahdollisten siirtojen määrä ennen voittoa tai tasapeliä (aloitukssta tasapeliin menee $7*6=42$ siirtoa). Koska pelilauta peruu aikasemmat siirrot algoritmin peruuttaessa hakupuuta ylöspäin, sen tilavaativus on vain yhden pelilaudan verran, eli vakio $O(1)$.

## Puutteet ja parannusehdotukset

Graafinen käyttöliittymä ja yleistä optimointia.

## Lähteet

[1] https://en.wikipedia.org/wiki/Negamax 8.4.2022
[2] https://en.wikipedia.org/wiki/Bitboard 8.4.2022
