# temperaturas.py
# Convierte grados Celsius a Kelvin o Fahrenheit

def celsius_a_kelvin(c):
    return c + 273.15

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def main():
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    print("¿A qué unidad deseas convertir?")
    print("1. Kelvin")
    print("2. Fahrenheit")
    opcion = input("Elige una opción (1 o 2): ")

    if opcion == "1":
        print(f"{celsius} °C = {celsius_a_kelvin(celsius):.2f} K")
    elif opcion == "2":
        print(f"{celsius} °C = {celsius_a_fahrenheit(celsius):.2f} °F")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
