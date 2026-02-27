import sqlite3
import matplotlib.pyplot as plt
import argparse
from sqlite3 import Error
import os

class NewBD():
    
    def __init__()-> None:
        pass
    
    def sql_connection():
        """Inicializa la base de datos y crea la tabla de gastos si no existe."""
        """Create a connection with SQLite database specified by the mytest.db file
        :param con: the connection object
        :return: connection object or Error"""
        try:
            # Conectar a la base de datos (o crearla si no existe)
            conn = sqlite3.connect('Datas.db')
            print("conexion exitosa")
            return conn
        except Error:
            #si hay un error al conectar a la base de datos, se imprime el error
            print(Error)


    # Crear una tabla
    def create_table(conn,StringQuery):
        """Create the table with given columns"""
        try:
            # Crear un cursor para ejecutar consultas
            cursor = conn.cursor()
            cursor.execute(StringQuery)
            # committing our connection
            conn.commit()
            #no se que hace commit, pero creo que sirve para crear la tabla, o para guardar los cambios en la base de datos, o algo asi
            print('The table is created successfully')
        except Error:
            print(Error)

    """#Establecer conexión
    conn = sql_connection(BD = 'Datas.db')"""

    #Para agregar registros a la agenda
    def add_data(conn, Categoria,Descripcion,Fecha,Monto):
        """ The second method to add records into the table"""        
        try:            
            cur = conn.cursor()
            #cur.execute("INSERT INTO employees VALUES(2, 'David', 'Anderson', 'IT', 'Dev', 3000, '2020-06-01')")
            #cur.execute("INSERT INTO employees VALUES(3, 'Tom', 'Roger', 'IT', 'Manager', 3000, '2018-03-02')")
            cur.execute("INSERT INTO gastos (Categoria,Descripcion,Fecha,Monto) VALUES(?, ?, ?, ?)",(Categoria,Descripcion,Fecha,Monto))
            conn.commit()#si me sigue pareciendo que es eso, y que execute sirve para almacenar lo que se quiere hacer antes de enviar commit            
            print("The records added successfully")
        except Error:
            print(Error)


    def select_all(conn, StringQuery):
        """Selects all rows from the table to display"""
        try:
            cur = conn.cursor()
            cur.execute(StringQuery)
            rows = cur.fetchall()
            for row in rows:
                print(row)            
            return rows
        except Error:
            print(Error)


    def update_data(conn,item_id, Categoria,Descripcion,Fecha,Hora):
        """Update the table with given new values"""
        try:
            cur = conn.cursor()
             
            print ("UPDATE gastos SET Categoria = ?, Descripcion = ?, Fecha = ? WHERE id = ?;",(Categoria,Descripcion,Fecha,item_id))
            cur.execute("UPDATE gastos SET Categoria = ?, Descripcion = ?, Fecha = ? WHERE id = ?;",(Categoria,Descripcion,Fecha,item_id))
            conn.commit()
      
            print("The record updated successfully")
        except Error:
            print(Error)


    def delete_record(conn, ID):
        """Delete the given record"""
        query = "DELETE FROM gastos WHERE id = ?;"
        try:
            cur = conn.cursor()
            cur.execute(query, (ID,))
            conn.commit()
  
            print("The record deleted successfully")
        except Error:
            print(Error)

    

con = NewBD.sql_connection()
NewBD.create_table(con, ''' CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Categoria TEXT NOT NULL,
            Descripcion TEXT NOT NULL DEFAULT 'Sin descripcion',
            Fecha TEXT NOT NULL,
            Monto REAL NOT NULL
        )'''
    )
        

    #Agregar regristro a agenda
    #add_data(conn,'Prueba3', 'Prueba de agenda3', '2019-04-15', '08:23')

    #Seleccionar registro de agenda
NewBD.select_all(con,'SELECT * FROM Agenda')