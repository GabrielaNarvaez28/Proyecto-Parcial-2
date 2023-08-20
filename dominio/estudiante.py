from dominio.persona import Persona
from datetime import datetime


class Estudiante(Persona):
    contador_estudiante = 0
    contador_id = 0

    def __init__(self, nivel: int = 1, cedula: str = None, nombre: str = None, apellido: str = None,
                  email: str = None, telefono: str = None, direccion: str = None, numero_libro: int = 0,
                 activo: bool = True, carrera: str = None, pedir_libro: bool = True,devolver_libro: bool = True,
                 estatura = int , peso = float, fnacimiento = datetime ):
        Persona.__init__(self,cedula=cedula,nombre=nombre, apellido=apellido,
                  email=email, telefono=telefono, direccion=direccion, numero_libro=numero_libro, activo=activo,
                         carrera=carrera, pedir_libro=pedir_libro,devolver_libro=devolver_libro,estatura = estatura,
                         peso = peso,fnacimiento = fnacimiento)

        Estudiante.contador_estudiante += 1
        Estudiante.contador_id += 1
        self._nivel = nivel
        self._id = Estudiante.contador_id
        self._estudiante = Estudiante.contador_estudiante

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @property
    def estudiante(self):
        return self._estudiante

    @estudiante.setter
    def estudiante(self, estudiante):
        self._estudiante = estudiante


    def solicitar_material(self):
        return f'{self._devolver_libro} {self._pedir_libro}'

    def __str__(self):
        return f'Estudiante: {self.__dict__.__str__()}, Pedido: {self.__dict__.__str__()}'


if __name__ == '__main__':
    e1 = Estudiante(cedula='0956341366', nombre='wendy', apellido='caicedo', email='wendycaicedo74@gmail.com',
                    telefono='0968662960', direccion='nobol', numero_libro=5, activo=True, carrera='GIG', nivel=2,
                    pedir_libro=True, devolver_libro=False)

    print(e1)
    print(f'Se pidio el libro {e1._pedir_libro} devolvieron el libro {e1._devolver_libro}')
    e2 = Estudiante(cedula='098754679', nombre='tatiana', apellido='caicedo', email='tatianac@gmail.com',
                    telefono='0968547896', direccion='gyq', numero_libro=3, activo=True, carrera='GIG', nivel=3,
                    pedir_libro=True, devolver_libro=False,estatura= 175, peso= 140, fnacimiento = '03/01/2000')
    print(e2)
    print(f'Se pidio el libro {e2._pedir_libro} devolvieron el libro {e2._devolver_libro}')
    e1.pedir('Revista', 'Programacion')