import openpyxl
from datetime import datetime
Iepirkumu_saraksts = {}
def pievienot_iepirkuma_sarakstam():

  Produkta_nosaukums = input("Produkta nosaukums: ")
  produkta_kategorija = input("Produkta kategorija: ")
  produkta_cena = float(input("Cena(EUR): "))
  Iepirkumu_saraksts[Produkta_nosaukums]={"Produkta kategorija": produkta_kategorija,
                                            "Produkta cena(EUR)": produkta_cena,
                                            "Pirkuma statuss": "Vajag pirkt"}            
  print(Produkta_nosaukums, "pievienots iepirkuma sarakstam.")

def dzest_produktu_no_saraksta():
  Produkta_nosaukums = input("Ievadiet produkta nosaukumu, kuru vajag izdzēst: ")
  if Produkta_nosaukums in Iepirkumu_saraksts:
    del Iepirkumu_saraksts[Produkta_nosaukums]
    print(Produkta_nosaukums, "ir izdzēsts no saraksta\n")
  else:
    print("Produkts nav atrasts iepirkumu sarakstā.")

def apskatit_sarakstu():
  if not Iepirkumu_saraksts:
    print("Iepirkumu saraksts ir tukšs\n")
    return
  for Produkta_nosaukums, i in Iepirkumu_saraksts.items():
    print(Produkta_nosaukums + ' | ' + i['Produkta kategorija'] + ' | ' + str(i['Produkta cena(EUR)']) + " EUR | " + i['Pirkuma statuss'])
  print()

def perkamo_un_nopirkto_produktu_izmaksas():
  summa_nopirktajiem_produktiem = sum(i['Produkta cena(EUR)'] for i in Iepirkumu_saraksts.values() if i["Pirkuma statuss"] == "Nopirkts")
  summa_perkamajiem_produktiem = sum(i['Produkta cena(EUR)'] for i in Iepirkumu_saraksts.values() if i["Pirkuma statuss"] == "Vajag pirkt")
  print(f"Produkti nopirkti par:{summa_nopirktajiem_produktiem:.2f}EUR")
  print(f"Produkti jāpērk par:{summa_perkamajiem_produktiem:.2f}EUR\n")

  
def opcijas():
  while True:
    print("1. Pievienot produktu iepirkuma sarakstam")
    print("2. Dzēst produktu no iepirkuma saraksta")
    print("3. Apskatīt iepirkuma sarakstu")
    print("4. Beigt programmu")

    lietotaja_opcija = input("Opcija no 1 līdz 4: ")

    if lietotaja_opcija == "1":
      pievienot_iepirkuma_sarakstam()
    elif lietotaja_opcija == "2":
      dzest_produktu_no_saraksta()
    elif lietotaja_opcija == "3":
      apskatit_sarakstu()
    elif lietotaja_opcija == "4":
      break
    else: print("Jāizvēlas opcija no 1 līdz 4\n")


    


if __name__ == "__main__":
  opcijas()


