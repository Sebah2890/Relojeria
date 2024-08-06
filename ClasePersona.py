from pydantic import BaseModel

class Persona(BaseModel):
    # Atributos de la clase Persona
    cedula: str               # Cédula de identidad
    nombre: str               # Nombre de la persona
    primerapellido: str       # Primer apellido
    segundoapellido: str      # Segundo apellido
    direccion: str            # Dirección de residencia
    correolectronico: str     # Correo electrónico
    tipo: str                 # Tipo de persona (por ejemplo, cliente, empleado)
    clave: str                # Clave o contraseña
