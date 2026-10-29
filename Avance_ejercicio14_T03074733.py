print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 14: Costo de envio")

pedido = float(input("\n¿Cuánto es tu pedido? $"))
distancia = float(input("¿A cuántos km vives de la tienda? "))

if distancia <= 3:
    costo_envio = 0
    print("\n¡Envío gratis!")

elif distancia <= 10:
    costo_envio = 39
    print("\nEl envío cuesta $39")

elif distancia <= 20:
    costo_envio = 69
    print("\nEl envío cuesta $69")

else:
    costo_envio = 0
    print("\nNo hacemos envíos a más de 20 km, recoge tu pedido en tienda")

total = pedido + costo_envio

print(f"Pedido: ${pedido:.2f}")
print(f"Envío: ${costo_envio:.2f}")
print(f"TOTAL A PAGAR: ${total:.2f}")