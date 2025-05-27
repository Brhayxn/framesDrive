import pandas as pd
import requests
import sqlite3

# ID del archivo
sheet_id = "1PRtkDUT7vzmcXgVwPEW0oOPkUQTdLddb3_cDo-qkSJY"

# URL para exportar como Excel
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx"

# Descargar el archivo
response = requests.get(url)
with open("hoja.xlsx", "wb") as f:
    f.write(response.content)
#dataframe a trabajar
df = pd.read_excel("./hoja.xlsx")

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect("personas.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS personas (
    rut INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
)
""")



# Función para mostrar los datos
def readData():
    print("\nDatos actuales:")
    print(df)
    print()

# Función para seleccionar una persona por RUT
def selectPerson(rut):
    persona = df[df["rut"] == rut]
    if not persona.empty:
        print("\nPersona encontrada:")
        print(persona)
    else:
        print(f"\nNo se encontró ninguna persona con el RUT {rut}")

# Función para editar la edad de una persona
def editPerson(rut, nuevo_nombre=None, nueva_edad=None):
    global df
    persona = df[df["rut"] == rut]

    if persona.empty:
        print(f"\nNo se encontró ninguna persona con el RUT {rut}")
        return

    cambios = []

    if nuevo_nombre is not None:
        df.loc[df["rut"] == rut, "nombre"] = nuevo_nombre
        cambios.append(f"Nombre a '{nuevo_nombre}'")

    if nueva_edad is not None:
        df.loc[df["rut"] == rut, "edad"] = nueva_edad
        cambios.append(f"Edad a {nueva_edad}")

    if cambios:
        print(f"\nDatos actualizados para el RUT {rut}: {', '.join(cambios)}")
    else:
        print("\nNo se realizaron cambios.")

# Función para agregar una persona
def addPerson(rut, nombre, apellido, edad):
    global df
    new_row = {"rut": rut, "nombre": nombre, "apellido": apellido, "edad": edad}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    print(f"\nPersona con RUT {rut} agregada correctamente")

# Función para eliminar una persona
def deletePerson(rut):
    global df
    if df[df["rut"] == rut].empty:
        print(f"\nNo se encontró ninguna persona con el RUT {rut}")
    else:
        df = df[df["rut"] != rut]
        print(f"\nPersona con RUT {rut} eliminada correctamente")

def dataMigration():
    for _, row in df.iterrows():
        cursor.execute("""
        INSERT OR REPLACE INTO personas (rut, nombre, edad)
        VALUES (?, ?, ?)
        """, (row['rut'], row['nombre'], row['edad']))

    # Guardar cambios y cerrar
    conn.commit()
    conn.close()

# Menú CRUD
def menu():
    while True:
        print("=== Menú CRUD ===")
        print("1. Ver todas las personas")
        print("2. Buscar persona por RUT")
        print("3. Editar edad de una persona")
        print("4. Agregar nueva persona")
        print("5. Eliminar persona por RUT")
        print("6. Migrar datos")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            readData()
        
        elif opcion == "2":
            try:
                rut = int(input("Ingresa el RUT a buscar: "))
                selectPerson(rut)
            except ValueError:
                print("\nPor favor ingresa un RUT válido (solo números).")

        elif opcion == "3":
            try:
                rut = int(input("Ingresa el RUT de la persona a editar: "))
                if df[df["rut"] == rut].empty:
                    print(f"\nNo se encontró ninguna persona con el RUT {rut}")
                    continue

                print("¿Qué deseas editar?")
                print("1. Nombre")
                print("2. Edad")
                print("3. Ambos")
                choice = input("Selecciona una opción: ")

                if choice == "1":
                    nuevo_nombre = input("Nuevo nombre: ")
                    editPerson(rut, nuevo_nombre=nuevo_nombre)
                elif choice == "2":
                    nueva_edad = int(input("Nueva edad: "))
                    editPerson(rut, nueva_edad=nueva_edad)
                elif choice == "3":
                    nuevo_nombre = input("Nuevo nombre: ")
                    nueva_edad = int(input("Nueva edad: "))
                    editPerson(rut, nuevo_nombre=nuevo_nombre, nueva_edad=nueva_edad)
                else:
                    print("\nOpción inválida.")

            except ValueError:
                print("\nPor favor ingresa valores válidos.")

        elif opcion == "4":
            try:
                rut = int(input("RUT: "))
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                edad = int(input("Edad: "))
                addPerson(rut, nombre, apellido, edad)
            except ValueError:
                print("\nPor favor ingresa valores válidos.")

        elif opcion == "5":
            try:
                rut = int(input("Ingresa el RUT a eliminar: "))
                deletePerson(rut)
            except ValueError:
                print("\nPor favor ingresa un RUT válido.")
        
        elif opcion == "6":
            dataMigration()
            print("\nDatos migrados correctamente a la base de datos\n")


        elif opcion == "7":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú
menu()

