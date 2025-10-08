# primo.py
# Verifica si un número es primo

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    num = int(input("Introduce un número: "))

    if es_primo(num):
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")

if __name__ == "__main__":
    main()
