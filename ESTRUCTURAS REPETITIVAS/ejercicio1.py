
numerosPositivos = 0
numerosNegativos = 0
numerosNeutros=0
i = 0
while i < 20:
    numero = float(input("Introduce un número: "))
    if numero > 0:
        numerosPositivos += 1
    elif numero < 0:
        numerosNegativos += 1
    elif numero==0:

        numerosNeutros +=1
    i += 1
print(f"Cantidad de números positivos: {numerosNegativos}")
print(f"Cantidad de números negativos: {numerosPositivos}")
print(f"cantidad de numeros Neutros :{numerosNeutros}")
