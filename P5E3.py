"""AUTOR:ADRIÁN AGUDO BRUNO
   ENUNCIADO:Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.
"""
N1=int(input('introducir primer número: '))
N2=int(input('introducir segundo número mayor que el anterior: '))
SUMA=[]
N3=0
for i in range(N1,N2+1):
    N3=N3+i
    SUMA=SUMA + [i]
print('la suma de los números entre',N1,'y',N2,'=',N3,'y son:',SUMA)
