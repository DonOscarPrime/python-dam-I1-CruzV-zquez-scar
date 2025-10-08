# cadenas.py
# Analiza una cadena de texto y cuenta varios elementos

def main():
    texto = input("Introduce una cadena de texto: ")

    vocales = "aeiouAEIOU"
    num_vocales = sum(1 for c in texto if c in vocales)
    num_consonantes = sum(1 for c in texto if c.isalpha() and c not in vocales)
    num_mayusculas = sum(1 for c in texto if c.isupper())
    num_caracteres = len(texto)

    print(f"\nVocales: {num_vocales}")
    print(f"Consonantes: {num_consonantes}")
    print(f"Mayúsculas: {num_mayusculas}")
    print(f"Número total de caracteres: {num_caracteres}")

if __name__ == "__main__":
    main()
