import psycopg2

class Conexion():
    
    def conectar(self):
        coneccion = psycopg2.connect(
            host='localhost',
            database = 'postgres',
            user = 'postgres',
            password = '12345'
        )
        self.cursor = coneccion.cursor()
        

class Conexion_entrada(Conexion):
    def __init__(self,id,nombre,telefono):
        self.conectar()
        self.cursor.execute("""INSERT INTO clientes (cedula,nombre,telefono) VALUES (%s , %s, %s )""",({id},{nombre},{telefono}))
        
        
        
        