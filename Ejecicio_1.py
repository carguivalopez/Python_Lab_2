''' 
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
'''

#Ejercicio_1

#Se solicita al usuario la cantidad de numeros a ingresar
def contar_numeros():
    cantidad_numeros = int(input("cantidad de numeros a introducir: "))

#Se inician las variables para guardar los valores y su conteo
    numeros_mayores_cero = 0
    numeros_menores_cero = 0
    numeros_iguales_cero = 0
    
#Bucle for para recopilar los datos del usuario
    for _ in range(cantidad_numeros):
        numero = float(input("Introduce un número: "))
#Se definen las condicionales         
        if numero > 0:
            numeros_mayores_cero += 1
        elif numero < 0:
            numeros_menores_cero += 1
        else:
            numeros_iguales_cero += 1

#Impresión final la evaluacion de cada tipo de dato        
    print(f"Números mayores que 0: {numeros_mayores_cero}")
    print(f"Números menores que 0: {numeros_menores_cero}")
    print(f"Números iguales a 0: {numeros_iguales_cero}")

contar_numeros()
