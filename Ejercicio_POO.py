class Estudiante ():
    def __init__(self,nombre,edad,direccion,telefono,programa,semestre):
        self.Nombre=nombre
        self.Edad=edad
        self.Direccion=direccion
        self.Telefono=telefono
        self.Programa=programa
        self.Semestre=semestre

    def Visualizar(self):
        print("Nombre: ",self.Nombre," Edad: ",self.Edad," Dirección: ",self.Direccion," Teléfono: ",self.Telefono," Programa: ",self.Programa," Semestre: ",self.Semestre)
    

class Asignatura (Estudiante):
    def __init__(self, nombre_asignatura, semestre_asignatura, lista_estudiante, nombre, edad, direccion, telefono, programa, semestre):
        super().__init__(nombre, edad, direccion, telefono, programa, semestre)
        self.Nombre_Asignatura=nombre_asignatura
        self.Semestre_Asignatura=semestre_asignatura
        self.Lista_Estudiante=lista_estudiante

    def Agregar(self):
        print("Agregar estudiante")

    def Visualizar(self):
        super().Visualizar()
        print("Nombre Asignatura: ",self.Nombre_Asignatura," Semestre Asignatura: ",self.Semestre_Asignatura," Lista Estudiante: ",self.Lista_Estudiante)


Estudiante1=Asignatura("Electiva 2",8,21,"x",24,"x",123,"Sistemas",8)
Estudiante1.Visualizar()