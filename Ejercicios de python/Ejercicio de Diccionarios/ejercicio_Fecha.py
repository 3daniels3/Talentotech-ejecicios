
meses_del_anio = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
                 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}

fecha_ingresada = input('Introduce la fecha en formato dd/mm/aaaa: ')
fecha_dividida = fecha_ingresada.split('/')
print(f"{fecha_dividida[0]} de {meses_del_anio[int(fecha_dividida[1])]} de {fecha_dividida[2]}")
