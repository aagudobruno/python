"""AUTOR:ADRIÁN AGUDO BRUNO
   ENUNCIADO:Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje de la siguiente manera:
Anchura del rectángulo: 5
Altura del rectángulo: 3
*****
*****
*****

"""
B=int(input('introducir base del rectángulo: '))
H=int(input('introducir altura del rectángulo: '))
for i in range(H,0,-1):
    print(B*'*')
    
