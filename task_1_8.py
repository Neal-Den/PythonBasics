zahl = int(input("Nenne mir eine Zahl: "))

if (zahl <20 and zahl >10):
    print(f"Die Zahl {zahl} befindet sich zwischen 10 und 20!")
elif (zahl <0 or zahl >100):
    print(f"Die Zahl {zahl} ist kleiner als 0 oder grösser als 100!")
    
""" Bei'and' müssen alle bedingungen erfüllt sein und bei 'or' muss nur eine der Bedingungen erfüllt sein. """