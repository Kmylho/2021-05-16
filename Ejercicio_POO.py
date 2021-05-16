class Estudiante ():
    def __init__(self,nombre,edad,direccion,telefono,programa,semestre):
        self.Nombre=nombre
        self.Edad=edad
        self.Direccion=direccion
        self.Telefono=telefono
        self.Programa=programa
        self.Semestre=semestre

    def VisualizarEstudiante(self):
        print("Nombre: ",self.Nombre," Edad: ",self.Edad," Dirección: ",self.Direccion," Teléfono: ",self.Telefono," Programa: ",self.Programa," Semestre: ",self.Semestre)
    

class Asignatura (Estudiante):
    def __init__(self, nombre_asignatura, semestre_asignatura, lista_estudiante):
        self.Nombre_Asignatura=nombre_asignatura
        self.Semestre_Asignatura=semestre_asignatura
        self.Lista_Estudiante=lista_estudiante

    def Agregar(self, nombre, edad, direccion, telefono, programa, semestre):
        super().__init__(nombre,edad,direccion,telefono,programa,semestre)
        print("Estudiante: ",self.Nombre," agregado a: ",self.Nombre_Asignatura)

    def Visualizar(self):
        print("Nombre Asignatura: ",self.Nombre_Asignatura," Semestre Asignatura: ",self.Semestre_Asignatura," Lista Estudiante: ",self.Lista_Estudiante)
        
    def Visualizar_Todo(self):
        super().VisualizarEstudiante()
        print("Nombre Asignatura: ",self.Nombre_Asignatura," Semestre Asignatura: ",self.Semestre_Asignatura," Lista Estudiante: ",self.Lista_Estudiante)


Asignatura1=Asignatura("Multimedia",8,21)
Asignatura1.Visualizar()

Asignatura2=Asignatura("electiva 2",8,21)
Asignatura2.Visualizar()

Estudiante1=Estudiante("Andres",21,"suba",132,"Sistemas",8)
Estudiante1.VisualizarEstudiante()

Asignatura2.Agregar("Camilo",21,"suba",123,"Sistemas",8)
Asignatura2.Visualizar_Todo()
