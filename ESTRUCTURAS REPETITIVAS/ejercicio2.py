
contador = 0
suma = 0
while contador < 10:
   numero = float(input("Ingresa un número negativo: "))
if numero < 0:
        numero_positivo = -numero
        suma += numero_positivo
        contador += 1
else:
        print("El número ingresado no es negativo. Por favor, ingresa un número negativo.")
print("La suma de los números positivos es:", suma)

