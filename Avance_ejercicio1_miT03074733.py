print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 1: Estado de mi celular")

print("Estado de mi celular\n")

# Pedir datos
bateria = int(input("¿Qué porcentaje de batería tienes? "))
espacio = float(input("¿Cuántos GB libres tienes? "))
notificaciones = int(input("¿Cuántas notificaciones sin leer tienes? "))

# Revisar batería
if bateria <= 20:
    print("Batería baja, conecta tu cargador")

# Revisar espacio
if espacio < 5:
    print("Poco espacio, borra fotos o apps que no uses")

# Revisar notificaciones
if notificaciones > 0:
    print("Tienes", notificaciones, "notificaciones sin leer")
else:
    print("Estás al día, no tienes notificaciones")