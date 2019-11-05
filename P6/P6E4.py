"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. El programa termina escribiendo los dos números tal y como se pide:
"""
N1=int(input('introducir un número: '))
N2=int(input('introducir otro número mayor: '))
while (N1>=N2):
    print(N2,'no es mayor que',N1)
    N1=int(input('introducir un número: '))
    N2=int(input('introducir otro número mayor: '))
print('los números escritos son',N1,'y',N2)           
