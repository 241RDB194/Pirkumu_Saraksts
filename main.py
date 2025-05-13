import openpyxl
from datetime import datetime
Pirkumu_saraksts = {}
def pievienot_iepirkuma_sarakstam():

  Produkta_nosaukums = input("Produkta nosaukums: ")
  produkta_kategorija = input("Produkta kategorija: ")
  produkta_cena = float(input("Cena(EUR): "))
  Pirkumu_saraksts[Produkta_nosaukums]={"Produkta kategorija": produkta_kategorija,
                                            "Produkta cena(EUR)": produkta_cena,
                                            "Pirkuma statuss": "Vajag pirkt"}            
  print(Produkta_nosaukums, "pievienots iepirkuma sarakstam.")

def dzest_produktu_no_saraksta():
  Produkta_nosaukums = input("Ievadiet produkta nosaukumu, kuru vajag izdzēst: ")
  if Produkta_nosaukums in Pirkumu_saraksts:
    del Pirkumu_saraksts[Produkta_nosaukums]
    print(Produkta_nosaukums, "ir izdzēsts no saraksta\n")
  else:
    print("Produkts nav atrasts iepirkumu sarakstā.")

def apskatit_sarakstu():
  if not Pirkumu_saraksts:
    print("Iepirkumu saraksts ir tukšs\n")
    return
  for Produkta_nosaukums, i in Pirkumu_saraksts.items():
    print(Produkta_nosaukums + ' | ' + i['Produkta kategorija'] + ' | ' + str(i['Produkta cena(EUR)']) + " EUR | " + i['Pirkuma statuss'])
  print()

def perkamo_un_nopirkto_produktu_izmaksas():
  summa_nopirktajiem_produktiem = sum(i['Produkta cena(EUR)'] for i in Pirkumu_saraksts.values() if i["Pirkuma statuss"] == "Nopirkts")
  summa_perkamajiem_produktiem = sum(i['Produkta cena(EUR)'] for i in Pirkumu_saraksts.values() if i["Pirkuma statuss"] == "Vajag pirkt")
  print(f"Produkti nopirkti par:{summa_nopirktajiem_produktiem:.2f}EUR")
  print(f"Produkti jāpērk par:{summa_perkamajiem_produktiem:.2f}EUR\n")

def apstiprinat_ka_nopirkts():
  Produkta_nosaukums = input("Produkta nosaukums, kas ir nopirkts: ")
  if Produkta_nosaukums in Pirkumu_saraksts:
    Pirkumu_saraksts[Produkta_nosaukums]["Pirkuma statuss"]="Nopirkts"
    print(Produkta_nosaukums, "ir nopirkts.\n")
  else:
    print('Produkts nav atrasts iepirkumu sarakstā.')

def opcijas():
  while True:
    print("1. Pievienot produktu iepirkuma sarakstam")
    print("2. Dzēst produktu no iepirkuma saraksta")
    print("3. Apskatīt iepirkuma sarakstu")
    print("4. Apstriprināt produktu, kas ir nopirkts")
    print("5. Apskatīt izmaksas nopirktam un perkamam precem")
    print("6. Beigt programmu")

    lietotaja_opcija = input("Opcija no 1 līdz 6: ")

    if lietotaja_opcija == "1":
      pievienot_iepirkuma_sarakstam()
    elif lietotaja_opcija == "2":
      dzest_produktu_no_saraksta()
    elif lietotaja_opcija == "3":
      apskatit_sarakstu()
    elif lietotaja_opcija == "4":
      apstiprinat_ka_nopirkts()
    elif lietotaja_opcija == "5":
      perkamo_un_nopirkto_produktu_izmaksas()
    elif lietotaja_opcija == "6":
      break
    else: print("Jāizvēlas opcija no 1 līdz 6\n")


    


if __name__ == "__main__":
  opcijas()


