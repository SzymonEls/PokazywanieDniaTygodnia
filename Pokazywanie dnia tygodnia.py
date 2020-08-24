#Sczytywanie daty
inp = input("Podaj date(DD-MM-RRRR):")

#Zmiana na zmienne
dzien = int(inp[:2])
miesiac = int(inp[3:5])
rok = int(inp[6:])

#Czyprzestępny
if rok % 4 == 0:
        czyprze = 1
else:
        czyprze = 0

#Zmienne  
dnia = 0

#miesiace
mcc_p = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mcc = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Zamina miesięcy na dni        
licznik = 0
while licznik != miesiac - 1:
        if czyprze == 1:
                dnia = dnia + mcc_p[licznik]
        else:
                dnia = dnia + mcc[licznik]
        licznik = licznik + 1      
    
#Zamiana reszty na dni
dnia = dnia + dzien
dnia = dnia + (rok - 1) * 365
dnia = int(dnia + (((rok - 1) - (rok - 1) % 4) / 4))

#Roznica
roznica = dnia - 700919 

#Pokazywanie dnia tygodnia
tydzien = ["poniedziałek", "wtorek", "środę", "czwartek", "piątek", "sobotę", "niedzielę"]
print("Podana data wypada w/we {m}".format(m=tydzien[roznica % 7]))
