print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 11: ¿Que me pongo hoy?")

temperatura = int(input("\n¿Cuántos grados hace hoy? "))

print("\n===== OUTFIT DEL DÍA =====")

if temperatura < 10:
    print("Hace mucho frío: chamarra, bufanda y botas")

elif temperatura < 20:
    print("Está fresco: sudadera y jeans")

elif temperatura < 30:
    print("Está agradable: playera y tenis")

else:
    print("Hace mucho calor: short, gorra y mucha agua")