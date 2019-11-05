"""AUTOR:ADRIÁN AGUDO BRUNO
   ENUNCIADO:Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje de la siguiente manera:
Anchura del rectángulo: 5
Altura del rectángulo: 4
*****
*   *
*   *
*****
"""
A=int(input('introducir anchura: '))
H=int(input('introducir altura: '))
print('*'*A)
for i in range((H-2),0,-1):
    print('*',' '*(A-4),'*')
print('*'*A)    
