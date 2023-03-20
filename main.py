import time

class estudiantes:
    def __init__(self):
        self.estudianteNombre = ""
        self.estudianteApellido = ""
        self.listaEstudiantes = []

    def agregarEstudiantes(self):
        print("Ingresaremos un nuevo estudiante al Colegio")
        print()
        print("Ingrese el nombre del estudiante:")
        self.estudianteNombre = input()
        print("Ingrese el apellido del estudiante:")
        self.estudianteApellido = input()
        print("Se agrego el nombre de", self.estudianteNombre, self.estudianteApellido, "en la lista de estudiantes.")
        self.listaEstudiantes.append(self.estudiante)
        print()

    def expulsarEstudiantes(self):
        print("Expulsaremos un estudiante del Colegio")
        print()
        print("Ingrese el nombre del estudiante:")
        self.estudiante = input()
        print("Se ha expulsado al estudiante", self.estudiante ,"del Colegio Downtown.")
        self.listaEstudiantes.remove(self.estudiante)
        print()

    def consultarEstudiantes(self):
        print(self.listaEstudiantes)
        print()

claseEstudiantes = estudiantes()

print("¡Bienvenido al Colegio Downtown!")
print()
time.sleep(1)

while True:
    print("Ingrese la actividad que le gustaria realizar"
          "\n(Agregar - Expulsar - Consultar)")
    accion = str(input())
    if accion.upper() == "AGREGAR":
        claseEstudiantes.agregarEstudiantes()
    elif accion.upper() == "EXPULSAR":
        claseEstudiantes.expulsarEstudiantes()
    elif accion.upper() == "CONSULTAR":
        claseEstudiantes.consultarEstudiantes()
    else:
        print("Ingrese una actividad valida...")
        print()
        time.sleep(1)

