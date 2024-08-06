import sqlite3

# Conectar a la base de datos (o crearla si no existe)
con = sqlite3.connect('Relojeria.db')
cur = con.cursor()

# Crear la tabla Persona si no existe
cur.execute("""CREATE TABLE IF NOT EXISTS Persona (
 cedula TEXT PRIMARY KEY,        
 nombre TEXT,                     
 apellidos TEXT,                   
 correo TEXT,                    
 telefono TEXT                     
);""")
con.commit()

# Crear la tabla Cliente si no existe
cur.execute("""CREATE TABLE IF NOT EXISTS Cliente (
 cedula TEXT PRIMARY KEY,        
 tipo TEXT,                       
 CONSTRAINT fk_cliente_persona FOREIGN KEY (cedula)  # Clave foránea que referencia a Persona
 REFERENCES Persona (cedula)
);""")
con.commit()

# Crear la tabla Relojero si no existe
cur.execute("""
CREATE TABLE IF NOT EXISTS Relojero (
 cedula TEXT PRIMARY KEY,          
 especialidad TEXT,         
 salarioxHora REAL,              
 CONSTRAINT fk_relojero_persona FOREIGN KEY (cedula)  # Clave foránea que referencia a Persona
 REFERENCES Persona (cedula)
);""")
con.commit()

# Crear la tabla Relojes si no existe
cur.execute("""
CREATE TABLE IF NOT EXISTS Relojes (
 serie TEXT PRIMARY KEY,        
 color TEXT,                     
 marca TEXT,                      
 modelo TEXT,                     
 duenno TEXT,                     
 CONSTRAINT fk_relojes_cliente FOREIGN KEY (duenno)  
 REFERENCES Cliente (cedula)
);""")

con.commit()
con.close()