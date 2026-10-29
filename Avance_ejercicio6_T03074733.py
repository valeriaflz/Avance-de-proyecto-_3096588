print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 6: Meta de ahorro")

producto = input("¿Qué quieres comprar? ")
precio = float(input("¿Cuánto cuesta? "))
ahorrado = float(input("¿Cuánto tienes ahorrado? "))
ahorro_semanal = float(input("¿Cuánto ahorras por semana? "))

if ahorrado >= precio:
    print("¡Ya puedes comprar tus", producto + "!")
else:
    faltante = precio - ahorrado
    semanas = faltante / ahorro_semanal

    print("Te faltan $", faltante, " para tus ", producto, sep="")
    print("Ahorrando $", ahorro_semanal, " por semana, los tendrás en ", semanas, " semanas", sep="")