num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Calcular la suma
suma = num1 + num2 + num3

# Calcular la media
media = suma / 3

# Encontrar el número más grande y el más pequeño
mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)

# Calcular el producto de los tres números
producto = num1 * num2 * num3

# Mostrar resultados
print("\nResultados:")
print(f"La suma de los números es: {suma}")
print(f"La media de los números es: {media}")
print(f"El número más grande es: {mayor}")
print(f"El número más pequeño es: {menor}")
print(f"La multiplicación de los números es: {producto}")

