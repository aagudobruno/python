"""AUTOR:ADRIÁN AGUDO BRUNO
   ENUNCIADO:Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura de un triángulo: 5
    *
   ***
  *****
 *******
*********
"""

h=int(input('introducir altura del triángulo: '))
for i in range(h,0,-1):
        print(' '*(i)+'* '*((h+1)-i))
        

