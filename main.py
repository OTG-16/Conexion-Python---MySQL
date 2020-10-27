import mysql.connector

bd = mysql.connector.connect(
    user='oscar', password='12345678',
    database='proyecto_arbolado')

cursor = bd.cursor()

while True:
    print('1) Agregar usuario')
    print('2) Mostrar usuarios')
    print('0) Salir')
    op = input()

    if op == '1':
        correo_U = input('correo: ')
        contrasena_U = input('contraseña: ')

        consulta = "INSERT INTO usuario (correo_U, contrasena_U) " \
                   "VALUES (%s, %s)" 
        cursor.execute(consulta, (correo_U, contrasena_U))
        bd.commit()
        if cursor.rowcount:
            print('Se agregó usuario')
        else:
            print("Error: No se pudo completar la acción correctamente")

    elif op == '2':
        consulta = "SELECT * FROM usuario"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print('id: ', row[0])
            print('correo: ', row[1])
            print('contraseña: ', row[2])

    elif op == '0':
        break