print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 16: Reto: arma tu bubble tea")

# ===== DECISIÓN 1: EL TAMAÑO =====
print("\n===== TAMAÑOS =====")
print("1 = Chico ($55)")
print("2 = Mediano ($70)")
print("3 = Grande ($85)")

tamano = int(input("Elige tu tamaño: "))

if tamano == 1:
    nombre_tamano = "Chico"
    precio_bebida = 55

elif tamano == 2:
    nombre_tamano = "Mediano"
    precio_bebida = 70

elif tamano == 3:
    nombre_tamano = "Grande"
    precio_bebida = 85

else:
    print("Opción no válida, te damos tamaño chico")
    nombre_tamano = "Chico"
    precio_bebida = 55

# ===== DECISIÓN 2: EL TOPPING =====
print("\n===== TOPPINGS =====")
print("1 = Perlas de tapioca ($15)")
print("2 = Jelly de frutas ($12)")
print("3 = Sin topping ($0)")

topping = int(input("Elige tu topping: "))

if topping == 1:
    nombre_topping = "Perlas de tapioca"
    precio_topping = 15

elif topping == 2:
    nombre_topping = "Jelly de frutas"
    precio_topping = 12

elif topping == 3:
    nombre_topping = "Sin topping"
    precio_topping = 0

else:
    print("Opción no válida, va sin topping")
    nombre_topping = "Sin topping"
    precio_topping = 0

# ===== TOTAL =====
total = precio_bebida + precio_topping

print("\n===== TU PEDIDO =====")
print(f"Tamaño: {nombre_tamano} ${precio_bebida}")
print(f"Topping: {nombre_topping} ${precio_topping}")
print(f"TOTAL: ${total}")