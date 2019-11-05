"""AUTOR:ADRIÁN AGUDO BRUNO
   ENUNCIADO:Escribe un programa que pida un número e imprima todos sus divisores."""
N1=int(input('introducir un número: '))
L=[]
for i in range(N1,0,-1):
    if (N1%i==0):
        L=L+[i]
print ('los divisores de',N1,'son:',L)        
