D,M,A=int(input("introducir dia: ")),int(input("introducir mes: ")),int(input("introducir año: "))
if (M==2):
    if (A%4==0):
        if (D>29):
            print("fecha no válida")
        else:
            print("fecha válida")
    else:
        if (D>28):
            print("fecha no válida")
        else:
            print("fecha válida")
else:
    if (M<=7):
        if (M%2==0):
            if (D>30):
                print("fecha no válida")
            else:
                print("fecha válida")
        else:
            if (D>31):
                print("fecha no válida")
            else:
                print("fecha válida")
    else:
         if (M%2==0):
            if (D>31):
                print("fecha no válida")
            else:
                print("fecha válida")
         else:
            if (D>30):
                print("fecha no válida")
            else:
                print("fecha válida")
