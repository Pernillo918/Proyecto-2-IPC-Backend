from flask import Flask, jsonify, request


from flask_cors import CORS

#CLASES 
from Cita import Cita
from Medicamento import Medicamento
from Doctor import Doctor
from Enfermera import Enfermera
from Persona import Persona



import json





Personas = []
Enfermeras = []
Doctores = []
Medicamentos = []
Citas =[]

#Citas.append(Cita('01/02/4812','10 am','Dolor de cabeza','Julio','Pendiente','Te chingas'))

#Medicamentos.append(Medicamento('Desemputol','Q.190','Alivia toda clase de enojos por ipc',15))
#Medicamentos.append(Medicamento('ARRIBA','Q.190','IDK',10))

#Doctores.append(Doctor('Linardo','Juarez','02/02/1995','H','lINA12','6321','Cirujano plastico',74125896))

#Enfermeras.append(Enfermera('Diana','Dias','01/07/2001','H','DD','123',50138833))

#Personas.append(Persona('Julio','Pernillo','01/07/2001','H','Pernillo918','50138833',50138833))




app = Flask(__name__)
CORS(app)





#------------------------------------------   METODOS PARA OBTENER DATOS    -------------------------------------------------


# METODO - OBTENER PACIENTES 
@app.route('/Personas', methods=['GET'])
def getPersonas():
    global Personas
    Datos = []
    for persona in Personas:
        objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'Nacimiento': persona.getNacimiento(),
            'Sexo': persona.getSexo(),
            'Username': persona.getUsername(),
            'Contra': persona.getContra(),
            'Telefono': persona.getTelefono()

        }
        Datos.append(objeto)
    return(jsonify(Datos))


# METODO - OBTENER ENFERMERAS
@app.route('/Enfermera', methods=['GET'])
def MostrarEnfermera():
    global Enfermeras
    Datos = []
    for enfermera in Enfermeras:
        objeto = {
            'Nombre': enfermera.getNombre(),
            'Apellido': enfermera.getApellido(),
            'Nacimiento': enfermera.getNacimiento(),
            'Sexo': enfermera.getSexo(),
            'Username': enfermera.getUsername(),
            'Contra': enfermera.getContra(),
            'Telefono': enfermera.getTelefono()

        }
        Datos.append(objeto)
    return(jsonify(Datos))


# METODO - OBTENER DOCTORES
@app.route('/Doctor', methods=['GET'])
def MostrarDoctor():
    global Doctores
    Datos = []
    for doctor in Doctores:
        objeto = {
            'Nombre': doctor.getNombre(),
            'Apellido': doctor.getApellido(),
            'Nacimiento': doctor.getNacimiento(),
            'Sexo': doctor.getSexo(),
            'Username': doctor.getUsername(),
            'Contra': doctor.getContra(),
            'Especialidad': doctor.getEspecialidad(),
            'Telefono': doctor.getTelefono()
        }
        Datos.append(objeto)
    return(jsonify(Datos))


# METODO - OBTENER MEDICAMENTOS 
@app.route('/Medicamentos', methods=['GET'])
def MostrarMedicamentos():
    global Medicamentos
    Datos = []
    for medicamento in Medicamentos:
        objeto = {
            'Nombre': medicamento.getNombre(),
            'Precio': medicamento.getPrecio(),
            'Descripcion': medicamento.getDescripcion(),
            'Cantidad': medicamento.getCantidad()
        }
        Datos.append(objeto)
    return(jsonify(Datos))

# METODO - OBTENER CITAS 
@app.route('/CITAS', methods=['GET'])
def MostrarCitas():
    global Citas
    Datos = []
    for cita in Citas:
        objeto = {
            'fecha': cita.getFecha(),
            'hora': cita.getHora(),
            'motivo': cita.getMotivo(),
            'paciente': cita.getPaciente(),
            'estado': cita.getEstado(),
            'doctor': cita.getDoctor()
        }
        Datos.append(objeto)
    return(jsonify(Datos))



#------------------------------------------------- OBTENER DATO EN ESPECIFICO ------------------------------------


