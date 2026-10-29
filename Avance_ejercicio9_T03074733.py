print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 9: Tamaño de tu bebida")

# Mostramos el menú
print("\n===== MENÚ DE TAMAÑOS =====")
print("1 = Chico ($55)")
print("2 = Mediano ($70)")
print("3 = Grande ($85)")

opcion = int(input("\n¿Qué tamaño quieres? Escribe 1, 2 o 3: "))

if opcion == 1:
    print("Elegiste tamaño CHICO, son $55")

elif opcion == 2:
    print("Elegiste tamaño MEDIANO, son $70")

elif opcion == 3:
    print("Elegiste tamaño GRANDE, son $85")

else:
    print("Opción no válida, elige 1, 2 o 3")

print("\n¡Gracias por tu compra!")