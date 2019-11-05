"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. Para acabar de escribir los números, escribe un número que no sea mayor que el anterior. El programa termina escribiendo la lista de números:
"""
n1=int(input('introducir un número: '))
n=[n1]
n2=int(input('introducir otro número mayor: '))
k=1
while (n1<n2):
    print(n2,'es mayor que',n1)
    n=n+[n2]
    n1=n2
    print('introducir otro número mayor que',n1,': ')
    n2=int(input())
    k=k+1             
print('los números escritos son: ')      
for i in range(0,k):
    if i<=k-2:
        print(n[i],end=',')      
    else:
        print(n[i])
