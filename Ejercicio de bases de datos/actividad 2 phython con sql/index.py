import sqlite3
#crea variable que equivalente a la conexion de la base de datos
conexion = sqlite3.connect('dbDaniels')

cursor1 =conexion.cursor()
#crea tabla
cursor1.execute('''create table usuarios(
    nombre varchar(20),
    edad int,
    direccion varchar(50),
    telefono int (10)
)''')
#inserta datos
cursor1.execute("insert into usuarios values('Daniels', 22, 'calle 23 No.9-30', 3005887411 )")


# creamos la variable que tenga la lista de elementos
usuarios_extra =[
    ("juan", 20, "avenida florida",3148759877),
    ("Goku", 60, "kamehouse",123456789),
    ("frank", 30, "la jungla",3448795622),
    ("Don corleone vito", 60, "italia",66624879),

]
#insertar en forma de listas 
cursor1.executemany('insert into usuarios values(?,?,?,?)',usuarios_extra)
#envia cambios como el git
conexion.commit()

conexion.close();