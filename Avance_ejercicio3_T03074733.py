print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 3: Wi-Fi del cafe")

contrasena_cafe = "Latte2026"

nombre = input("¿Cómo te llamas? ")
contrasena = input("Escribe la contraseña: ")
gasto = float(input("¿Cuánto gastaste? "))

if contrasena == contrasena_cafe:
    print("Conectado al Wi-Fi, bienvenida", nombre)
else:
    print("Contraseña incorrecta")

if gasto >= 100:
    print("Tienes 1 hora de Wi-Fi")
else:
    print("Tienes 30 minutos de Wi-Fi")