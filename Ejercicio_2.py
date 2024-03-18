
'''
Crea un programa que permita adivinar un número. El rango es de 0 a 10 números y va respondiendo si el número
 a adivinar es mayor o menor que el introducido,a demás de los intentos que te quedan (tienes 3 intentos para acertarlo). 
 El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de 
 intentos termina el programa
 '''


import random

#Definimos las variables globales  y la función principal
def adivinar_numero():
    numero_a_adivinar = random.randint(0, 10)
    intentos_maximos = 3
    intentos_realizados = 0

#Mostramos los mensajes de inicio del juego 
    print("¡Bienvenido al juego de adivinar el número!")
    print("Tienes 3 intentos para adivinar el número del 0 al 10.")
    

#Iniciamos Ciclo while que se repite mientras no se cumpla la condición de parada    
    while intentos_realizados < intentos_maximos:
        intentos_realizados += 1
        intentos_restantes = intentos_maximos - intentos_realizados
        

        #Pedimos al usuario un número y comprobamos si es correcto o no
        numero_introducido = int(input(f"Intento {intentos_realizados}. Introduce un número entre 0 y 10: "))
        
        if numero_introducido < numero_a_adivinar:
            print("El número a adivinar es mayor.")
        elif numero_introducido > numero_a_adivinar:
            print("El número a adivinar es menor.")
        else:
            print(f"¡Felicidades! ¡Has adivinado el número en {intentos_realizados} intentos!")
            return
        

        #Verificamos si se han agotados los intentos, salimos del bucle while en tal caso
        if intentos_restantes > 0:
            print(f"Te quedan {intentos_restantes} intentos.")
        else:
            print("Has agotado todos tus intentos. ¡Fin del juego!")

    print(f"El número a adivinar era: {numero_a_adivinar}")


adivinar_numero()
5