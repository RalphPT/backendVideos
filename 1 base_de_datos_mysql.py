# psycopg2 > sirve para poder conectarse a las BD en POSTGRES
# pip install psycopg2
# mysqlclient > permite conectarnos a BD en MYSQL
# pip install mysqlclient
from MySQLdb import _mysql

conexion = _mysql.connect(host = 'localhost', user='root', password='root', database ='pruebas')
conexion.query("SELECT * FROM usuarios;")

resultado = conexion.store_result()

print(resultado.fetch_row())