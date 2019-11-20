"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que pida una frase, y pase la frase como parámetro a una función que debe eliminar los espacios en blanco (compactar la frase). El programa principal imprimirá por pantalla el resultado final.
"""
def rima(a,b):
    if (a[len(a)-1]==b[len(b)-1]):
        if (a[len(a)-2]==b[len(b)-2]):
            if (a[len(a)-3]==b[len(b)-3]):
                print(f'las palabras {a} y {b} riman')
            else:
                print(f'las palabras {a} y {b} riman un poco')
    else:            
        print(f'las palabras {a} y {b} NO riman')
    
p1=input('introducir primera palabra: ')
p2=input('introducir segunda palabra: ')
rima(p1,p2)
