"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número se trata. El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.
"""
import random
import time
veces=1
random.seed (time.time ())
minimo = int (input ( "Valor mínimo:"))
maximo = int (input ( "Valor máximo:"))
secreto = random.randint (minimo, maximo)
print (f"Piensa un número entre {minimo} y {maximo}, a ver si lo adivino")
n=input(f"Es {secreto}?: ")
while (n!='igual'):
    if (n=='mayor'):
        minimo=secreto
        secreto = random.randint (minimo, maximo)
        n=input(f"Es {secreto}?: ")
    else:
        maximo=secreto
        secreto = random.randint (minimo, maximo)
        n=input(f"Es {secreto}?: ")
print('Grácias!')
