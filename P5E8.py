"""AUTOR:ADRIÁN AGUDO BRUNO
   ENUNCIADO:Escribe un programa que pida la anchura de un triángulo y lo dibuje de la siguiente manera:
Altura del triángulo: 4
*
**
***
****
***
**
*
"""
A=int(input('introducir la anchura del triángulo: '))
B=A//2
if (A%2==0):
    for i in range(0,B+1):
        print('*'*i)
    for i in range(B,0,-1):
        print('*'*i)
else:
    for i in range(0,B+2):
        print('*'*i)
    for i in range(B,0,-1):
        print('*'*i)    
    
        
        
