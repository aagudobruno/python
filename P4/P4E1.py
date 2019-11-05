N1=int(input("introducir primer número: "))
N2=int(input("introducir segundo número: "))
N3=int(input("introducir tercero número: "))
N4=int(input("introducir cuarto número: "))
N5=int(input("introducir quinto número: "))
minimo=N1
maximo=N1
if(N2>maximo):
    maximo=N2
if(N3>maximo):
    maximo=N3
if(N4>maximo):
    maximo=N4
if(N5>maximo):
    maximo=N5
print("el número máximo es:",maximo)
if(N2<minimo):
    minimo=N2
if(N3<minimo):
    minimo=N3
if(N4<minimo):
    minimo=N4
if(N5<minimo):
    minimo=N5
print("el número mínimo es:",minimo)        
        
        
    
