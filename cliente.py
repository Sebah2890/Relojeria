import sqlite3
from pydantic import BaseModel

# Definición de la clase Cliente que hereda de BaseModel
class Cliente(BaseModel):
    cedula : str
    tipo : str

    # Método para inicializar una nueva instancia de Cliente
    def nueva(self, cedula, tipo):
        self.cedula = cedula
        self.tipo = tipo

    # Método para guardar la instancia en la base de datos
    def guardaenBD(self):
        con = sqlite3.connect('Relojeria.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Cliente(cedula, tipo) VALUES (
        '{self.cedula}', 
        '{self.tipo}')'''
        cur.execute(sql)
        con.commit()
        con.close()

    # Método para eliminar la instancia de la base de datos
    def eliminaenBD(self):
        con = sqlite3.connect('Relojeria.db')
        cur = con.cursor()
        sql = f'''DELETE FROM Cliente WHERE cedula = '{self.cedula}''' 
        cur.execute(sql)
        con.commit()
        con.close()

    # Método para actualizar la instancia en la base de datos
    def actualizaenBD(self):
        con = sqlite3.connect('Relojeria.db')
        cur = con.cursor()
        sql = f'''UPDATE Cliente SET tipo = 
        '{self.tipo}' WHERE cedula = '{self.cedula}'''
        cur.execute(sql)
        con.commit()
        con.close()

    # Método para seleccionar todas las instancias de la base de datos
    def seleccionatodoenBD(self):
        con = sqlite3.connect('Relojeria.db')
        cur = con.cursor()
        listaDevolver = []
        for fila in cur.execute('SELECT * FROM Cliente'):
            objetoInterno = Cliente(cedula = fila[0], tipo = fila[1])
            listaDevolver.append(objetoInterno)
        con.close()
        return listaDevolver