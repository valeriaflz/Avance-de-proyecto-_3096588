print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 2: Crea tu cuenta")

nombre = input("¿Cómo te llamas? ")
anio = int(input("¿En qué año naciste? "))
red_social = input("¿Cuál es tu red social favorita? ")

edad = 2026 - anio

print(nombre + ", tienes", edad, "años")

if edad >= 13:
    print("Tu cuenta en", red_social, "fue creada")
else:
    print("Todavía no puedes crear tu cuenta, te faltan", 13 - edad, "años")

if edad >= 18:
    print("Compras dentro de la app activadas")
else:
    print("Compras dentro de la app desactivadas")