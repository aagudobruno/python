I=int(input("introducir importe en euros: "))
E=0
if(I%500==0):
    E=I/500
    print("el cajero te devuelve",E,"billetes de 500€")
else:
    if(I%200==0):
        E=I/200
        print("el cajero te devuelve",E,"billetes de 200€")
    else:
        if(I%100==0):
            E=I/100
            print("el cajero te devuelve",E,"billetes de 100€")
        else:
            if(I%50==0):
                E=I/50
                print("el cajero te devuelve",E,"billetes de 50€")
            else:
                if(I%20==0):
                    E=I/20
                    print("el cajero te devuelve",E,"billetes de 20€")
                else:
                    if(I%10==0):
                        E=I/10
                        print("el cajero te devuelve",E,"billetes de 10€")
                    else:
                        if(I%5==0):
                            E=I/5
                            print("el cajero te devuelve",E,"billetes de 5€")
                        else:
                            print("lo siento,no le puedo dar el importe deseado")
                    
    
    
    
