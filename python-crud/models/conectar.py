# Conexión a MySQL
import mysql.connector
from mysql.connector import Error

# Clase para manejar la conexión a la base de datos
class Conectar:
    
    def __init__(self):
        self.host = 'localhost'
        self.database = 'personal'
        self.user = 'root'
        self.password = 'CONTRASEÑA PONER, BORRADA POR SEGURIDAD' 

    # Conecta a la base de datos
    def conectar(self):
        try:
            conexion = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            
            if conexion.is_connected():
                print("Conexión exitosa a MySQL")
                return conexion
                
        except Error as e:
            print(f"Error de conexión: {e}")
            return None
        
        finally:
            print("Intento de conexión finalizado")
    
    # Cierra la conexión a la base de datos
    def desconectar(self, conexion):
        if conexion and conexion.is_connected():
            conexion.close()
            print("Conexión cerrada")