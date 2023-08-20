from dominio.material import Material



class Libro(Material):
    contador_libro = 0
    contador_id = 0

    def __init__(self, tipo_pasta: str = None, codigo: str = None, autor: str = None, titulo: str = None, anio: int =
                  None, editorial: str = None, disponible: bool = None, cantidad_disponible: int = None,
                 actualizar_disponibilidad: bool = None, solicitante: str = None, lista_material: str = None,
                 materia: str = None, fecha_prestamo: str = None, fecha_devolucion: str = None):
        Material.__init__(self, codigo=codigo, autor=autor, titulo=titulo, anio=anio,
                         editorial=editorial, disponible=disponible, cantidad_disponible=cantidad_disponible,
                         actualizar_disponibilidad=actualizar_disponibilidad)

        Libro.contador_id += 1
        Libro.contador_libro += 1
        self._libro = Libro.contador_libro
        self._id = Libro.contador_id
        self._tipo_pasta = tipo_pasta

    @property
    def tipo_pasta(self):
        return self._tipo_pasta

    @tipo_pasta.setter
    def tipo_pasta(self, tipo_pasta):
        self._tipo_pasta = tipo_pasta

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def libro(self):
        return self._libro

    @libro.setter
    def libro(self, libro):
        self._libro = libro

    def __str__(self):
        return f'Libro: {self.__dict__.__str__()} , Pedido: {self.__dict__.__str__()}'

    def ver_disponibilidad(self):
        return f'{self._disponible} {self._cantidad_disponible}'


if __name__ == '__main__':
    # pass
    l1 = Libro(codigo='0123', autor='Miguel de Cervantes', titulo='Don Quijote de la Mancha', anio=1613,
                  editorial='Juan de la Cuesta', disponible=True, cantidad_disponible=10,
                actualizar_disponibilidad=True, tipo_pasta='encuadernado', solicitante='estudiante',
               lista_material='libro', materia='estadistica', fecha_prestamo='05/02/2023', fecha_devolucion=
               '20/02/2023')
    print(l1)
    libro1 = Libro()
    print(libro1)
    print(f'Esta disponible el Material  {l1._disponible} y la cantidad disponible es {l1._cantidad_disponible}')
    # , debito=200.00)
    # print(obj)