# METODO - OBTENER UN DATO PACIENTES 
@app.route('/Personas/<string:nombre>', methods=['GET'])
def ObtenerPersona(nombre): 
    global Personas
    for persona in Personas:
        if persona.getNombre() == nombre:
            objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'Nacimiento': persona.getNacimiento(),
            'Sexo': persona.getSexo(),
            'Username': persona.getUsername(),
            'Contra': persona.getContra(),
            'Telefono': persona.getTelefono()
            }
            return(jsonify(objeto))       
    salida = { "Mensaje": "Usuario no existente"}
    return(jsonify(salida))


# METODO - OBTENER UN DATO ENFERMERAS 
@app.route('/Enfermeras/<string:nombre>', methods=['GET'])
def ObtenerEnfermera(nombre): 
    global Enfermeras
    for enfermera in Enfermeras:
        if enfermera.getNombre() == nombre:
            objeto = {
            'Nombre': enfermera.getNombre(),
            'Apellido': enfermera.getApellido(),
            'Nacimiento': enfermera.getNacimiento(),
            'Sexo': enfermera.getSexo(),
            'Username': enfermera.getUsername(),
            'Contra': enfermera.getContra(),
            'Telefono': enfermera.getTelefono()
            }
            return(jsonify(objeto))       
    salida = { "Mensaje": "La enfermera no existente"}
    return(jsonify(salida))


# METODO - OBTENER UN DATO DOCTORES 
@app.route('/Doctores/<string:nombre>', methods=['GET'])
def ObtenerDoctores(nombre): 
    global Doctores
    for doctor in Doctores:
        if doctor.getNombre() == nombre:
            objeto = {
            'Nombre': doctor.getNombre(),
            'Apellido': doctor.getApellido(),
            'Nacimiento': doctor.getNacimiento(),
            'Sexo': doctor.getSexo(),
            'Username': doctor.getUsername(),
            'Contra': doctor.getContra(),
            'Especialidad': doctor.getEspecialidad(),
            'Telefono': doctor.getTelefono()
            }
            return(jsonify(objeto))       
    salida = { "Mensaje": "El doctor no existente"}
    return(jsonify(salida))


# METODO - OBTENER UN DATO MEDICAMENTOS 
@app.route('/Medicamentos/<string:nombre>', methods=['GET'])
def ObtenerMedicamento(nombre): 
    global Medicamentos
    for medicamento in Medicamentos:
        if medicamento.getNombre() == nombre:
            objeto = {
            'Nombre': medicamento.getNombre(),
            'Precio': medicamento.getPrecio(),
            'Descripcion': medicamento.getDescripcion(),
            'Cantidad': medicamento.getCantidad()
            }
            return(jsonify(objeto))       
    salida = { "Mensaje": "El medicamento no existente"}
    return(jsonify(salida))

# METODO - OBTENER UN DATO CITA 
@app.route('/CITAS/<string:paciente>', methods=['GET'])
def ObtenerCitas(paciente): 
    global Citas
    for cita in Citas:
        if cita.getPaciente == paciente:
            objeto = {
                    'fecha': cita.getFecha(),
                    'hora': cita.getHora(),
                    'motivo': cita.getMotivo(),
                    'paciente': cita.getPaciente(),
                    'estado': cita.getEstado(),
                    'doctor': cita.getDoctor()
            }
            return(jsonify(objeto))       
    salida = { "Mensaje": "La cita  no existe"}
    return(jsonify(salida))



#----------------------------------------------  METODOS PARA ALMACENAR LOS DATOS-------------------------------------



# METODO - GUARDAR UN DATO PACIENTES 
@app.route('/Personas', methods=['POST'])
def AgregarUsuario():
    global Personas

    nombre = request.json['nombre']
    apellido = request.json['apellido']
    nacimiento = request.json['nacimiento']
    sexo = request.json['sexo']
    username = request.json['username']
    contra = request.json['contra']
    telefono = request.json['telefono']

    nuevo = Persona(nombre,apellido,nacimiento,sexo,username,contra,telefono)
    Personas.append(nuevo)
    return jsonify({'Mensaje':'Paciente agregado correctamente',})


