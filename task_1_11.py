# BMI = Gewicht (kg) / (Größe (m) × Größe (m))
# BMI = 70 / (1,75 × 1,75) = 22,86 kg/m²

Gewicht = int(input("Gebe dein Gewicht ein (kg): "))
Groesse = float(input("Gebe deine Grösse ein (meter): "))

BMI = Gewicht / (Groesse * Groesse)

print(f"Dein BMI ist {BMI:.2f} kg/m².")