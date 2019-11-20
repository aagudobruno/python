"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que lea el nombre de una persona y un carácter, le pase estos datos a una función que comprobará si dicho carácter está en su nombre. El resultado de dicha función lo imprimirá el programa principal por pantalla.
"""
def busca(a,b):
    c='NO'
    for i in range(0,len(a)):
        if (a[i]==b):
           c='SI' 
    return(c)

name=input('introducir nombre completo: ')
char=input('introducir una letra de su nombre: ')
if ((busca(name,char))=='SI'):
    print(f'la letra {char} SÍ se encuentra en su nombre:{name}')
else:
    print(f'la letra {char} NO se encuentra en su nombre:{name}')
