def calcular_precio_entrada(edad):
    if edad <= 0:
        return "La edad debe ser mayor que cero."
    elif edad < 18:
        return 7
    elif 18 <= edad <= 50:
        return 15
    else:
        return 5
while True:
    try:
        edad = int(input("Ingrese la edad de la persona: "))
        precio = calcular_precio_entrada(edad)

        if isinstance(precio, int):
            print(f"El precio de la entrada es de {precio} soles.")
        else:
            print(precio)

    except ValueError:
        print("Por favor, ingrese un número entero válido para la edad.")
