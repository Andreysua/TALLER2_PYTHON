# se escribe los contadores
numeroPersonas = int(input("Introduce el número total de personas en el salón: "))
contadorHombres = 0
contadorMujeres = 0
contadorActual = 0

# Bucle para procesar cada persona
while contadorActual < numeroPersonas:
    # se Solicitar el género de la persona
    genero = input("Introduce el género de la persona (hombre/mujer): ")
    
    # se actualizan los contadores
    if genero == "hombre":
        contadorHombres += 1
    elif genero == "mujer":
        contadorMujeres += 1
    else:
        print("Género no válido. Introduce 'hombre' o 'mujer'.")
        continue  # Volver a preguntar si el género no es el correcto
    
    # Incrementar el contador de personas ingresadas
    contadorActual += 1

# Mostrar los resultados
print(f"Cantidad de hombres: {contadorHombres}")
print(f"Cantidad de mujeres: {contadorMujeres}")