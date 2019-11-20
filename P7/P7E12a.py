"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribir un programa que lea una frase, y pase ésta como parámetro a una función que debe contar el número de palabras que contiene. Debe imprimir el programa principal el resultado. Asumir que cada palabra está separada por un solo blanco:
Asumir que cada palabra está separada por un solo blanco.
"""
def capi_o_pal(a):
    b=1
    for i in range(0,len(a)):
        if (a[i]==' '):
           b=b+1         
    return(b)
pal=list(input('introduce una frase: '))
print(f'en la frase introducida hat {capi_o_pal(pal)} palabras')
    
