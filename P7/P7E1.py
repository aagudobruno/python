"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que pida un texto por pantalla, este texto lo pase como parámetro a un procedimiento, y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.
"""
def proc(a):
    print(a.lower())
    print(a.upper())    
            
txt=input('introduzca un texto: ')
proc(txt)
