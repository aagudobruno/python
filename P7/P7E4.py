"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que pida una frase, y le pase como parámetro a una función dicha frase. La función debe sustituir todos los espacios en blanco de una frase por un asterisco, y devolver el resultado para que el programa principal la imprima por pantalla.
"""
def asterisco(a):
    for i in range(0,len(a)):
        if (a[i]==' '):
            a[i]='*'
    return(a)
frase=list(input('introducir frase: '))
for i in range(0,len(asterisco(frase))):
    print(asterisco(frase)[i],end='')
