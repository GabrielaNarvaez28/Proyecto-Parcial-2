from dominio.pedido import Pedido
from dominio.persona import Persona


class Docente(Persona, Pedido):
    contador_docente = 0
    contador_id = 0

    def __init__(self, titulo_3er_nivel: str = None, titulo_4to_nivel: str = None, cedula: str = None, nombre: str = None,
                 apellido: str = None, email: str = None, telefono: str = None, direccion: str = None,
                  numero_libro: int = 0, activo: bool = True, carrera: str = None, pedir_libro: bool = True,
                  devolver_libro: bool = True, solicitante : str = None, lista_material: str = None,
                 materia: str = None, fecha_prestamo: str = None, fecha_devolucion: str = None):
        Persona.__init__(self, cedula=cedula, nombre=nombre, apellido=apellido, email=email, telefono=telefono,
                         direccion=direccion, numero_libro=numero_libro, activo=activo, carrera=carrera,
                         pedir_libro=pedir_libro, devolver_libro=devolver_libro)
        Pedido.__init__(self, solicitante=solicitante, lista_material=lista_material, materia=materia,
                        fecha_prestamo=fecha_prestamo, fecha_devolucion=fecha_devolucion)
        Docente.contador_docente += 1
        Docente.contador_id += 1
        self._docente = Docente.contador_docente
        self._titulo_3er_nivel = titulo_3er_nivel
        self._titulo_4to_nivel = titulo_4to_nivel
        self._id = Docente.contador_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def titulo_3er_nivel(self):
        return self._titulo_3er_nivel

    @titulo_3er_nivel.setter
    def titulo_3er_nivel(self, titulo_3er_nivel):
        self._titulo_3er_nivel = titulo_3er_nivel

    @property
    def titulo_4to_nivel(self):
        return self._titulo_4to_nivel

    @titulo_4to_nivel.setter
    def titulo_4to_nivel(self, titulo_4to_nivel):
        self._titulo_4to_nivel = titulo_4to_nivel

    @property
    def docente(self):
        return self._docente

    @docente.setter
    def docente(self, docente):
        self._docente = docente

    def solicitar_material(self):
        return f'{self._devolver_libro} {self._pedir_libro}'

    def __str__(self):
        return f'Docente: {self.__dict__.__str__()} , Pedido: {self.__dict__.__str__()}'


if __name__ == '__main__':
    d1 = Docente(cedula='0934569871', nombre='carmen', apellido='ruiz', email='carmenruiz74@gmail.com', telefono=
    '09257893145', direccion='lomas', numero_libro=5, activo=True, carrera='GIG', titulo_3er_nivel='contadora',
                 titulo_4to_nivel='analista', pedir_libro=True, devolver_libro=False)
    print(d1)
    print(f'Se pidio el libro {d1._pedir_libro} devolvieron el libro {d1._devolver_libro} ')

    d2 = Docente(cedula='095789412', nombre='maria', apellido='cercado', email='mariac@gmail.com', telefono=
    '0947942356', direccion='Guayaquil', numero_libro=4, activo=True, carrera='GIG', titulo_3er_nivel='contadora',
    titulo_4to_nivel='analista', pedir_libro=True, devolver_libro=False)
    print(d2)
    print(f'Se pidio el libro {d2._pedir_libro} devolvieron el libro {d2._devolver_libro}')
