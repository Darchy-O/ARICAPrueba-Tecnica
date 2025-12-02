# CRUD Usuarios - Python + MySQL + Django

Sistema de gestión de usuarios con CRUD completo desarrollado en Python puro y Django, conectado a base de datos MySQL.


## 🎯 Descripción

Aplicación que permite gestionar usuarios mediante operaciones CRUD (Create, Read, Update, Delete) en dos versiones:
1. **Versión consola**: Aplicación Python con menú interactivo
2. **Versión web**: Interfaz Django con formularios HTML

---

## 🛠️ Tecnologías

- Python 3.x
- MySQL 8.0+
- Django 5.x
- mysql-connector-python
- mysqlclient

---

## 📁 Estructura del Proyecto
```
crud-python/
├── main.py                      # Aplicación consola con menú CRUD
├── models/
│   ├── __pycache__
│   ├── conectar.py             # Clase de conexión a MySQL
│   └── DAO.py                  # Data Access Object con operaciones CRUD
├── crud_project/               # Proyecto Django
│   ├── __init__.py
│   ├── settings.py            # Configuración (DATABASES aquí)
│   ├── urls.py                # URLs principales
│   ├── asgi.py
│   └── wsgi.py
├── usuarios/                   # App Django
│   ├── migrations/
│   ├── templates/
│   │   ├── listar.html
│   │   ├── crear.html
│   │   ├── actualizar.html
│   │   └── eliminar.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py              # Modelo Usuario
│   ├── views.py               # Vistas CRUD
│   ├── urls.py                # URLs de la app
│   └── tests.py
├── manage.py
└── README.md
```

---

## ⚙️ Instalación y Configuración

### 1. Crear Base de Datos MySQL
```bash
# Ingresar a MySQL
mysql -u root -p
```
```sql
-- Crear base de datos
CREATE DATABASE personal;

-- Seleccionar base de datos
USE personal;

-- Crear tabla usuario
CREATE TABLE usuario (
    Rut VARCHAR(10),
    Nombre TEXT,
    Apellido TEXT,
    Id_user INT AUTO_INCREMENT PRIMARY KEY
);

-- Insertar datos de prueba (generados con IA)
INSERT INTO usuario (Rut, Nombre, Apellido) VALUES
('12345678-9', 'Juan', 'Pérez'),
('98765432-1', 'María', 'García'),
('11223344-5', 'Pedro', 'López');

-- Verificar datos
SELECT * FROM usuario;
```

**Resultado esperado:**
```
+------------+--------+----------+---------+
| Rut        | Nombre | Apellido | Id_user |
+------------+--------+----------+---------+
| 12345678-9 | Juan   | Pérez    |       1 |
| 98765432-1 | María  | García   |       2 |
| 11223344-5 | Pedro  | López    |       3 |
+------------+--------+----------+---------+
```

### 2. Instalar Dependencias Python
```bash
# Instalar librería para Python puro
pip install mysql-connector-python

# Instalar Django y conector MySQL
pip install django mysqlclient
```

### 3. Configurar Contraseña de Base de Datos

⚠️ **IMPORTANTE**: Antes de ejecutar, configurar contraseña en 2 archivos:

**Archivo 1: `models/conectar.py`**
```python
self.password = 'TU_PASSWORD_AQUI'  # Línea 11
```

**Archivo 2: `crud_project/settings.py`**
```python
DATABASES = {
    'default': {
        ...
        'PASSWORD': 'TU_PASSWORD_AQUI',  # Línea ~80
        ...
    }
}
```

---

## 🔨 Proceso de Desarrollo

### Fase 1: Base de Datos (MySQL)

1. Ingresé a MySQL con: `mysql -u root -p`
2. Creé la base de datos: `CREATE DATABASE personal;`
3. Asigné la base de datos: `USE personal;`
4. Creé la tabla `usuario` con campos: Rut, Nombre, Apellido, Id_user
5. Generé 3 registros de prueba con ayuda de IA
6. Verifiqué con `SELECT * FROM usuario;`

