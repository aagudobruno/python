"""AUTOR:ADRIÁN AGUDO BRUNO
   ENUNCIADO:Escribe un programa que pida dos números y escriba qué números entre ese par de números son pares y cuáles impares
"""
N1=int(input('introducir primer número: '))
N2=int(input('introducir segundo número mayor que el anterior: '))
NP=[]
NI=[]
for i in range(N1,N2+1):
    if(i%2==0):
        NP=NP + [i]   
    else:
        NI=NI + [i]
print('números pares entre',N1,'y',N2,':',NP)
print('números impares entre',N1,'y',N2,':',NI)
