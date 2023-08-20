from dominio.material import Material
from dominio.pedido import Pedido


class Revista(Material, Pedido):
    contador_revista = 0
    contador_id = 0

    def __init__(self, tipo: str = None,codigo: str = None, autor: str = None, titulo: str = None, anio: int = None,
                    editorial: str = None, disponible: bool = None, cantidad_disponible: int = None,
                    actualizar_disponibilidad: bool = None, solicitante: str = None, lista_material: str = None,
                 materia: str = None, fecha_prestamo: str = None, fecha_devolucion: str = None):
        Material.__init__(self, codigo=codigo, autor=autor, titulo=titulo, anio=anio,
                         editorial=editorial, disponible=disponible, cantidad_disponible=cantidad_disponible,
                         actualizar_disponibilidad=actualizar_disponibilidad)
        Pedido.__init__(self, solicitante=solicitante, lista_material=lista_material, materia=materia,
                        fecha_prestamo=fecha_prestamo, fecha_devolucion=fecha_devolucion)
        Revista.contador_id += 1
        Revista.contador_revista += 1
        self._revista = Revista.contador_revista
        self._id = Revista.contador_id
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def revista(self):
        return self.revista

    @revista.setter
    def revista(self, revista):
        self._revista = revista

    # @abstractmethod
    def __str__(self):
        return f'Revista: {self.__dict__.__str__()}, Pedido : {self.__dict__.__str__()}'

    '''
    Display name
    '''

    # @abstractmethod
    def ver_disponibilidad(self):
        return f'{self._disponible} {self._cantidad_disponible}'


if __name__ == '__main__':
    # pass
    R1 = Revista(codigo='12', autor='Maria de la cuadra', titulo='Secreto de la belleza', anio=2023,
                 editorial='Imprenta nueva luz', disponible=True, cantidad_disponible=20,
                 actualizar_disponibilidad=True, tipo='couche', solicitante='docente', lista_material='libro',
                 materia='Literatura', fecha_prestamo='20/02/2023', fecha_devolucion='05/03/2023')
    print(R1)
    Revista1 =Revista()
    print(Revista1)
    print(f'Esta disponible el Material  {R1._disponible} y la cantidad disponible es {R1._cantidad_disponible}')
    # , debito=300.00)
    # print(obj)