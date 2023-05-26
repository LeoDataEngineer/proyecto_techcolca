'''Proyecto:
Se deben consultar, editar, eliminar, y actualizar usuarios. Los campos que debe tener la tabla usuario son: (id, nombre, apellido, estado, pais, ciudad, telefono). Debe ubicarse en un repositorio el código. En el archivo readme del repositorio se debe explicar que base de datos usaron, como se implementó. Si es posible hacer un corto video explicando sería ideal, de no mas de 5 minutos.'''

import sqlite3
import os


# Obtener la ruta de la base de datos:
path = os.path.abspath(__file__)
db_path = os.path.join(os.path.dirname(path), 'databasecrud.db')

# Conectar a la base de datos
conn = sqlite3.connect(db_path)

# Bienvenida al programa
def home():
    print("-----------------------------------")
    print("Bienvenido al registro de usuarios!")
    print("-----------------------------------")
    
#Permite agragar nuevos usuarios.
def agregar():
    name = input("Ingrese su Nombre: ").capitalize()
    lastname = input("Ingrese su Apellido: ").capitalize()
    state = input("Ingrese el Estado: ").capitalize()
    country = input("Ingrese el País: ").capitalize()
    city = input("Ingrese la Ciudad: ").capitalize()
    phone = int(input("Ingrese el número de Teléfono: "))
    
    #Inserta en la tabla "users" de la base de datos los nuevos registros.
    conn.execute("INSERT INTO users (name, lastname, state, country, city, phone) VALUES (?, ?, ?, ?, ?, ?)", (name, lastname, state, country, city, phone))
    conn.commit()# confirma y aplica los cambios en la base de datos
    print("Se agregaron los dato de forma exitosa!")

# Recupera todos los registros de la tabla "users" y los muestra en forma de tabla.
def mostrar():
    cursor = conn.execute("SELECT * FROM users") #el objeto cursor retiene los resultados de la consulta. 
    rows = cursor.fetchall() # se llama en el objeto cursor para obtener todos los registros como una lista de tuplas.
    print("Personas registradas:")
    print("----------------------------------------------------------------------")
    print(f"{'Id':<3} {'Nombre':<10} {'Apellido':<10} {'Estado':<10} {'País':<10} {'Ciudad':<10} {'Teléfono':<10}")
    print("----------------------------------------------------------------------")
    for row in rows:
        print(f"{row[0]:<3} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<10} {row[5]:<10} {row[6]:<10}")
    
#Elimina un usuario de la tabla "users" según el ID proporcionado.      
def eliminar(id):
    conn.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    print("El usuario se elimino de forma exitosa!")

#Permite al usuario seleccionar qué campo desea actualizar para un usuario específico y realiza la actualización en la base de datos.
def actualizar(id):
    print()
    print("Seleccione qué dato desea actualizar:")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Estado")
    print("4. País")
    print("5. Ciudad")
    print("6. Teléfono")
    
    opcion = input("Ingrese el número de opción: ")
    
    if opcion == '1':
        name = input("Ingrese el nuevo nombre: ").capitalize()
        conn.execute("UPDATE users SET name=? WHERE id=?", (name, id))
    elif opcion == '2':
        lastname = input("Ingrese el nuevo apellido: ").capitalize()
        conn.execute("UPDATE users SET lastname=? WHERE id=?", (lastname, id))
    elif opcion == '3':
        state = input("Ingrese el nuevo estado: ").capitalize()
        conn.execute("UPDATE users SET state=? WHERE id=?", (state, id))
    elif opcion == '4':
        country = input("Ingrese el nuevo país: ").capitalize()
        conn.execute("UPDATE users SET country=? WHERE id=?", (country, id))
    elif opcion == '5':
        city = input("Ingrese la nueva ciudad: ").capitalize()
        conn.execute("UPDATE users SET city=? WHERE id=?", (city, id))
    elif opcion == '6':
        phone = int(input("Ingrese el nuevo número de teléfono: "))
        conn.execute("UPDATE users SET phone=? WHERE id=?", (phone, id))
    else:
        print("Opción inválida. Intente de nuevo.")
        return
    
    conn.commit()
    print("Usuario actualizado exitosamente!")



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
