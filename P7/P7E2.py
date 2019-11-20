"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de caracteres diferentes), los pase como parámetros a una función, y ésta debe unirlos y devolver una única cadena. La cadena final la imprimirá el programa por pantalla.
"""
def fun(a,b,c):
    d=(f'su nombre completo es {a} {b} {c}')
    return(d)
nom=input('introducir nombre: ')
ap1=input('introducir primer apellido: ')
ap2=input('introducir segundo apellido: ')
print(fun(nom,ap1,ap2))
