print("Sofia Lozano y Fatima Lopez")
print("T03074733 y T03096588")
print("Ejercicio 8: Cuenta entre amigos")

cuenta = float(input("¿Cuánto fue la cuenta? "))
personas = int(input("¿Cuántas personas van a pagar? "))
dinero = float(input("¿Cuánto dinero traes? "))

propina = cuenta * 10 / 100
total = cuenta + propina
por_persona = total / personas

print("Total con propina: $", total, sep="")
print("A cada persona le toca: $", por_persona, sep="")

if dinero >= por_persona:
    print("Te alcanza, te sobran $", dinero - por_persona, sep="")
else:
    print("No te alcanza, te faltan $", por_persona - dinero, sep="")

if por_persona > 300:
    print("Salió caro, la próxima busquen promo")
else:
    print("¡Buen precio!")