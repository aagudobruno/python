"""AUTOR:ADRIÁN AGUDO BRUNO
   ENUNCIADO:Escribe un programa que pida un número y calcule su factorial.
"""
N1=int(input('introducir un número: '))
N2=1
for i in range(N1,0,-1):
    N2=N2*i
print('el factorial de el número anterior es:',N2)    
