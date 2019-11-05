"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número se trata. El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.
"""
N1=int(input('introducir un número: '))
L=[]
i=N1
while(i!=0):
    if (N1%i==0):
        L=L+[i]
    i=i-1    
if (len(L)>2):
    print(N1,'NO es un número primo')
else:
    print(N1,'SÍ es un número primo') 
"""Es mejor hacerlo con el for, ya que sabemos el números de iteraciones que hay que realizar"""
