print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 15: Rango en tu videojuego")

puntos = int(input("\n¿Cuántos puntos tienes? "))

print("\n===== TU RANGO =====")

if puntos >= 3000:
    print("Rango: DIAMANTE")
    print("¡Ya estás en el rango máximo!")

elif puntos >= 2000:
    faltan = 3000 - puntos
    print("Rango: ORO")
    print(f"Te faltan {faltan} puntos para Diamante")

elif puntos >= 1000:
    faltan = 2000 - puntos
    print("Rango: PLATA")
    print(f"Te faltan {faltan} puntos para Oro")

else:
    faltan = 1000 - puntos
    print("Rango: BRONCE")
    print(f"Te faltan {faltan} puntos para Plata")