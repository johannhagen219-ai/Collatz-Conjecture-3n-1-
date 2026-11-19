import math

ergebnis = math.sqrt(16)
print(ergebnis)  
zahl = int(input("Gib mir eine Startnummer: "))
schritte = 0

while zahl != 1:
    schritte += 1
    if zahl % 2 == 0:
        print(zahl, "ist gerade -> teile durch 2")
        zahl = zahl // 2
    else:
        print(zahl, "ist ungerade -> mal 3 plus 1")
        zahl = zahl * 3 + 1

print("Fertig! Wir sind nach", schritte, "Schritten bei 1 angekommen.")

