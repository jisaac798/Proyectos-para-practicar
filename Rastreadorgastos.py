from db_gastos import NewBD
import matplotlib.pyplot as plt
import datetime
import time
import os
import sys

db = NewBD
conexion = db.sql_connection()

while True:
    NewBD.create_table(conexion, ''' CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Categoria TEXT NOT NULL,
            Descripcion TEXT NOT NULL DEFAULT 'Sin descripcion',
            Fecha TEXT NOT NULL,
            Monto REAL NOT NULL
        )'''
    )
    #aqui añado a la base de datos informacion del gasto llamando a una funcion que cree en el otro script
    #
    NewBD.add_data(conexion, input("tipo de gasto: "), input('descripcion: '), datetime.date.today(), int(input("monto: ")))
    print("Registro agregado a la base de datos.")
    rows = NewBD.select_all(conexion, "SELECT * FROM gastos")
    print("Registros actuales en la base de datos:")
    for row in rows:
        print(row)
    plt.pie([row[4] for row in rows], labels=[row[2] for row in rows])
    plt.xlabel('ID del gasto')
    plt.ylabel('Monto del gasto')
    plt.title('Gastos registrados')
    plt.show()
    conexion.close()
    print("La conexión se ha cerrado. El programa se cerrará en 5 segundos.")
    time.sleep(5)
    sys.exit()
    
