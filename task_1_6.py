riegel = 3.20
geld = float(input("Wieviel Geld hast du?: "))

# Anzahl der Riegel, die du kaufen kannst (ganzzahlig)
riegelmenge = int(geld // riegel)

# Restgeld berechnen
restgeld = geld - (riegelmenge * riegel)

print(f"Du kannst dir {riegelmenge} Riegel kaufen.")
print(f"Restgeld: {restgeld:.2f} €")
