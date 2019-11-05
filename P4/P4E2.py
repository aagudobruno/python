N1=int(input("introducir primer número: "))
N2=int(input("introducir segundo número: "))
N3=int(input("introducir tercero número: "))
N4=int(input("introducir cuarto número: "))
N5=int(input("introducir quinto número: "))
if (N1>N2>N3>N4>N5):
    print("orden descendente")
else:
    if (N1<N2<N3<N4<N5):
        print("orden ascendente")
    else:
        print("desordenados")
