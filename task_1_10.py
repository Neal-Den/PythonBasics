"""
Erstelle ein Programm, das folgende Aufgabe löst:

Frage einen Benutzer, welche Distanz (km) er auf seiner geplanten Reise zurücklegen möchte.
Frage einen Benutzer, wie schnell (km/h) sein Auto durchschnittlich fährt und wie hoch der Verbrauch des Autos in Liter Benzin pro 100km ist.
Gib die Fahrzeit in Minuten und den gesamten Benzinverbrauch aus.
"""

km = int(input("Wie weit ist deine Reise? (km): "))
speed = int(input("Wie schnell färst du im Durchschnitt? (kmh): "))
verbrauch = int(input("Wieviel benzin verbraucht dein auto auf 100km? (Liter): "))

totalverbrauch = int((verbrauch/100)*km)
dauer = int((km/speed)*60)

print(f"Die Fahrt dauert {dauer} Minuten und dein auto verbraucht {totalverbrauch} Liter Benzin auf der strecke.")