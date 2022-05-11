# Käyttöohje

## Asennus
Tarvitset [Poetryn](https://python-poetry.org/) asentaaksesi ohjelman.

Asenna välttämättömät riippuvuudet
```bash
$ poetry install [--no-dev]
```

## Ajaminen

Ohjelman normaali käynnistys, missä voit pelata itseäsi vastaan
```bash
$ poetry run invoke start
```

Pelataksesi tietokonetta vastaan
```bash
$ poetry run invoke start-against
```

## Pelaaminen

Pelatessa ohjelma kysyy lukua 0 ja 6 välillä. Luku ilmaisee sarakkeen, mihin pala tiputetaan. Syöttämällä minkä tahansa kirjaimen tai painamalla `Ctrl+C` ohjelma pysähtyy.

## Testien ajaminen

Ohjelman nopeat yleistä kattavuutta tavoittelevat testit voi aja komennolla
```bash
$ poetry run invoke test
```
</br>
Koodikattavuuden voi luoda komennolla
```bash
$ poetry run invoke coverage-report
```
Tällöin kattavuusraportti löytyy kansiosta `docs`
</br>

Ratkaisijan oikeellisuusta voi testata esilasketuilla pelitauluilla. Tämä saattaa kuitenkin kestää useamman sekunnin.
```bash
$ poetry run invoke slow-test
```

## Profilointi
```bash
$ poetry run invoke profile
```