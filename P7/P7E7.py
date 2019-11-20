"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento. El procedimiento contará el número de vocales (de cada una) que aparecen, y lo imprimirá por pantalla.
"""
def contvocal(a):
    d=0
    for i in range(0,len(a)):
        if (a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
            d=d+1
    print(f'en la frase ({a}) aparecen {d} vocales')    
    
frase=input('introducir frase: ')
contvocal(frase)
