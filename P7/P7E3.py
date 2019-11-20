"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento, y éste debe mostrar la frase con un carácter en cada línea.
"""

def letra_a_letra (a):
    for i in range(0,len(a)):
        print(a[i])

frase=input('introducir frase: ')
letra_a_letra(frase)
