# Pirkumu Saraksts

## Ievads

Šī ir Python valodas balstīta pirkumu saraksta pārvaldnieka programma, kas palīdz ērti pārvaldīt pirkumu sarakstu. Jūs varat pievienot produktus, apstiprināt produktus kā nopirktus, dzēst produktus no saraksta, aprēķināt iegādes izmaksas un eksportēt savu pirkumu sarakstu uz Excel failu.

## Saturs

- [Metožu pārskats](#metožu-pārskats)
- [Kas ir projekts "Pirkumu Saraksts"?](#kas-ir-projekts-pirkumu-saraksts)
- [Kad izmantot šo programmu?](#kad-izmantot-šo-programmu)
- [Kā lietot šo programmu?](#kā-lietot-šo-programmu)
- [Prasības](#prasības)
- [Izmantotās bibliotēkas](#izmantotās-bibliotēkas)
- [Avoti](#avoti)
- [Autors](#autors)
- [Kontakti](#kontakti)

## Metožu pārskats

*   [x] **Pievienot produktu pirkumu sarakstam**<br />
Šī metode ļauj pievienot jaunu produktu pirkumu sarakstam, norādot tikai produkta nosaukumu, kategoriju un cenu. Produkts tiek pievienots sarakstā, kurā katru produktu raksturo tā kategorija, cena un pirkuma statuss.
*   [x] **Dzēst produktu no pirkumu saraksta**<br />
Šī metode ļauj izdzēst produktu no pirkumu saraksta pēc tā nosaukuma.
*   [x] **Apskatīt pirkumu sarakstu**<br />
Šī metode izvada visus produktus sarakstā, parādot to nosaukumu, kategoriju, cenu un statusu, vai produkts ir nopirkts vai vēl jānopērk.
*   [x] **Aprēķināt nopirkto un vēl iegādājamo preču izmaksas**<br />
Šī metode aprēķina kopējo izmaksu summu produktiem, kuriem pirkuma statuss ir "Nopirkts" un kuriem pirkuma statuss ir "Vajag nopirkt".
*   [x] **Apstiprināt preces kā nopirktas**<br />
Šī metode ļauj apstiprināt produktu kā nopirktu, izmainot produkta statusu uz "Nopirkts".
*   [x] **Eksportēt pirkumu sarakstu uz Excel failu**<br />
Šī metode ļauj eksportēt pirkumu sarakstu uz Excel failu, saglabājot visus produktus ar to raksturojošajām kategorijām, cenām un statusiem.

## Kas ir projekts "Pirkumu Saraksts"?

Pirkumu Saraksts ir Python programma, kas palīdz lietotājiem organizēt un pārvaldīt savu pirkumu sarakstu. Tā piedāvā dažādas iespējas, piemēram, pievienot, dzēst, apskatīt produktus, aprēķināt nopirkto un vēl pērkamo produktu izmaksas, kā arī eksportēt pirkumu sarakstu uz Excel failu. Šis projekts ir veidots, lai atvieglotu pirkumu sarakstu veidošanu, nodrošinot ātru un vieglu veidu, kā organizēt pirkumus un uzskaitīt izmaksas.

## Kad izmantot šo programmu?

Šo programmu vari izmantot, kad vajag ieplānot, organizēt pirkumus, piemēram, pārtikas produktu iegādi, arī, kad nepieciešams saglabāt sarakstu Excel failā, kā arī, kad vajag aprēķināt izdevumus par nopirktajiem un ieplānotajiem produktiem.

## Kā lietot šo programmu?

Kā sākt izmantot "Pirkumu Saraksts" programmu:

1. Jāpārliecinās, ka ir uzstādīts Python 3. Ja nepieciešamas, to lejupielādē no https://www.python.org/downloads/.
2. Jāinstalē nepieciešamo bibliotēku ar komandu `pip install openpyxl`.
3. Jālejupielādē vai jānokopē programmas pirkumu_saraksts.py failu savā datorā.
4. Palaiž programmu ar Python: `python pirkumu_saraksts.py`
5. Izvēlās vienu no piedāvātajām opcijām:
     1. Pievienot produktu pirkumu sarakstam
     2. Dzēst produktu no pirkumu saraksta
     3. Apskatīt pirkumu sarakstu
     4. Apstriprināt produktu, kā nopirktu
     5. Apskatīt izmaksas nopirktajām un pērkamajām precēm
     6. Ierakstīt Excel failā pirkumu sarakstu
     7. Iziet no programmas
6. Saglabā datus, izvēloties sesto opciju "Ierakstīt Excel failā pirkumu sarakstu", jo programma saglabā sarakstu Excel failā tikai tad, kad izvēlas attiecīgo opciju. Dati netiek automātisku saglabāti, ja tos neeksportē uz Excel failu.
## Prasības

* Python 3.x
* `openpyxl` bibliotēka (Excel eksportēšanai)
  * Instalējiet to, izmantojot: `pip install openpyxl`

## Izmantotās bibliotēkas

Šajā projektā tiek izmantotas sekojošās Python bibliotēkas:
1. `openpyxl` <br />
Šī bibliotēka tiek izmantota, lai strādātu ar Excel failiem(XLSX formatu), XLSX failu izveidei, šūnu formatēšanai un pirkumu saraksta datu eksportēšanai uz Excel izklājlapu.
2. `datetime` <br />
Šī bibliotēka ir izmantota, lai iegūtu pašreizējo laiku, datumu un lai pierakstītu datu ievades laiku Excel failā.

## Avoti

1. [Python dokumentācija](https://docs.python.org/3/) - Oficiālā Python dokumentācija.
2. [openpyxl dokumentācija](https://openpyxl.readthedocs.io/en/stable/) - Oficiālā dokumentācija `openpyxl` bibliotēkai.
3. [Markdown sintakse](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) - Atsauce uz Markdown sintaksi.
## Autors 

Darbu izstrādāja: Mikus Rodrigo Viļķins, 241RDB194

## Kontakti

Ja vēlies ar mani sazināties, raksti uz e-pastu: Mikus-Rodrigo.Vilkins@edu.rtu.lv.
