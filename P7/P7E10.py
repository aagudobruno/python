"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que te pida una palabra o número, pase por parámetro estos datos a una función, y ésta te diga si es o no palíndroma o capicúa. El programa principal imprimirá el resultado de la función:
"""
def capi_o_pal(a):
    b=0
    c='n'
    for i in range(0,len(a)):
        if (a[i]==a[len(a)-1-i]):
           b=b+1     
    if (b==len(a)):
        c='s'    
    return(c)
pal=input('introduce una plábra o un número: ')
if (capi_o_pal(pal)=='s'):
    print('la palabra/número SÍ es palíndroma/capicua')
else:
    print('la palabra/número NO es palíndroma/capicua')
