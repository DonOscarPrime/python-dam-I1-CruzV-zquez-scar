# analisis_notas.py
# Programa sencillo para analizar calificaciones

def main():
    # Pedir las notas al usuario
    entrada = input("Introduce las calificaciones separadas por comas: ")

    # Convertir las notas a números
    notas = []
    valores = entrada.split(",")  # Separar por comas
    for valor in valores:
        valor = valor.strip()  # Quitar espacios
        if valor != "":
            try:
                nota = float(valor)
                notas.append(nota)
            except:
                print("Error: todos los valores deben ser números.")
                return  # Salir si hay error

    if len(notas) == 0:
        print("No se introdujeron notas.")
        return

    # Número total de notas
    total = len(notas)

    # Calcular suma, mínima y máxima
    suma = 0
    minimo = notas[0]
    maximo = notas[0]
    for n in notas:
        suma += n
        if n < minimo:
            minimo = n
        if n > maximo:
            maximo = n

    # Calcular media
    media = round(suma / total, 2)

    # Contar aprobados y sobresalientes
    aprobados = 0
    sobresalientes = 0
    for n in notas:
        if n >= 5:
            aprobados += 1
        if n >= 9:
            sobresalientes += 1

    porcentaje_aprobados = round(aprobados * 100 / total, 2)
    porcentaje_sobresalientes = round(sobresalientes * 100 / total, 2)

    # Calcular nota más repetida (moda)
    frecuencias = {}
    for n in notas:
        if n in frecuencias:
            frecuencias[n] += 1
        else:
            frecuencias[n] = 1

    max_frec = 0
    for n in frecuencias:
        if frecuencias[n] > max_frec:
            max_frec = frecuencias[n]

    modas = []
    for n in frecuencias:
        if frecuencias[n] == max_frec:
            modas.append(n)

    # Mensaje final según la media
    if media >= 8:
        mensaje = "Nivel excelente"
    elif media >= 5:
        mensaje = "Nivel medio"
    else:
        mensaje = "Necesita refuerzo"

    # Mostrar resultados
    print("\n--- Resumen de notas ---")
    print("Número total de notas:", total)
    print("Media:", media)
    print("Nota mínima:", minimo)
    print("Nota máxima:", maximo)
    print("Porcentaje de aprobados (>=5):", porcentaje_aprobados, "%")
    print("Porcentaje de sobresalientes (>=9):", porcentaje_sobresalientes, "%")
    print("Nota(s) más repetida(s):", modas)
    print("Mensaje final:", mensaje)


if __name__ == "__main__":
    main()

