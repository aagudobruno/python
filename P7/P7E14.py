"""AUTOR:Adrián Agudo Bruno
   ENUNCIADO:Aprovechando el potencial de los diccionarios, escribe un programa que llame a un procedimiento, que recibe como parámetro la fecha en números y devuelve la fecha  con el nombre del mes. Comentario: no es necesario validar si la es correcta, damos por hecho que lo será. 
"""
def F(a):
    DiccMeses={'01':'Enero',
               '02':'Febrero',
               '03':'Marzo',
               '04':'Abril',
               '05':'Mayo',
               '06':'Junio',
               '07':'Julio',
               '08':'Agosto',
               '09':'Septiembre',
               '10':'Octubre',
               '11':'Noviembre',
               '12':'Diciembre'}
    dia=(f'{a[0]}{a[1]}')
    mes=(f'{a[3]}{a[4]}')
    año=(f'{a[6]}{a[7]}{a[8]}{a[9]}')
    fechaV2=(f'{dia} de {DiccMeses[mes]} del {año}')
    print(fechaV2)
fecha=input('introduce una fecha en formato dd/mm/aaaa: ')
F(fecha)
