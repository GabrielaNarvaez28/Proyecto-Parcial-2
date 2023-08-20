from pyodbc import IntegrityError, ProgrammingError

from datos.conexion import Conexion
from dominio.estudiante import Estudiante


class EstudianteDao:
    _INSERTAR = "INSERT INTO Estudiantes (cedula,nombre,apellido,email,carrera,activo, estatura,peso,fnacimiento) VALUES (?,?,?,?,?,?,?,?,?)"
    _SELECCIONAR_X_CEDULA = "select id,cedula,nombre,apellido, email,carrera,activo,estatura,peso,fnacimiento from Estudiantes " \
                             " where cedula = ? "
    _SELECCIONAR = "select id,cedula, nombre, apellido, email,carrera,activo,estatura,peso,fnacimiento from Estudiantes where activo = 1"
    @classmethod
    def insertar_estudiante(cls, estudiante):
        #cursor = Conexion.obtenerCursor()
        respuesta = {'exito': False, 'mensaje': ''}
        flag_exito = False
        mensaje = ''
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula, estudiante.nombre, estudiante.apellido,estudiante.email,estudiante.carrera,
                         estudiante.activo, estudiante.estatura, estudiante.peso,estudiante.fnacimiento)
                cursor.execute(cls._INSERTAR, datos)
                flag_exito = True
                mensaje = 'Ingreso exitoso'
        except IntegrityError as e:
            flag_exito = False
            #print('La cedula que intenta ingresar ya existe')
            if e.__str__().find('Cedula') > 0:
                print('Cedula ya ingresada')
                mensaje = 'Cedula ya ingresada'
            elif e.__str__().find('Email') > 0:
                print('Email ya ingresado')
                mensaje = 'Email ya ingresado'
            else:
                print('Error de Integridad')
                mensaje = 'Error de Integridad'
        except ProgrammingError as e:
            flag_exito = False
            print('Los datos ingresados no son del tamaño permitido')
            mensaje = 'Los datos ingresados no son del tamaño permitido'
        except Exception as e:
            flag_exito = False
            print(e)
        finally:
            respuesta['exito'] = flag_exito
            respuesta['mensaje'] = mensaje
            return respuesta


    @classmethod
    def seleccionar_por_cedula(cls, estudiante):
        persona_encontrada = None
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula,)
                resultado = cursor.execute(cls._SELECCIONAR_X_CEDULA, datos)
                persona_encontrada = resultado.fetchone()
                estudiante.email = persona_encontrada[4]
                estudiante.nombre = persona_encontrada[2]
                estudiante.apellido = persona_encontrada[3]
                estudiante.carrera = persona_encontrada[5]
                estudiante.activo = persona_encontrada[6]
                estudiante.cedula = persona_encontrada[1]
                estudiante.id = persona_encontrada[0]
        except Exception as e:
            print(e)
        finally:
            return estudiante


    @classmethod
    def seleccionar_estudiantes(cls):
        lista_estudiantes = list()
        try:
            with Conexion.obtenerCursor() as cursor:
                resultado = cursor.execute(cls._SELECCIONAR)
                for tupla_estudiante in resultado.fetchall():
                    estudiante = Estudiante()
                    estudiante.id = tupla_estudiante [0]
                    estudiante.cedula = tupla_estudiante[1]
                    estudiante.nombre = tupla_estudiante[2]
                    estudiante.apellido = tupla_estudiante[3]
                    estudiante.email = tupla_estudiante[4]
                    estudiante.carrera = tupla_estudiante[5]
                    estudiante.activo = tupla_estudiante[6]
                    estudiante.estatura = tupla_estudiante[7]
                    estudiante.peso = tupla_estudiante[8]
                    estudiante.fnacimiento = tupla_estudiante[9]
                    lista_estudiantes.append(estudiante)

        except Exception as e:
            lista_estudiantes = None
        finally:
            return lista_estudiantes



if __name__ == '__main__':
    #e1 = Estudiante()
    #e1.cedula = '9876543211'
    #e1.nombre = 'Juan'
    #e1.apellido = 'Cruz'
    #e1.email = 'jcruz@mail.com'
    #e1.carrera = 'ADM'
    #e1.activo = True
    #EstudianteDao.insertar_estudiante(e1)
    #persona_encontrada = EstudianteDao.seleccionar_por_cedula(e1)
    #print(persona_encontrada)
    EstudianteDao.seleccionar_estudiantes()
    for estudiante in estudiantes:
        print(estudiante)


