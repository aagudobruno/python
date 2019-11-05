"""AUTOR:ADRIÁN AGUDO BRUNO
   ENUNCIADO:Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura del triángulo: 4
****
***
**
*

"""
H=int(input('introducir altura del triángulo: '))
for i in range(H,0,-1):
    print('*'*i)    
