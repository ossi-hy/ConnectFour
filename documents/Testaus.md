# Testausdokumentti

[Testikattavuus](https://ossi-hy.github.io/ConnectFour/)

## Mitä on testattu?

Testattu pelilogiikkaa ja pelilaudan tulostamista. Testattu pelin päättymistä neljän suorasta. Testattu algoritmin toimintaa sekä simppeleissä ihmisen luettavissa tilanteissa, että erittäin kattavasti esilasketuilla tauluilla.

## Testien toistaminen

Asenna kaikki riippuvuudet
```$ poetry install```

Testit voidaan toistaa komennolla
```$ poetry run invoke test```

Tämän jälkeen testien kattavuuden voi katsoa komennolla
```$ poetry run invoke coverage```

Kattavuudesta voi muodostaa HTML-raportin komennolla
```$ poetry run invoke coverage-html```
Reportti löytyy kansiosta `docs` ja sitä voi katsoa avaamalla tiedoston `index.html`.

Esilaskettuihin tauluihin perustuvat testit voi ajaa komennolla
```$ poetry run invoke slow-test```