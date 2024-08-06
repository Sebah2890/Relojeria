#Importaciones de la libreria de FastAPI y sus submodulos
from fastapi import FastAPI     
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse

#Importación de modulos 
import persona
import cliente
import relojero
import relojes

#Instancia de la aplicacion FastAPI
app = FastAPI()

#Endpoint (put) informacion de persona
@app.put("/persona")
async def update_persona(item: persona.Persona):
    objetoPersona = persona.Persona(cedula=item.cedula, apellidos=item.apellidos,
                                    correo=item.correo,
                                    nombre=item.nombre,
                                    telefono=item.telefono)
    objetoPersona.guardaenBD()  #guarda la informacion en la base de datos
    return objetoPersona.seleccionatodoenBD()  #devuelve toda la informacion  de la base de datos

#Endpoint(GET) informacion de persona
@app.get("/persona")
async def get_persona():
    objetoPersona = persona.Persona(cedula='', apellidos='',
                                    correo='',
                                    nombre='',
                                    telefono='')
    return objetoPersona.seleccionatodoenBD()  #devuelve toda la informacion de la base de datos

#Endpoint (delete) informacion de persona
@app.delete("/persona")
async def delete_persona(item: persona.Persona):
    objetoPersona = persona.Persona(cedula=item.cedula, 
                                    apellidos='',
                                    correo='',
                                    nombre='',
                                    telefono='')
    objetoPersona.eliminaenBD()  #elimina la informacion de la base de datos
    return objetoPersona.seleccionatodoenBD()  #devuelve toda la informacion de la base de datos

#Endpoint  (post) informacion de persona
@app.post("/persona")
async def create_persona(item: persona.Persona):
    objetoPersona = persona.Persona(cedula=item.cedula, apellidos=item.apellidos,
                                    correo=item.correo,
                                    nombre=item.nombre,
                                    telefono=item.telefono)
    objetoPersona.actualizaenBD()  #Actualiza la informacion en la base de datos
    return objetoPersona.seleccionatodoenBD()  #devuelve toda la informacion de la base de datos

# Endpoint  (put) informacion de cliente
@app.put("/cliente")
async def update_cliente(item: cliente.Cliente):
    objetoPersona = cliente.Cliente(cedula=item.cedula, 
                                    tipo=item.tipo)
    objetoPersona.guardaenBD()  # Guarda la informacion en la base de datos
    return objetoPersona.seleccionatodoenBD()  #devuelve toda la informacion de la base de datos

# Endpoint para obtener (get) informacion de cliente
@app.get("/cliente")
async def get_cliente():
    objetoPersona = cliente.Cliente(cedula='', tipo='')
    return objetoPersona.seleccionatodoenBD()  #devuelve toda la informacion de la base de datos

# Endpoint para obtener (get) un archivo HTML relacionado con cliente
@app.get("/clienteHTML")
async def get_cliente_html():
    return FileResponse("cliente.html")  # Devuelve el archivo cliente.html

# Endpoint para actualizar (put) información de relojero
@app.put("/relojero")
async def update_relojero(item: relojero.Relojero):
    objetoPersona = relojero.Relojero(cedula=item.cedula, 
                                      especialidad=item.especialidad, salarioxHora=item.salarioxHora)
    objetoPersona.guardaenBD()  # Guarda la información en la base de datos
    return objetoPersona.seleccionatodoenBD() #devuelve toda la informacion de la base de datos

# Endpoint para obtener (get) información de relojero
@app.get("/relojero")
async def get_relojero():
    objetoPersona = relojero.Relojero(cedula='', especialidad='', salarioxHora=0)
    return objetoPersona.seleccionatodoenBD()  #devuelve toda la informacion de la base de datos

#Endpoint para obtener (get) un archivo HTML relacionado con relojero
@app.get("/relojeroHTML")
async def get_relojero_html():
    return FileResponse("relojero.html")  #devuelve el archivo relojero.html

#Endpoint para actualizar (put) información de relojes
@app.put("/relojes")
async def update_relojes(item: relojes.Relojes):
    objetoPersona = relojes.Relojes(serie=item.serie, color=item.color, marca=item.marca, 
                                    modelo=item.modelo, duenno=item.duenno)
    objetoPersona.guardaenBD()  #guarda la informacion en la base de datos
    return objetoPersona.seleccionatodoenBD()  #devuelve toda la informacion de la base de datos

#Endpoint (get) informacion de relojes
@app.get("/relojes")
async def get_relojes():
    objetoPersona = relojes.Relojes(serie='', color='', marca='', modelo='', duenno='')
    return objetoPersona.seleccionatodoenBD()  #devuelve toda la informacion de la base de datos

#Endpoint (get) un archivo HTML relacionado con relojes
@app.get("/relojesHTML")
async def get_relojes_html():
    return FileResponse("relojes.html")  #devuelve el archivo relojes.html

#Endpoint (get) un archivo html de persona
@app.get("/personaHTML", response_class=HTMLResponse)
async def get_persona_html():
    objetoPersona = persona.Persona(cedula='', apellidos='', correo='', nombre='', telefono='')
    html = objetoPersona.paginaWeb()  #genera y devuelve la página web con la información de persona
    return html
