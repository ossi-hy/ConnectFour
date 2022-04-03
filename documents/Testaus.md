# Testausdokumentti

[Testikattavuus](https://ossi-hy.github.io/ConnectFour/)

## Mitä on testattu?

Testattu pelilogiikkaa ja pelilaudan tulostamista. Testattu pelin päättymistä neljän suorasta.

## Testien toistaminen

Testit voidaan toistaa komennolla
```$ poetry run coverage run --branch -m pytest src```

Tämän jälkeen testien kattavuuden voi katsoa komennolla
```$ poetry run coverage report -m```

Kattavuudesta voi muodostaa HTML-raportin komennolla
```$ poetry run coverage html -d docs```