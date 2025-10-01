# Programa para clasificar la edad de una persona
# Pide el nombre y la edad de nacimiento y clasifica según el rango de edad

def edadClasificar(edad):
    """
    Función que clasifica la edad en tramos:
    - Menos de 18 -> Niño
    - Entre 18 y 65 -> Adulto
    - Mayor de 65 -> Anciano
    """
    if edad < 18:
        return "Niño"
    elif 18 <= edad <= 65:
        return "Adulto"
    else:
        return "Anciano"

def main():
    # Pedimos nombre
    nombre = input("Introduce tu nombre: ")

    # Manejo de errores para la entrada de edad
    while True:
        try:
            anio_nacimiento = int(input("Introduce tu año de nacimiento (YYYY): "))
            # Calculamos edad aproximada
            from datetime import datetime
            anio_actual = datetime.now().year
            edad = anio_actual - anio_nacimiento

            # Verificamos que la edad tenga sentido
            if edad < 0 or edad > 120:
                print("⚠️ Año de nacimiento no válido, intenta de nuevo.")
                continue
            break
        except ValueError:
            print("⚠️ Debes introducir un número válido para el año.")

    # Clasificamos la edad
    clasificacion = edadClasificar(edad)

    # Mostramos el resultado
    print(f"\nHola {nombre}, tienes {edad} años y eres clasificado como: {clasificacion}.")

# Ejecutamos el programa
if __name__ == "__main__":
    main()
