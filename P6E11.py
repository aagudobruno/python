"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribir un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y luego el usuario va probando valores. El programa va decidiendo si son demasiado grandes o pequeños.
"""
import random
import time
veces=1
random.seed (time.time ())
minimo = int (input ( "Valor mínimo:"))
maximo = int (input ( "Valor máximo:"))
secreto = random.randint (minimo, maximo)
print (f"A ver si adivinas el número entre {minimo} y {maximo}")
n=int(input("Escribe un número: "))
while (n!=secreto):
    if (n > secreto):
        n=int(input('Demasiado grande! Volver a provar:'))
        veces=veces+1
    else:
        n=int(input('Demasiado pequeño! Volver a provar:'))
        veces=veces+1
print(f'Correcto! lo intentaste {veces} veces')
    
