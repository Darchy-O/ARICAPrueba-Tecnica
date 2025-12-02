# DAO (Data Access Object) para tabla usuario
# Implementa las operaciones CRUD

from models.conectar import Conectar

class UsuarioDAO:
    
    def __init__(self):
        self.db = Conectar()
    
    # ==========================================
    # CREATE - Crear nuevo usuario
    # ==========================================
    def crear(self, rut, nombre, apellido):

        conexion = self.db.conectar()
        if not conexion:
            return False
        
        try:
            cursor = conexion.cursor()
            
            # Iniciar transacción
            conexion.start_transaction()
            
            # Query SQL
            query = """
                INSERT INTO usuario (Rut, Nombre, Apellido)
                VALUES (%s, %s, %s)
            """
            valores = (rut, nombre, apellido)
            
            # Ejecutar
            cursor.execute(query, valores)
            
            # Confirmar cambios
            conexion.commit()
            
            print(f" Usuario {nombre} {apellido} creado con ID: {cursor.lastrowid}")
            return True
            
        except Exception as e:
            # Si hay error, deshacer cambios
            conexion.rollback()
            print(f" Error al crear usuario: {e}")
            return False
            
        finally:
            cursor.close()
            self.db.desconectar(conexion)
    
    # ==========================================
    # READ - Leer usuarios, obtiene lista de diccionarios de los usuarios
    # ==========================================
    def listar_todos(self):
        conexion = self.db.conectar()
        if not conexion:
            return []
        
        try:
            cursor = conexion.cursor(dictionary=True)
            
            query = "SELECT * FROM usuario ORDER BY Id_user"
            cursor.execute(query)
            
            usuarios = cursor.fetchall()
            return usuarios
            
        except Exception as e:
            print(f"❌ Error al listar usuarios: {e}")
            return []
            
        finally:
            cursor.close()
            self.db.desconectar(conexion)
    
    # ==========================================
    # READ - Busca usuario por ID y retorna diccionaro con datos del usuario
    # ==========================================
    def buscar_por_id(self, id_user):
        conexion = self.db.conectar()
        if not conexion:
            return None
        
        try:
            cursor = conexion.cursor(dictionary=True)
            
            query = "SELECT * FROM usuario WHERE Id_user = %s"
            cursor.execute(query, (id_user,))
            
            usuario = cursor.fetchone()
            return usuario
            
        except Exception as e:
            print(f"Error al buscar usuario: {e}")
            return None
            
        finally:
            cursor.close()
            self.db.desconectar(conexion)
    
    # ==========================================
    # UPDATE - Actualizar usuario
    # ==========================================
    def actualizar(self, id_user, rut, nombre, apellido):
        conexion = self.db.conectar()
        if not conexion:
            return False
        
        try:
            cursor = conexion.cursor()
            
            conexion.start_transaction()
            
            query = """
                UPDATE usuario 
                SET Rut = %s, Nombre = %s, Apellido = %s
                WHERE Id_user = %s
            """
            valores = (rut, nombre, apellido, id_user)
            
            cursor.execute(query, valores)
            conexion.commit()
            
            print(f"✅ Usuario ID {id_user} actualizado exitosamente")
            return True
            
        except Exception as e:
            conexion.rollback()
            print(f"❌ Error al actualizar usuario: {e}")
            return False
            
        finally:
            cursor.close()
            self.db.desconectar(conexion)
    
    # ==========================================
    # DELETE - Eliminar usuario
    # ==========================================
    def eliminar(self, id_user):
        conexion = self.db.conectar()
        if not conexion:
            return False
        
        try:
            cursor = conexion.cursor()
            
            conexion.start_transaction()
            
            query = "DELETE FROM usuario WHERE Id_user = %s"
            cursor.execute(query, (id_user,))
            
            conexion.commit()
            
            print(f"Usuario ID {id_user} eliminado exitosamente")
            return True
            
        except Exception as e:
            conexion.rollback()
            print(f"Error al eliminar usuario: {e}")
            return False
            
        finally:
            cursor.close()
            self.db.desconectar(conexion)

