import sqlite3  # Bases de datos SQLite
from pydantic import BaseModel  # Pydantic para validado

#Definicion de la clase Relojes que hereda de BaseModel
class Relojes(BaseModel):
    #Atributos del modelo
    serie: str
    color: str
    marca: str
    modelo: str
    duenno: str

    #Metodo para actualizar los atributos del objeto
    def nueva(self, serie, color, marca, modelo, duenno):
        self.serie = serie
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.duenno = duenno

    #Metodo para guardar el objeto en la base de datos
    def guardaenBD(self):
        con = sqlite3.connect('Relojeria.db')  #Conexion a la base de datos
        cur = con.cursor()  #cursor para ejecutar comandos SQL
        sql = f'''INSERT INTO Relojes(serie, color, marca, modelo, duenno) VALUES (
        '{self.serie}', 
        '{self.color}', 
        '{self.marca}', 
        '{self.modelo}', 
        '{self.duenno}')'''  #SQL para insertar un registro
        cur.execute(sql)  #Ejecución del comando SQL
        con.commit()  #Confirmación de la transaccion
        con.close()  #Cierre de la conexion

#Metodo para eliminar el objeto de la base de datos
    def eliminaenBD(self):
        con = sqlite3.connect('Relojeria.db')  # Conexion a la base de datos
        cur = con.cursor()  # Cursor para ejecutar comandos SQL
        sql = f'''DELETE FROM Relojes WHERE serie = '{self.serie}'''  # SQL para eliminar un registro
        cur.execute(sql)  #Ejecucion del comando SQL
        con.commit()  #Confirmacion de la transaccion
        con.close()  #Cierre de la conexion

#Metodo para actualizar el objeto en la base de datos
    def actualizaenBD(self):
        con = sqlite3.connect('Relojeria.db')  #Conexion a la base de datos
        cur = con.cursor()  # Cursor para ejecutar comandos SQL
        sql = f'''UPDATE Relojes SET color = '{self.color}', 
        marca = '{self.marca}', 
        modelo = '{self.modelo}', 
        duenno = '{self.duenno}' 
        WHERE serie = '{self.serie}' '''  #SQL para actualizar un registro
        cur.execute(sql)  #Ejecución del comando SQL
        con.commit()  #Confirmación de la transaccion
        con.close()  #Cierre de la conexion

#Metodo para seleccionar todos los registros de la tabla Relojes
    def seleccionatodoenBD(self):
        con = sqlite3.connect('Relojeria.db')  # Conexión a la base de datos
        cur = con.cursor()  # Cursor para ejecutar comandos SQL
        listaDevolver = []          #lista para almacenar los registros seleccionados
        for fila in cur.execute('SELECT * FROM Relojes'):  # Selección de todos los registros
            objetoInterno = Relojes(serie=fila[0], 
                                    color=fila[1], 
                                    marca=fila[2], 
                                    modelo=fila[3], 
                                    duenno=fila[4])  # Creación de un objeto Relojes por cada registro
            listaDevolver.append(objetoInterno)  # añadir el objeto a la lista
        con.close()  #Cierre de la conexion
        return listaDevolver  #devolucion de la lista de objetos