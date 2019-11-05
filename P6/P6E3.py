"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas. 
"""
p=int(input('introducir una nota, escribir notas que no este entre 0 y 10 \
        \npara parar de introducir las notas: '))
notas=[]

while(p>=0 and p<=10):
    notas=notas+[p]
    p=int(input('introducir una nota, escribir notas que no este entre 0 y 10 \
        \npara parar de introducir las notas: '))        
print('las notas introducidas son:',notas)
