"""AUTOR:ADRIÁN AGUDO BRUNO
   ENUNCIADO:Escribe un programa que pida un número y escriba si primo o no"""
N1=int(input('introducir un número: '))
L=[]
for i in range(N1,0,-1):
    if (N1%i==0):
        L=L+[i]
if (len(L)>2):
    print(N1,'NO es un número primo')
else:
    print(N1,'SÍ es un número primo')    
