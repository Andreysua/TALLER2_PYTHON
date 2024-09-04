pesosNiños = []
pesosJovenes = []
pesosAdultos = []
pesosAncianos = []
for i in range(50):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    peso = float(input(f"Ingrese el peso de la persona {i+1}: "))
    if edad <= 12:
        pesosNiños.append(peso)
    elif edad <= 29:
        pesosJovenes.append(peso)
    elif edad <= 59:
        pesosAdultos.append(peso)
    else:
        pesosAncianos.append(peso)
def calcular_promedio(pesos, categoria):
    if pesos:
        promedio = sum(pesos) / len(pesos)
        print(f"Promedio de peso en la categoría {categoria}: {promedio:.2f} kg")
calcular_promedio(pesosNiños, "Niños")
calcular_promedio(pesosJovenes, "Jóvenes")
calcular_promedio(pesosAdultos, "Adultos")
calcular_promedio(pesosAncianos, "Ancianos")
