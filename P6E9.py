"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que te pida nombres de personas y sus números de teléfono. Para terminar debe pulsar “S” cuando te pida el nombre. El programa termina escribiendo nombres y números de teléfono. Nota: La lista en la que se guardan los nombres y números de teléfono tiene esta estructura[[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.
"""
nom=''
tlf=''
nxt=[]
while(nom!='s'):
    nom=input('introduzca el nombre: ')
    if(nom!='s'):
        tlf=input('introduzca el correspondiente número de teléfono: ')
        nxt.append([nom,tlf])
print('los nombres y teléfonos de la agenda son:')
for i in range(len(nxt)):
    for j in range(len(nxt[i])):
        if (j!=(len(nxt[i])-1)):
            print(nxt[i][j],end=':')
        else:
            print(nxt[i][j])
    
 
    
    
