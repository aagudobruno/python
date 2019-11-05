N1=int(input("introducir primer número: "))
N2=int(input("introducir segundo número: "))
N3=int(input("introducir tercero número: "))
N4=int(input("introducir número divisor de los tres últimos: "))
if (N1%N4==0):
    if (N2%N4==0):
        if (N3%N4==0):
            print("el número SÍ es divisor de los otros tres")
        else:
            print("el número NO es divisor de los otros tres")
    else:
        print("el número NO es divisor de los otros tres")
else:
    print("el número NO es divisor de los otros tres")