# METODO - GUARDAR UN DATO ENFERMERAS 
@app.route('/Enfermeras', methods=['POST'])
def AgregarEnfermeras():
    global Enfermeras

    nombre = request.json['nombre']
    apellido = request.json['apellido']
    nacimiento = request.json['nacimiento']
    sexo = request.json['sexo']
    username = request.json['username']
    contra = request.json['contra']
    telefono = request.json['telefono']

    nuevo = Enfermera(nombre,apellido,nacimiento,sexo,username,contra,telefono)
    Enfermeras.append(nuevo)
    return jsonify({'Mensaje':'Enfermera agregada con exito ',})


# METODO - GUARDAR UN DATO DOCTORES 
@app.route('/Doctores', methods=['POST'])
def AgregarDoctores():
    global Doctores

    nombre = request.json['nombre']
    apellido = request.json['apellido']
    nacimiento = request.json['nacimiento']
    sexo = request.json['sexo']
    username = request.json['username']
    contra = request.json['contra']
    especialidad = request.json['especialidad']
    telefono = request.json['telefono']

    nuevo = Doctor(nombre,apellido,nacimiento,sexo,username,contra,especialidad,telefono)
    Doctores.append(nuevo)
    return jsonify({'Mensaje':'Doctores agregados con exito ',})


# METODO - GUARDAR UN DATO MEDICAMENTOS 
@app.route('/Medicamentos', methods=['POST'])
def AgregarMedicamentos():
    global Medicamentos

    nombre = request.json['nombre']
    precio = request.json['precio']
    descripcion = request.json['descripcion']
    cantidad = request.json['cantidad']

    nuevo = Medicamento(nombre,precio,descripcion,cantidad)
    Medicamentos.append(nuevo)
    return jsonify({'Mensaje':'Medicamentos agregados con exito ',})

# METODO - GUARDAR UN DATO CITAS 
@app.route('/CITAS', methods=['POST'])
def AgregarCitas():
    global Citas


    fecha = request.json['fecha']
    hora = request.json['hora']
    motivo = request.json['motivo']
    paciente = request.json['paciente']
    estado = request.json['estado']
    doctor = request.json['doctor']

    nuevo = Cita(fecha,hora,motivo,paciente,estado,doctor)
    Citas.append(nuevo)
    return jsonify({'Mensaje':'Cita agregada con exito ',})




#-------------------------------------- METODOS PARA ACTUALIZAR LOS DATOS 

#METODO - ACTUALIZAR DATO PACIENTE
@app.route('/Personas/<string:nombre>', methods=['PUT'])
def ActualizarPersona(nombre):
    global Personas
    for i in range(len(Personas)):

        if nombre == Personas[i].getNombre():

            Personas[i].setNombre(request.json['nombre'])
            Personas[i].setApellido(request.json['apellido'])
            Personas[i].setNacimiento(request.json['nacimiento'])
            Personas[i].setSexo(request.json['sexo'])
            Personas[i].setUsername(request.json['username'])
            Personas[i].setContra(request.json['contra'])
            Personas[i].setTelefono(request.json['telefono'])

            return jsonify({'Mensaje':'La actualizacion se completo con exito'})
    return jsonify({'Mensaje':'El dato no se encontro para actualizar'})


#METODO - ACTUALIZAR DATO ENFERMERAS
@app.route('/Enfermeras/<string:nombre>', methods=['PUT'])
def ActualizarEnfermera(nombre):
    global Enfermeras
    for i in range(len(Enfermeras)):

        if nombre == Enfermeras[i].getNombre():

            Enfermeras[i].setNombre(request.json['nombre'])
            Enfermeras[i].setApellido(request.json['apellido'])
            Enfermeras[i].setNacimiento(request.json['nacimiento'])
            Enfermeras[i].setSexo(request.json['sexo'])
            Enfermeras[i].setUsername(request.json['username'])
            Enfermeras[i].setContra(request.json['contra'])
            Enfermeras[i].setTelefono(request.json['telefono'])

            return jsonify({'Mensaje':'Datos actualizados correctamente'})
    return jsonify({'Mensaje':'No ha sido posible  actualizar'})


