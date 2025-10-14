zahl1 = int(input("Nenne mir eine Zahl: "))
zahl2 = int(input("Nenne mir eine zweite Zahl: "))

if zahl1 > zahl2:
    print(f"Die Zahl {zahl1} ist grösser als die Zahl {zahl2}!")
elif zahl1 == zahl2:
    print(f"Die Zahl {zahl1} ist gleich gross wie die Zahl {zahl2}!")
else:
    print(f"Die Zahl {zahl1} ist kleiner als die Zahl {zahl2}!")