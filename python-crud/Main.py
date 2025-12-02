# Main con menu
from models.DAO import UsuarioDAO

# Limpiar pantalla
def limpiar_pantalla():
    print("\n" * 2)

# Mostrar menú principal
def mostrar_menu():
    print("\n" + "="*60)
    print("           📋 SISTEMA DE GESTIÓN DE USUARIOS")
    print("="*60)
    print("1. 🆕 Crear nuevo usuario")
    print("2. 📋 Listar todos los usuarios")
    print("3. 🔍 Buscar usuario por ID")
    print("4. ✏️  Actualizar usuario")
    print("5. 🗑️  Eliminar usuario")
    print("6. ❌ Salir")
    print("="*60)

# Menu crear usuario
def opcion_crear(dao):
    """Opción 1: Crear usuario"""
    limpiar_pantalla()
    print("---  CREAR NUEVO USUARIO ---\n")
    
    rut = input("Ingrese RUT (ej: 12345678-9): ")
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    
    dao.crear(rut, nombre, apellido)

# Menu Listar
def opcion_listar(dao):
    limpiar_pantalla()
    print("--- 📋 LISTA DE USUARIOS ---\n")
    
    usuarios = dao.listar_todos()
    
    if not usuarios:
        print("No hay usuarios registrados")
        return
    
    # Mostrar tabla
    print(f"{'ID':<5} {'RUT':<15} {'Nombre':<20} {'Apellido':<20}")
    print("-" * 60)
    
    for u in usuarios:
        print(f"{u['Id_user']:<5} {u['Rut']:<15} {u['Nombre']:<20} {u['Apellido']:<20}")
    
    print(f"\nTotal de usuarios: {len(usuarios)}")

# Menu Buscar
def opcion_buscar(dao):
    limpiar_pantalla()
    print("--- BUSCAR USUARIO ---\n")
    
    try:
        id_user = int(input("Ingrese ID del usuario: "))
    except ValueError:
        print("Error: Debe ingresar un número")
        return
    
    usuario = dao.buscar_por_id(id_user)
    
    if usuario:
        print("\n Usuario encontrado:")
        print(f"   ID:       {usuario['Id_user']}")
        print(f"   RUT:      {usuario['Rut']}")
        print(f"   Nombre:   {usuario['Nombre']}")
        print(f"   Apellido: {usuario['Apellido']}")
    else:
        print(f" No se encontró usuario con ID {id_user}")

# Menu Actualizar
def opcion_actualizar(dao):
    limpiar_pantalla()
    print("--- ACTUALIZAR USUARIO ---\n")
    
    try:
        id_user = int(input("Ingrese ID del usuario a actualizar: "))
    except ValueError:
        print("Error: Debe ingresar un número")
        return
    
    # Verificar si existe
    usuario = dao.buscar_por_id(id_user)
    if not usuario:
        print(f"No existe usuario con ID {id_user}")
        return
    
    # Mostrar datos actuales
    print(f"\nDatos actuales:")
    print(f"   RUT:      {usuario['Rut']}")
    print(f"   Nombre:   {usuario['Nombre']}")
    print(f"   Apellido: {usuario['Apellido']}")
    
    # Pedir nuevos datos
    print(f"\nIngrese nuevos datos:")
    rut = input("Nuevo RUT: ")
    nombre = input("Nuevo Nombre: ")
    apellido = input("Nuevo Apellido: ")
    
    # Actualizar
    dao.actualizar(id_user, rut, nombre, apellido)

# Menu Eliminar
def opcion_eliminar(dao):
    limpiar_pantalla()
    print("--- ELIMINAR USUARIO ---\n")
    
    try:
        id_user = int(input("Ingrese ID del usuario a eliminar: "))
    except ValueError:
        print("Error: Debe ingresar un número")
        return
    
    # Verificar si existe
    usuario = dao.buscar_por_id(id_user)
    if not usuario:
        print(f"No existe usuario con ID {id_user}")
        return
    
    # Mostrar datos y confirmar
    print(f"\n⚠️  Está a punto de eliminar:")
    print(f"   ID:       {usuario['Id_user']}")
    print(f"   RUT:      {usuario['Rut']}")
    print(f"   Nombre:   {usuario['Nombre']} {usuario['Apellido']}")
    
    confirmacion = input("\n¿Está seguro? (s/n): ")
    
    if confirmacion.lower() == 's':
        dao.eliminar(id_user)
    else:
        print("❌ Operación cancelada")

# Funcion principal
def main():
    print("\n Iniciando Sistema de Gestión de Usuarios...")
    
    # Crear instancia del DAO
    dao = UsuarioDAO()
    
    # Bucle principal
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-6): ")
        
        if opcion == '1':
            opcion_crear(dao)
        elif opcion == '2':
            opcion_listar(dao)
        elif opcion == '3':
            opcion_buscar(dao)
        elif opcion == '4':
            opcion_actualizar(dao)
        elif opcion == '5':
            opcion_eliminar(dao)
        elif opcion == '6':
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print(" Opción inválida. Por favor seleccione 1-6")
        
        input("\n[Presione ENTER para continuar...]")

if __name__ == "__main__":
    main()