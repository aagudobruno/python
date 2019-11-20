"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que pida una frase, y pase la frase como parámetro a una función que debe eliminar los espacios en blanco (compactar la frase). El programa principal imprimirá por pantalla el resultado final.
"""
def asterisco(a):
    for i in range(0,len(a)):
        if (a[i]==' '):
            a[i]=''
    return(a)
frase=list(input('introducir frase: '))
for i in range(0,len(asterisco(frase))):
    print(asterisco(frase)[i],end='')
