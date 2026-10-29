print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 13: Mensaje segun tu calificacion")

calificacion = int(input("\n¿Qué calificación sacaste en el examen de Cisco? "))

print("\n===== RESULTADO =====")

if calificacion > 100:
    print("Calificación no válida, debe ser de 0 a 100")

elif calificacion < 0:
    print("Calificación no válida, debe ser de 0 a 100")

elif calificacion >= 90:
    print("¡Excelente! Eres crack")

elif calificacion >= 80:
    print("Muy bien")

elif calificacion >= 70:
    print("Aprobaste, pero puedes mejorar")

else:
    print("Reprobaste, ¡a estudiar!")