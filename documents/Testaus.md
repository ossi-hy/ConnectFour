# Testausdokumentti

[Testikattavuus](https://ossi-hy.github.io/ConnectFour/)
<iframe src=https://ossi-hy.github.io/ConnectFour/ width=700 height=200></iframe>

## Mitä on testattu?

Testattu pelilogiikkaa ja pelilaudan tulostamista. Testattu pelin päättymistä neljän suorasta.

## Testien toistaminen

Testit voidaan toistaa komennolla
`poetry run coverage run --branch -m pytest src`
Tämän jälkeen testien kattavuuden voi katsoa komennolla
`poetry run coverage report -m`