### Fase 2: Python CRUD (Versión Consola)

1. **Estructura inicial:**
   - Creé carpeta `python-crud`
   - Creé `main.py` (archivo principal)
   - Creé carpeta `models/`
   - Creé `models/__init__.py`
   - Creé `models/conectar.py`
   - Creé `models/DAO.py`

2. **Módulo de conexión (`conectar.py`):**
   - Instalé: `pip install mysql-connector-python`
   - Implementé clase `Conectar` con métodos `conectar()` y `desconectar()`
   - Probé la conexión:
```python
   from models.conectar import Conectar
   db = Conectar()
   conexion = db.conectar()
   if conexion:
       db.desconectar(conexion)
```
   -  **Resultado: Éxito**

3. **DAO - Data Access Object (`DAO.py`):**
   - Creé clase `UsuarioDAO` con ayuda de IA Claude
   - Implementé operaciones:
     - `crear()` - INSERT
     - `listar_todos()` - SELECT *
     - `buscar_por_id()` - SELECT WHERE
     - `actualizar()` - UPDATE
     - `eliminar()` - DELETE
   - Probé cada operación:
```python
   from models.DAO import UsuarioDAO
   dao = UsuarioDAO()
   usuarios = dao.listar_todos()
   print(usuarios)
   dao.crear("99999999-9", "Test", "Prueba")
   usuario = dao.buscar_por_id(1)
   print(usuario)
```
   - ✅ **Resultado: Éxito**

4. **Menú interactivo (`main.py`):**
   - Desarrollé con ayuda de Claude y conocimiento propio
   - Implementé menú con 6 opciones:
     1. Crear usuario
     2. Listar usuarios
     3. Buscar por ID
     4. Actualizar usuario
     5. Eliminar usuario
     6. Salir
   - Encajé la lógica con el DAO creado
   - ✅ **Resultado: Funcional**

### Fase 3: Django (Versión Web)

1. **Instalación:**
```bash
   pip install django mysqlclient
```

2. **Creación del proyecto:**
```bash
   django-admin startproject crud_project .
   python manage.py startapp usuarios
```
   - Esto creó carpetas `crud_project/` y `usuarios/`

3. **Configuración (`settings.py`):**
   - Agregué `'usuarios'` en `INSTALLED_APPS`
   - Actualicé `DATABASES` para conectar a MySQL:
   
   **¿Por qué? (Pregunta IA)** Django por defecto usa SQLite. Como ya tenía una base de datos MySQL existente llamada "personal" con la tabla "usuario", necesité configurar Django para que usara esa base de datos en lugar de crear una nueva.

4. **Modelo (`models.py`):**
   - Creé clase `Usuario` conectada a tabla existente
   - Usé `managed = False` para que Django no gestione la tabla

5. **Vistas (`views.py`):**
   - Desarrollé con ayuda de IA Claude
   - Implementé funciones:
     - `listar_usuarios()`
     - `crear_usuario()`
     - `actualizar_usuario()`
     - `eliminar_usuario()`

6. **URLs:**
   - Creé `usuarios/urls.py` con ayuda de Claude
   - Actualicé `crud_project/urls.py` agregando `include`
   
   **¿Por qué? (PREGUNTA IA)** Django necesita saber qué hacer cuando un usuario visita una URL. El archivo `crud_project/urls.py` es el punto de entrada principal, y `usuarios/urls.py` define las rutas específicas de la aplicación. En estos campos se agregó `include` y las rutas a mostrar. Sin esto, Django no sabría qué vista ejecutar para cada URL.

7. **Templates:**
   - Creé carpeta: `mkdir -p usuarios/templates`
   - Creé archivos HTML básicos:
     - `listar.html` - Tabla con todos los usuarios
     - `crear.html` - Formulario de creación
     - `actualizar.html` - Formulario de edición
     - `eliminar.html` - Confirmación de eliminación

