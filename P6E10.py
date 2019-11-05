"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo de 0 a 10, el programa entenderá que no quieres introducir más notas de este alumno. Si no escribes el nombre, el programa entenderá que no quieres introducir más alumnos. Nota: La lista en la que se guardan los nombres y notas tiene esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc].
"""
nom=input('introduce el nombre del alumno: ')
nota=int(input('introducir una nota del 0 al 10: '))
nomxnota=[]
notal=[]
aux=[]
while(nom!=''):
    while(nota>=0 and nota<=10):
        notal.append(nota)
        nota=int(input('introducir otra nota del 0 al 10: '))
    aux.append(nom)
    for i in range(len(notal)):
        aux.append(notal[i])
    notal=[]
    nomxnota.append(aux)
    aux=[]
    nom=input('introduce otro nombre de otro alumno: ')
    if(nom!=''):
        nota=int(input('introducir otra nota del 0 al 10: '))          
for i in range(len(nomxnota)):
    for j in range(len(nomxnota[i])):
        if (j!=0):
            if (j==(len(nomxnota[i])-1)):
              print (nomxnota[i][j],end=' ')
            else: 
              print (nomxnota[i][j],end='-');
        else:
              print (nomxnota[i][j],end=':')
        

            
