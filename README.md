


# 📊 Mini Proyecto CRUD con Google Sheets, Pandas y SQLite

Este es un pequeño sistema CRUD (**Crear, Leer, Actualizar, Eliminar**) que utiliza los siguientes componentes:

- **Google Sheets** como fuente de datos inicial.
- **Pandas** para manipular los datos en memoria.
- **SQLite** para migrar los datos a una base de datos local.
- **Requests** para descargar el archivo Excel desde Google Sheets.

---

## 🧰 Requisitos

Asegúrate de tener instaladas las siguientes librerías en tu entorno Python:

```bash
pip install pandas requests openpyxl
```

> **Nota:** `sqlite3` viene preinstalado en Python.  
> `openpyxl` es necesario para trabajar con archivos `.xlsx`.

---

## 📁 Archivos Usados

| Archivo        | Descripción |
|----------------|-------------|
| `hoja.xlsx`    | Archivo descargado desde Google Sheets con los datos iniciales. |
| `personas.db`  | Base de datos SQLite donde se almacenan los datos migrados. |
| `main.py`      | Script principal del programa. |

---

## 🌐 Fuente de Datos

El proyecto descarga automáticamente un archivo Excel desde una hoja de cálculo pública de Google Sheets utilizando su ID:

```
https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx
```

La estructura esperada del archivo es:

| rut  | nombre   | edad |
|------|----------|------|
| 1234 | Juan     | 30   |
| 5678 | María    | 25   |

---

## 🛠️ Funcionalidades Principales

### ✅ Ver todas las personas:
Muestra en consola todos los registros cargados en memoria.

### 🔍 Buscar por RUT:
Busca y muestra la información de una persona por su RUT.

### 🖋 Editar registro:
Permite editar el **nombre**, la **edad** o **ambos** campos de una persona existente.

### ➕ Agregar nueva persona:
Agrega una nueva persona con RUT, nombre y edad al DataFrame en memoria.

### ❌ Eliminar persona:
Elimina una persona por su RUT del DataFrame.

### 🔄 Migrar datos:
Guarda los datos actuales del DataFrame en una tabla SQLite (`personas.db`).

### 💾 Guardar cambios:
Guarda los datos actualizados en el archivo `hoja.xlsx`.

---

## 🚀 Cómo Ejecutar

1. Guarda este código en un archivo llamado `main.py`.
2. Asegúrate de tener instaladas todas las dependencias.
3. Ejecuta el script:

```bash
python main.py
```

---

## 📝 Notas Adicionales

- El archivo `hoja.xlsx` se descarga automáticamente al iniciar el programa.
- Los cambios no se guardan permanentemente hasta que se selecciona la opción "Guardar xlsx" en el menú.
- La base de datos SQLite solo se actualiza cuando se selecciona la opción "Migrar datos".

---