8. **Pruebas:**
   - Ejecuté: `python manage.py runserver`
   - Abrí: `http://127.0.0.1:8000/`
   -  **Resultado: Todas las operaciones funcionan correctamente**

### Fase 4: GitHub

1. Borré contraseñas de archivos antes de subir
2. Subí proyecto a GitHub
3. Agregué colaborador `emiliog-1985`

---

## 🤖 Uso de Inteligencia Artificial (Claude)

### Prompts Utilizados:

**1. Generación de datos de prueba:**
```
"Genera 3 INSERT INTO para la tabla usuario con campos Rut (formato chileno), 
Nombre y Apellido"
```

**2. DAO completo:**
```
"Crea una clase UsuarioDAO con métodos CRUD para tabla usuario: 
crear(rut, nombre, apellido), listar_todos(), buscar_por_id(id)"
```

**3. Menú interactivo:**
```
"Ayúdame a crear un main.py con menú en consola que use el DAO. "
```

**4. Modelo Django:**
```
"Crea un modelo Django llamado Usuario que se conecte a mi tabla 'usuario' 
existente. Usa managed=False para que Django no gestione la tabla", me confirmas si django tiene templates"
```

**5. Configuración URLs:**
```
"Ayúdame a configurar las URLs en Django. Necesito que crud_project/urls.py 
use include para redireccionar a usuarios/urls.py donde están las rutas reales"
```

**6. Ayuda crear README:**
```
"Ayúdame a crear un README, esto es lo que he anotado tras el proceso del desarrollo de prueba tecnica : X "
```
En general, fue un proceso Mixto entre IA + Manual.

## 🚀 Ejecución

### Opción 1: Python Consola
# Navegar a la carpeta
cd python-crud

# ⚠️ Configurar contraseña en models/conectar.py primero

# Ejecutar
python main.py
```

**Funcionalidades disponibles:**
- Crear usuario
- Listar todos
- Buscar por ID
- Actualizar
- Eliminar
- Salir

### Opción 2: Django Web
```bash
# ⚠️ Configurar contraseña en crud_project/settings.py primero

# Ejecutar servidor
python manage.py runserver

# Abrir navegador en:
# http://127.0.0.1:8000/
```

**Rutas disponibles:**
- `/` - Listar usuarios
- `/crear/` - Crear usuario
- `/actualizar/<id>/` - Editar usuario
- `/eliminar/<id>/` - Eliminar usuario

---

## ✨ Funcionalidades

### CRUD Completo:

| Operación | Python Consola | Django Web |
|-----------|----------------|------------|
| **Create** | ✅ Opción 1 del menú | ✅ Formulario /crear/ |
| **Read** | ✅ Opción 2: Listar todos<br>✅ Opción 3: Buscar por ID | ✅ Tabla en / |
| **Update** | ✅ Opción 4 del menú | ✅ Formulario /actualizar/id/ |
| **Delete** | ✅ Opción 5 del menú | ✅ Confirmación /eliminar/id/ |


## ⚠️ Notas Importantes

1. **Contraseñas:** Se deben configurar en 2 archivos antes de ejecutar:
   - `models/conectar.py`
   - `crud_project/settings.py`

2. **Base de datos:** Debe existir la BD "personal" con tabla "usuario" antes de ejecutar

3. **Puerto MySQL:** Por defecto usa puerto 3306

4. **Puerto Django:** Por defecto usa 8000 (modificable en runserver)

5. **Archivos ignorados en Git:**
   - Contraseñas (por seguridad)
   - `__pycache__/`
   - `venv/`
   - `*.pyc`

---

## 👤 Autor

Ismael

**Fecha:** 2 de Diciembre, 2024

**Institución:** ARICA - Prueba Técnica


---

## 🔗 Enlaces

- **Repositorio GitHub:** https://github.com/Darchy-O/ARICAPrueba-Tecnica
- **Documentación Django:** https://docs.djangoproject.com/
- **MySQL Connector Python:** https://dev.mysql.com/doc/connector-python/
