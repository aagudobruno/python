"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, simplemente escribe “Salir”. El programa termina escribiendo la lista de números.
"""
numero=[]
p=' '
p=input('introducir un, escribir SALIR para terminar \nde introducir los números: ')
while(p!='SALIR'):
        numero=numero+[p]
        p=input('introducir un, escribir SALIR para terminar \nde introducir los números: ')
print('los números introducidos son:',numero)
