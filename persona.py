import sqlite3 # Bases de datos SQLite
from pydantic import BaseModel  # Pydantic para validado
# Definición de la clase Persona que hereda de BaseModel
class Persona(BaseModel):
    cedula : str
    nombre : str
    apellidos : str
    correo : str
    telefono : str

    # Método para inicializar una nueva instancia de Persona
    def nueva(self, cedula, nombre, apellidos, correo, telefono):
        self.cedula = cedula
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.telefono = telefono

    # Método para guardar la instancia en la base de datos
    def guardaenBD(self):
        con = sqlite3.connect('Relojeria.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Persona(cedula, nombre, apellidos, correo, telefono) VALUES (
        '{self.cedula}', 
        '{self.nombre}', 
        '{self.apellidos}', 
        '{self.correo}', 
        '{self.telefono}')'''
        cur.execute(sql)
        con.commit()
        con.close()

    # Método para eliminar la instancia de la base de datos
    def eliminaenBD(self):
        con = sqlite3.connect('Relojeria.db')
        cur = con.cursor()
        sql = f'''DELETE FROM Persona WHERE cedula = {self.cedula}'''
        cur.execute(sql)
        con.commit()
        con.close()

    # Método para actualizar la instancia en la base de datos
    def actualizaenBD(self):
        con = sqlite3.connect('Relojeria.db')
        cur = con.cursor()
        sql = f'''UPDATE Persona SET nombre = 
        '{self.nombre}', apellidos = 
        '{self.apellidos}', correo = 
        '{self.correo}', telefono = 
        '{self.telefono}' WHERE cedula = {self.cedula}'''
        cur.execute(sql)
        con.commit()
        con.close()

    # Método para seleccionar todas las instancias de la base de datos
    def seleccionatodoenBD(self):
        con = sqlite3.connect('Relojeria.db')
        cur = con.cursor()
        listaDevolver = []
        for fila in cur.execute('SELECT * FROM persona'):
            objetoInterno = Persona(
                cedula = fila[0], 
                apellidos = fila[2],
                correo = fila[3],
                nombre = fila[1],
                telefono = fila[4]
            )
            listaDevolver.append(objetoInterno)
        return listaDevolver

    # Método para generar el HTML de la página web
    def paginaWeb(self):
        return '''<html><head>
        <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0px;
        }

        .navbar {
            background-color: #007bff;
            padding: 15px;
            color: white;
            margin-bottom: 10px;
        }

        .navbar ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
        }

        .navbar ul li {
            margin: 0 15px;
        }

        .navbar ul li a {
            color: white;
            text-decoration: none;
            font-size: 18px;
            padding: 8px 16px;
            border-radius: 4px;
            font-family: sans-serif;
        }

        .navbar ul li a:hover {
            background-color: #0056b3;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .Texto, select, .numero {
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            width: calc(80% - 22px);
            box-sizing: border-box;
            outline: none;
            border-radius: 100px;
        }

        .boton {
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            background-color: #007bff;
            color: white;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
        }

        .boton:hover {
            background-color: #0056b3;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: #ffffff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }

        th {
            background-color: #007bff;
            color: white;
        }

        #espacioTabla {
            margin-top: 20px;
        }
        </style>
        </head>
        <body>

        <!-- Barra de navegación -->
        <div class="navbar">
            <ul>
                <li><a href="/clienteHTML">Cliente</a></li>
                <li><a href="/relojesHTML">Relojes</a></li>
                <li><a href="/relojeroHTML">Relojero</a></li>
            </ul>
        </div>

        <!-- Campos de entrada para los datos de la persona -->
        <input class="Texto" id="cedula" type="text" placeholder="Escriba su cedula"/>
        <input class="Texto" id="nombre" type="text" placeholder="Escriba su nombre"/>
        <input class="Texto" id="apellidos" type="text" placeholder="Escriba sus apellidos"/>
        <input class="Texto" id="correo" type="text" placeholder="Escriba su correo"/>
        <input class="Texto" id="telefono" type="text" placeholder="Escriba su telefono"/>
        
        <!-- Botón para guardar o modificar -->
        <input class="boton" id="btnaccion" type="button" value="Ingresar" onclick="guardar()"/>
        
        <!-- Espacio para la tabla -->
        <div id="espacioTabla">
            <table>
                <thead>
                    <tr>
                        <td>Cedula</td>
                        <td>Nombre</td>
                        <td>Apellidos</td>
                        <td>Correo</td>
                        <td>Telefono</td>
                        <td>Modificar</td>
                        <td>Eliminar</td>
                    </tr>
                </thead>
                <tbody id="cuerpoTabla">
                    <!-- Filas de la tabla se rellenarán aquí -->
                </tbody>
            </table>
        </div>

        <script>
        listadepersonas = []

        // Función para cargar los datos de las personas desde el servidor
        function cargarDatos() {
            var objetoaenviar = new Object();
            try {
                var xhr = new XMLHttpRequest();
                xhr.open('GET', '/persona');
                xhr.setRequestHeader('Content-Type', 'application/json');
                xhr.onload = function() {
                    if (xhr.status == 200) {
                        console.log(JSON.parse(xhr.responseText));
                        rellenaTabla(JSON.parse(xhr.responseText))
                    } else {
                        console.log(xhr);
                    }
                };
                xhr.send();
            } catch (err) {
                console.log(err.message);
            }
        }

        // Función para rellenar la tabla con los datos de las personas
        function rellenaTabla(vector) {
            listadepersonas = vector
            document.getElementById("cuerpoTabla").innerHTML = ""
            document.getElementById("cuerpoTabla").innerHTML += "<tr>"
            for (var elemento in vector) {
                document.getElementById("cuerpoTabla").innerHTML += "<td>" + vector[elemento].cedula + "</td><td>" + vector[elemento].nombre + "</td><td>" + vector[elemento].apellidos + "</td><td>" + vector[elemento].correo + "</td><td>" + vector[elemento].telefono + "</td><td><input type='button' value='Modificar' onclick='modificar(" + vector[elemento].cedula + ")' /></td><td><input type='button' value='Eliminar' onclick='eliminar(" + vector[elemento].cedula + ")' /></td><td>"
            }
            document.getElementById("cuerpoTabla").innerHTML += "</tr>"
        }

        // Función para guardar los datos de una persona en el servidor
         function guardar()
        {
            var objetoaenviar = new Object();
            objetoaenviar.cedula = document.getElementById("cedula").value
            objetoaenviar.nombre = document.getElementById("nombre").value
            objetoaenviar.apellidos = document.getElementById("apellidos").value
            objetoaenviar.correo = document.getElementById("correo").value
            objetoaenviar.telefono = document.getElementById("telefono").value        
                    
            try
                {
                    var xhr = new XMLHttpRequest();
                    xhr.open('PUT','/persona');
                    xhr.setRequestHeader('Content-Type','application/json');
                    xhr.onload = function()
                    {
                    if(xhr.status == 200)
                        {
                            console.log(JSON.parse(xhr.responseText));
                            alert('Guardado')
                            rellenaTabla(JSON.parse(xhr.responseText))

                        }
                    else
                        {
                            console.log(xhr);
                        }
                    };
                    xhr.send(JSON.stringify(objetoaenviar));
                    }
            catch(err)
                {
                    console.log(err.message);
                }
        }
        function modificar(cedula)
        {
        if (window.confirm("Desea modificar el dato?")) {
            var objetoEncontrado = listadepersonas.filter(obj => {
                    return obj.cedula === String(cedula)
                    })
            document.getElementById("cedula").value = objetoEncontrado[0].cedula
            document.getElementById("nombre").value = objetoEncontrado[0].nombre
            document.getElementById("apellidos").value = objetoEncontrado[0].apellidos
            document.getElementById("correo").value = objetoEncontrado[0].correo
            document.getElementById("telefono").value = objetoEncontrado[0].telefono    
            document.getElementById('btnaccion').value = 'Modificar'
            document.getElementById('btnaccion').setAttribute( "onClick", "modificaenbd()" );          
        }

      
        }
          function modificaenbd()
        {
         var objetoaenviar = new Object();
            objetoaenviar.cedula = document.getElementById("cedula").value
            objetoaenviar.nombre = document.getElementById("nombre").value
            objetoaenviar.apellidos = document.getElementById("apellidos").value
            objetoaenviar.correo = document.getElementById("correo").value
            objetoaenviar.telefono = document.getElementById("telefono").value        
                               
            try
                {
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST','/persona');
                    xhr.setRequestHeader('Content-Type','application/json');
                    xhr.onload = function()
                    {
                    if(xhr.status == 200)
                        {
                            console.log(JSON.parse(xhr.responseText));
                            alert('Modificado')
                            rellenaTabla(JSON.parse(xhr.responseText))
                            document.getElementById('btnaccion').value = 'Guardar'
                            document.getElementById('btnaccion').setAttribute( "onClick", "guardar()" );          
                            document.getElementById("cedula").value = ""
                            document.getElementById("nombre").value = ""
                            document.getElementById("apellidos").value = ""
                            document.getElementById("correo").value = ""
                            document.getElementById("telefono").value = ""
                        }
                    else
                        {
                            console.log(xhr);
                        }
                    };
                    xhr.send(JSON.stringify(objetoaenviar));
                    }
            catch(err)
                {
                    console.log(err.message);
                }   
                } 
        function eliminar(cedula)
        {
        if (window.confirm("Desea eliminar el dato?")) {
            var objetoaenviar = new Object();
            objetoaenviar.cedula = String(cedula)       
            objetoaenviar.nombre = ""
            objetoaenviar.apellidos = ""
            objetoaenviar.correo = ""
            objetoaenviar.telefono = ""           
            try
                {
                    var xhr = new XMLHttpRequest();
                    xhr.open('DELETE','/persona');
                    xhr.setRequestHeader('Content-Type','application/json');
                    xhr.onload = function()
                    {
                    if(xhr.status == 200)
                        {
                            console.log(JSON.parse(xhr.responseText));
                            alert('Eliminado')
                            rellenaTabla(JSON.parse(xhr.responseText))

                        }
                    else
                        {
                            console.log(xhr);
                        }
                    };
                    xhr.send(JSON.stringify(objetoaenviar));
                    }
            catch(err)
                {
                    console.log(err.message);
                }   
                } 
        }
        cargarDatos()
        </script>
        </body>
        </html>'''
               