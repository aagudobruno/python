"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que te pida una frase, y pase la frase como parámetro a una función. Ésta debe devolver si es palíndroma o no , y el programa principal escribirá el resultado por pantalla.
"""
def capi_o_pal(a):
    b=0
    c='n'
    a1=a.replace(" ","")
    for i in range(0,len(a1)):
        if (a1[i]==a1[len(a1)-1-i]):
           b=b+1     
    if (b==len(a1)):
        c='s'    
    return(c)
pal=input('introduce una plábra o un número: ')
if (capi_o_pal(pal)=='s'):
    print('la palabra/número SÍ es palíndroma/capicua')
else:
    print('la palabra/número NO es palíndroma/capicua')
