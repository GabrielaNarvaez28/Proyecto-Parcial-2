from abc import ABC, abstractmethod


class Material(ABC):

    def __init__(self, codigo: str = None, autor: str = None, titulo: str = None, anio: int = None,
                 editorial: str = None, disponible: bool = None, cantidad_disponible: int = None,
                 actualizar_disponibilidad: bool = None):
        self._codigo = codigo
        self._autor = autor
        self._titulo = titulo
        self._anio = anio
        self._editorial = editorial
        self._disponible = disponible
        self._cantidad_disponible = cantidad_disponible
        self._actualizar_disponibilidad = actualizar_disponibilidad

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def anio(self):
        return self.anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, editorial):
        self._editorial = editorial

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, disponible):
        self._disponible = disponible

    @property
    def cantidad_disponible(self):
        return self._cantidad_disponible

    @cantidad_disponible.setter
    def cantidad_disponible(self, cantidad_disponible):
        self._cantidad_disponible = cantidad_disponible

    @property
    def actualizar_disponibilidad (self):
        return self._actualizar_disponibilidad

    @actualizar_disponibilidad.setter
    def actualizar_disponibilidad(self, actualizar_disponibilidad):
        self._actualizar_disponibilidad = actualizar_disponibilidad

    def __str__(self):
        return f'Material: {self.__dict__.__str__()}'

    @abstractmethod
    def ver_disponibilidad(self):
        return f'{self._disponible} {self._cantidad_disponible}'


if __name__ == '__main__':
    pass
    #m1= Material(codigo='0123',autor='Miguel de Cervantes',titulo='Don Quijote de la Mancha',anio=1613
                 #,editorial ='Juan de la Cuesta' ,disponible=True ,cantidad_disponible=10
                 #,actualizar_disponibilidad=True)
    #print(m1)
    #print(f'Esta disponible el Material  {m1._disponible} y la cantidad disponible es {m1._cantidad_disponible}')