#METODO - ACTUALIZAR DATO DOCTORES
@app.route('/Doctores/<string:nombre>', methods=['PUT'])
def ActualizarDoctores(nombre):
    global Doctores
    for i in range(len(Doctores)):

        if nombre == Doctores[i].getNombre():

            Doctores[i].setNombre(request.json['nombre'])
            Doctores[i].setApellido(request.json['apellido'])
            Doctores[i].setNacimiento(request.json['nacimiento'])
            Doctores[i].setSexo(request.json['sexo'])
            Doctores[i].setUsername(request.json['username'])
            Doctores[i].setContra(request.json['contra'])
            Doctores[i].setEspecialidad(request.json['especialidad'])
            Doctores[i].setTelefono(request.json['telefono'])

            return jsonify({'Mensaje':'La actualizacion se completo con exito'})
    return jsonify({'Mensaje':'El dato no se encontro para actualizar'})


#METODO - ACTUALIZAR DATO MEDICAMENTO 
@app.route('/Medicamentos/<string:nombre>', methods=['PUT'])
def ActualizarMedicamentos(nombre):
    global Medicamentos
    for i in range(len(Medicamentos)):

        if nombre == Medicamentos[i].getNombre():

            Medicamentos[i].setNombre(request.json['nombre'])
            Medicamentos[i].setPrecio(request.json['precio'])
            Medicamentos[i].setDescripcion(request.json['descripcion'])
            Medicamentos[i].setCantidad(request.json['cantidad'])
           

            return jsonify({'Mensaje':'La actualizacion se completo con exito'})
    return jsonify({'Mensaje':'El dato no se encontro para actualizar'})


#METODO - ACTUALIZAR DATO CITAS 
@app.route('/Citas/<string:nombre>', methods=['PUT'])
def ActualizarCitas(nombre):
    global Citas
    for i in range(len(Citas)):

        if nombre == Citas[i].getPaciente():

            
            Citas[i].setEstado(request.json['estado'])
            Citas[i].setDoctor(request.json['doctor'])

            return jsonify({'Mensaje':'La actualizacion se completo con exito'})
    return jsonify({'Mensaje':'El dato no se encontro para actualizar'})




#--------------------------------------------    METODOS PARA ELIMINAR DATOS ----------------------------------------


# METODO - ELIMINAR UN DATO PACIENTES 
@app.route('/Personas/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    global Personas
    for i in range(len(Personas)):
        if nombre == Personas[i].getNombre():
            del Personas[i]
            return jsonify({'Mensaje':'Usuario eliminado correctamente'})       
    return jsonify({'Mensaje':'Usuario no encontrado para eliminar'})
    

# METODO - ELIMINAR UN DATO ENFERMERAS 
@app.route('/Enfermeras/<string:nombre>', methods=['DELETE'])
def EliminarEnfermera(nombre):
    global Enfermeras
    for i in range(len(Enfermeras)):
        if nombre == Enfermeras[i].getNombre():
            del Enfermeras[i]
            return jsonify({'Mensaje':'Enfermera eliminada correctamente'})       
    return jsonify({'Mensaje':'Enfermera no encontrada para eliminar'})


# METODO - ELIMINAR UN DATO DOCTORES 
@app.route('/Doctores/<string:nombre>', methods=['DELETE'])
def EliminarDoctor(nombre):
    global Doctores
    for i in range(len(Doctores)):
        if nombre == Doctores[i].getNombre():
            del Doctores[i]
            return jsonify({'Mensaje':'Doctor eliminado correctamente'})       
    return jsonify({'Mensaje':'Doctor no encontrado para eliminar'})


# METODO - ELIMINAR UN DATO MEDICAMENTO 
@app.route('/Medicamentos/<string:nombre>', methods=['DELETE'])
def EliminarMedicamento(nombre):
    global Medicamentos
    for i in range(len(Medicamentos)):
        if nombre == Medicamentos[i].getNombre():
            del Medicamentos[i]
            return jsonify({'Mensaje':'Medicamento eliminado correctamente'})       
    return jsonify({'Mensaje':'Medicamento no encontrado para eliminar'})

# METODO - ELIMINAR UN DATO CITA 
@app.route('/CITAS/<string:nombre>', methods=['DELETE'])
def EliminarCITAS(nombre):
    global Citas
    for i in range(len(Citas)):
        if nombre == Citas[i].getPaciente():
            del Citas[i]
            return jsonify({'Mensaje':'Cita eliminadA correctamente'})       
    return jsonify({'Mensaje':'Cita no encontrado para eliminar'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)