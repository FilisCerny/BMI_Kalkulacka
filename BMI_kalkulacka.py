# Vstupni hodnoty
jmeno=input("Jak se jmenujes? : ")
vaha=float(input("Kolik vazis kilogramů?: "))
vyska=float(input("Kolik meris v metrech?: "))
# Vypocet
bmi=vaha/(vyska ** 2)

# kategorie
kategorie = ''
if bmi > 40:
    kategorie = 'těžká obezita'
elif bmi > 30:
    kategorie = 'obezita'
elif bmi > 25:
    kategorie = 'mírná nadváha'
elif bmi > 18.5:
    kategorie = 'zdravá váha'
else:
    kategorie = 'podvýživa'

# Výsledek
print(jmeno, "tvé BMI je", str(bmi) + ", což spadá do kategorie", kategorie + ".")