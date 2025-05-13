import openpyxl
from datetime import datetime
Iepirkumu_saraksts = {}
def pievienot_iepirkuma_sarakstam():

  Produkta_nosaukums = input("Produkta nosaukums: "), produkta_kategorija = input("Produkta kategorija: "), produkta_cena = float(input("Cena(EUR): "))
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

