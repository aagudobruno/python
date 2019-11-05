"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter. El programa termina escribiendo la lista de palabras.
"""
p=input('introducir una palabra, pulsar enter para terminar \nde introducir las palabras: ')
palabras=[]
while(p!=''):
    palabras=palabras+[p]
    p=input('introducir una palabra, pulsar enter para terminar \nde introducir las palabras: ')
print('las palabras introducidas son:',palabras)
