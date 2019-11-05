"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los números introducidos supere el límite inicial. El programa termina escribiendo la lista de números.
"""
n1=int(input('introducir número límite: '))
x=int(input('introduce un valor: '))
suma=x
numeros=[x]
k=1
while (suma<n1):
    x=int(input('introduce otro valor: '))
    suma=suma+x
    k=k+1
    numeros=numeros+[x]    
print('el límite a superar era',n1,'la lista creada es:')
for i in range(0,k):
    if i<=k-2:
        print(numeros[i],end=',')
    else:
        print(numeros[i],end=' ')
print('ya que la suma de estos números es',suma)        
        
