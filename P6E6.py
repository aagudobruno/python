"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios. Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales. El programa termina escribiendo la lista de números.
"""
n1=int(input('introducir número mínimo: '))
n2=int(input('introducir número máximo: '))
x=int(input(f'introduce un número entre {n1} y {n2}: '))
numeros=[]
k=0
while (n1<x<n2):
    numeros=numeros+[x]
    x=int(input(f'introduce un número entre {n1} y {n2}: '))
    k=k+1
print('los números son:',end=' ')
for i in range(0,k):
    if i<=k-2:
        print(numeros[i],end=',')
    else:
        print(numeros[i])
