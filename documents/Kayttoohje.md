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

Jos haluat säätää algoritmin laskennan syvyyttä, joudut käynnistämään ohjelman manuaalisesti, esim:
```bash
$ poetry run python3 src/main.py --depth 13 [--against]
```
Oletussyvyys on 9 siirtoa.

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
Jos haluat tutkia ohjelman nopeutta esim. cProfile työkalulla, voi tällä pakottaa ohjelman ajamaan esilaskettuja asemia.
```bash
$ poetry run invoke profile
```