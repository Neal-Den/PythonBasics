riegel = 3.20
geld = float(input("Wieviel Geld hast du?: "))
riegelmenge = int(geld // riegel)
restgeld = geld - (riegelmenge * riegel)

print(f"Du kannst dir {riegelmenge} Riegel kaufen.")
print(f"Restgeld: {restgeld:.2f} Fr.")
