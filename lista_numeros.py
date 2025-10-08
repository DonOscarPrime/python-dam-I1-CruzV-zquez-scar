# lista_numeros.py
# Pide una lista de números separados por comas y los procesa

def main():
    entrada = input("Introduce una lista de números separados por comas: ")
    numeros = [float(x.strip()) for x in entrada.split(",") if x.strip() != ""]

    print(f"\nLista de números: {numeros}")
    print(f"Suma: {sum(numeros)}")
    print(f"Promedio: {sum(numeros)/len(numeros):.2f}")

if __name__ == "__main__":
    main()
