print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 12: Playlist segun tu mood")

print("\n===== ¿CÓMO TE SIENTES HOY? =====")
print("1 = Feliz")
print("2 = Triste")
print("3 = Con energía")
print("4 = Estudiando")

mood = int(input("\nEscribe el número de tu mood: "))

if mood == 1:
    print("Te recomiendo una playlist de pop")

elif mood == 2:
    print("Te recomiendo una playlist de baladas")

elif mood == 3:
    print("Te recomiendo una playlist de reggaetón o K-pop")

elif mood == 4:
    print("Te recomiendo una playlist de lo-fi para concentrarte")

else:
    print("Ese mood no está en la lista")