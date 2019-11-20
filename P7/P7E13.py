"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que le pida al usuario si quiere calcular
   si un número es primo con for o con while, por tanto,
   habrán dos funciones que se caracterizan
   por hacer ese mismo cálculo de una manera (con for y sin breaks), o de otra (con while). Ambas funciones devolverá true (si es es primo) o false (si no es primo). El programa principal informará del resultado. Además, como mejora puedes calcular el tiempo que tarda en encontrar la solución de una manera u otra. Comentario: aprovecha el código que tienes ya creado
"""
def esPrimoWhile(a):
    l=[]
    i=a
    while(i!=0):
        if (a%i==0):
            l=l+[i]
        i=i-1      
    if (len(l)>2):
        return(True)
    else:
        return(False)

def esPrimoFor(b):
    l=[]
    for i in range(b,0,-1):
        if (b%i==0):
            l=l+[i]
    if (len(l)>2):
        return(True)
    else:
        return(False)
    
option=int(input('introducir 1 si quiere hacer el programa con un for, \no 2 si lo prefiere hacer con while: '))
n1=int(input('introducir un número: '))
if (option==1):
    if (esPrimoFor(n1)):
        print(n1,'NO es un número primo')
    else:
        print(n1,'SÍ es un número primo')
else:
    if (esPrimoWhile(n1)):
        print(n1,'NO es un número primo')
    else:
        print(n1,'SÍ es un número primo')
        
