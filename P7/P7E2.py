"""AUTOR:Adrián Agudo Bruno 
   ENUNCIADO:Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de caracteres diferentes), los pase como parámetros a una función, y ésta debe unirlos y devolver una única cadena. La cadena final la imprimirá el programa por pantalla.
"""
def fun(a,b,c):
    print(f'su nombre completo es {a} {b} {c}')

nom=input('introducir nombre: ')
ap1=input('introducir primer apellido: ')
ap2=input('introducir segundo apellido: ')
fun(nom,ap1,ap2)
