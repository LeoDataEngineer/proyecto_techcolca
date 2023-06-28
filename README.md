# Proyecto final del curso de python 
### Fecha: 26 de Mayo de 2023
### Profesor: Arnol 
### Alumno: LEOMAR
### Academia: TECHCOLCA

## Descripción del proyecto a realizar:
<p>
Se deben consultar, editar, eliminar, y actualizar usuarios. Los campos que debe tener la tabla usuario son: (id, nombre, apellido, estado, pais, ciudad, telefono). Debe ubicarse en un repositorio el código. En el archivo readme del repositorio se debe explicar que base de datos usaron, como se implementó.
<p>

## 1. Importar modulos para el proyecto:
```
import sqlite3
import os 
```
<p>
Importamos estos modulos para interactuar con la basa de datos y el sistema operativo
<p>

## 2. Se crea la conexión a la base de datos:
```
# Obtener la ruta de la base de datos:
path = os.path.abspath(__file__)
db_path = os.path.join(os.path.dirname(path), 'databasecrud.db')

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
```

## 3. Funciones del programa:
```
def agregar() # Permite agragar nuevos usuarios.
def mostrar() # Recupera todos los registros de la db
def eliminar(id) # Elimina el registro de la db
def actualizar(id) # Actualiza la informacion en la db
```
## 4. Línea de código que comienza a correr el programa.
```
# Corremos nuestro programa
home()

while True:
  
    print( """
    ---------------------------      
   | 1. Agregar un usuario    |
   | 2. Mostras los usuarios  |
   | 3. Eliminar un usuario   |
   | 4. Actualizar un usuario |
   | 5. Salir                 |
    ---------------------------
                    """)
    action = input("Ingrese una opción: ")
          
    if action == '5':
        break
    elif action == '1':
        agregar()
    elif action == '2':
        mostrar()
    elif action == '3':
        id = input("Ingrese el ID a eliminar: ")
        eliminar(id)
    elif action == '4':
        id = input("Ingrese el ID ha actualizar: ")
        actualizar(id)
    else:
        print("Acción no permitida. Intete de nuevo.")


# cierre de la conexión de la base de dato
conn.close()
```

## 5. Creación de la base de datos:
- Usamos el motor de base de datos SQLite
- Se creó una tabla llamada users
- Contien los siguientes campos (id, name, lastname, state, country, city, phone)
- Donde el id es nuestra primary key

