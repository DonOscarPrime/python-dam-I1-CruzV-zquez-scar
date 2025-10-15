# primo.py
# Verifica si un número es primo

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def divisor_mas_pequeno(n):   # <-- mejora añadida
    """Devuelve el menor divisor > 1 si existe, o None si es primo."""
    if n <= 3:
        return None
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return None

def main():
    num = int(input("Introduce un número: "))

    if es_primo(num):
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
        div = divisor_mas_pequeno(num)
        if div:
            print(f"Su menor divisor (mayor que 1) es: {div}")

if __name__ == "__main__":
    main()