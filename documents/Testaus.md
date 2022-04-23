# Testausdokumentti

[Testikattavuus](https://ossi-hy.github.io/ConnectFour/)

## Mitä on testattu?

Testattu pelilogiikkaa ja pelilaudan tulostamista. Testattu pelin päättymistä neljän suorasta. Testattu algoritmin toimintaa erittäin kattavasti esilasketuilla tauluilla.

## Testien toistaminen

Testit voidaan toistaa komennolla
```$ poetry run invoke test```

Tämän jälkeen testien kattavuuden voi katsoa komennolla
```$ poetry run invoke coverage```

Kattavuudesta voi muodostaa HTML-raportin komennolla
```$ poetry run invoke coverage-html```