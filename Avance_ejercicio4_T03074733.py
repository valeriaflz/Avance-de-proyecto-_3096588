print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 4: Mis estadísticas de creador")

usuario = input("¿Cuál es tu usuario? ")
seguidores = int(input("¿Cuántos seguidores tienes? "))
likes = int(input("¿Cuántos likes tuvo tu último video? "))

if seguidores >= 1000:
    print("Ya puedes hacer lives")
else:
    print("Te faltan", 1000 - seguidores, "seguidores para hacer lives")

if likes > seguidores:
    print("¡Tu último video se hizo viral!")
else:
    print("Sigue publicando, vas bien")