import pymysql.cursors

class Conexion:
    def __init__(self):
        
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    database='hospedaje',
                                    cursorclass=pymysql.cursors.DictCursor)
        # with connection:
        #     with connection.cursor() as cursor:
        #         # Create a new record
        #         sql = "INSERT INTO `tipo_usuario` (`nombre`) VALUES (%s)"
        #         cursor.execute(sql, ('administrador'))

        #     # connection is not autocommit by default. So you must commit to save
        #     # your changes.
        #     connection.commit()

        #     with connection.cursor() as cursor:
        #         # Read a single record
        #         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        #         cursor.execute(sql, ('webmaster@python.org',))
        #         result = cursor.fetchone()
        #         print(result)