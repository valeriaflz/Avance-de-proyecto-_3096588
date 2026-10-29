print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 10: Nivel de influencer")

usuario = input("\nTu usuario: @")
seguidores = int(input("¿Cuántos seguidores tienes? "))

print(f"\n===== NIVEL DE @{usuario} =====")

if seguidores < 1000:
    print("Nivel: Principiante")

elif seguidores < 10000:
    print("Nivel: Microinfluencer")

elif seguidores < 100000:
    print("Nivel: Influencer")

else:
    print("Nivel: Celebridad digital")