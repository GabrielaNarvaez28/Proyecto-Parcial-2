from datetime import datetime
from abc import ABC, abstractmethod



class Persona(ABC):

    def __init__(self, cedula: str = None, nombre: str = None, apellido : str= None, email: str = None, estatura = int,
                 telefono: str = None, direccion: str = None, numero_libro: int = None, activo: bool = None,
                 carrera: str = None,pedir_libro: bool = None, devolver_libro: bool = None, peso= float,
                 fnacimiento= datetime):

        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._estatura = estatura
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libro = numero_libro
        self._activo = activo
        self._carrera = carrera
        self._pedir_libro = pedir_libro
        self._devolver_libro = devolver_libro
        self._peso = peso
        self.fnacimiento = fnacimiento
      

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido= apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def numero_libro(self):
        return self._numero_libro

    @numero_libro.setter
    def numero_libro(self, numero_libro):
        self._numero_libro = numero_libro

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, activo):
        self._activo = activo

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, carrera):
        self._carrera = carrera

    @property
    def pedir_libro(self):
        return self._pedir_libro

    @pedir_libro.setter
    def pedir_libro(self, pedir_libro):
        self._pedir_libro = pedir_libro

    @property
    def devolver_libro(self):
        return self._devolver_libro

    @devolver_libro.setter
    def devolver_libro(self, devolver_libro):
        self._devolver_libro = devolver_libro

    @property
    def estatura(self):
        return self._estatura

    @estatura.setter
    def estatura(self, estatura):
        self._estatura = estatura

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    @property
    def fnacimiento(self):
        return self._fnacimiento

    @fnacimiento.setter
    def fnacimiento(self, fnacimiento):
        self._fnacimiento = fnacimiento

    @abstractmethod
    def solicitar_material(self):
        return f'{self._devolver_libro} {self._pedir_libro}'

    def pedir(self,lista_material , materia):
        print(f'Se pide el material a: {self._cedula}\n'
              f'lista_material:{lista_material}\n'
              f'materia:{materia}')




    def __str__(self):
        return f'Persona: {self.__dict__.__str__()}'


if __name__ == '__main__':
     pass
     #p1= Persona(cedula='0957254097',nombre='Allan',apellido='Baque',email='baque@gmail.com',telefono ='09864747383' ,direccion='suburbio' ,numero_libro=5, activo=True ,carrera= 'Marketing',pedir_libro=True,devolver_libro=False)
     #print(p1)
     #print(f'Se pidio el libro {p1.pedir_libro} devolvieron el libro {p1.devolver_libro} ')
     # print(obj)