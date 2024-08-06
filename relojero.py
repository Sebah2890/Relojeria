import sqlite3 # Bases de datos SQLite
from pydantic import BaseModel  # Pydantic para validado

class Relojero(BaseModel):
    cedula: str
    especialidad: str
    salarioxHora: int

    #mEtodo para inicializar un nuevo relojero
    def nueva(self, cedula, especialidad, salarioxHora):
        self.cedula = cedula
        self.especialidad = especialidad
        self.salarioxHora = salarioxHora

    #Metodo para guardar el relojero en la base de datos
    def guardaenBD(self):
        #Conectar a la base de datos
        con = sqlite3.connect('Relojeria.db')
        cur = con.cursor()
        #Sentencia SQL para insertar un nuevo registro en la tabla Relojero
        sql = f'''INSERT INTO Relojero(cedula, especialidad, salarioxHora) VALUES (
        '{self.cedula}', 
        '{self.especialidad}', 
        {self.salarioxHora})'''
        #Ejecutar la sentencia SQL
        cur.execute(sql)
        #Confirmar los cambios en la base de datos
        con.commit()
        #Cerrar la conexion
        con.close()

    #Mrtodo para eliminar el relojero de la base de datos
    def eliminaenBD(self):
        # Conectar a la base de datos
        con = sqlite3.connect('Relojeria.db')
        cur = con.cursor()
        #Sentencia SQL para eliminar un registro de la tabla Relojero
        sql = f'''DELETE FROM Relojero WHERE cedula = '{self.cedula}''' # Agregar comillas simples alrededor de cedula
        #Ejecutar la sentencia SQL
        cur.execute(sql)
        #Confirmar los cambios en la base de datos
        con.commit()
        #Cerrar la conexion
        con.close()

    #Metodo para actualizar los datos del relojero en la base de datos
    def actualizaenBD(self):
        # Conectar a la base de datos
        con = sqlite3.connect('Relojeria.db')
        cur = con.cursor()
        #Sentencia SQL para actualizar un registro en la tabla Relojero
        sql = f'''UPDATE Relojero SET especialidad = 
        '{self.especialidad}', salarioxHora = 
        {self.salarioxHora} WHERE cedula = '{self.cedula}''' # Agregar comillas simples alrededor de cedula y especialidad
        #Ejecutar la sentencia SQL
        cur.execute(sql)
        #Confirmar los cambios en la base de datos
        con.commit()
        #Cerrar la conexion
        con.close()

    #Metodo para seleccionar todos los relojeros de la base de datos
    def seleccionatodoenBD(self):
        #Conectar a la base de datos
        con = sqlite3.connect('Relojeria.db')
        cur = con.cursor()
        #Lista para almacenar los resultados de la consulta
        listaDevolver = []
        #Ejecutar la consulta para seleccionar todos los registros de la tabla Relojero
        for fila in cur.execute('SELECT * FROM Relojero'):
            #Crear un objeto Relojero por cada fila de la consulta
            objetoInterno = Relojero(cedula=fila[0], 
                                     especialidad=fila[1], 
                                     salarioxHora=fila[2])
            #Añadir el objeto a la lista
            listaDevolver.append(objetoInterno)
        #Cerrar la conexion
        con.close()
        #Devolver la lista de objetos Relojero
        return listaDevolver
  