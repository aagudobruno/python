"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que te pida una frase y una vocal, y pase estos datos como parámetro a una función que se encargará de cambiar todas las vocales de la frase por la vocal seleccionada. Devolverá la función la frase modificada, y el programa principal la imprimirá
"""
def asterisco(a,b):
    for i in range(0,len(a)):
        if (a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
            a[i]=b
    return(a)
    
frase=list(input('introducir frase: '))
vocal=input('introducir vocal: ')
for i in range(0,len(asterisco(frase,vocal))):
    print(asterisco(frase,vocal)[i],end='')
