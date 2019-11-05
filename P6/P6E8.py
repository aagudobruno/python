"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.
"""
n1=int(input('introducir número a igualar: '))
x=int(input('introduce un valor: '))
suma=x
numeros=[x]
k=1
while (suma!=n1):
    x=int(input('introduce otro valor: '))
    suma=suma+x
    while (suma>n1):
        suma=suma-x
        x=int(input(f'valor no válido, excede {n1},introducir valor menor: '))
        suma=suma+x
    k=k+1
    numeros=numeros+[x]    
print('el número a igualar era',n1,'la lista creada es:',end=' ')
for i in range(0,k):
    if i<=k-2:
        print(numeros[i],end=',')
    else:
        print(numeros[i])
    
