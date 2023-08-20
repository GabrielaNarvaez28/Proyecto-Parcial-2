

from PySide6 import QtGui

from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMessageBox, QMainWindow

from UI.vtn_principal import Ui_vtn_principal
from datos.estudiante_dao import EstudianteDao
from dominio.docente import Docente
from dominio.estudiante import Estudiante
from statistics import mean,median,mode
from datetime import date


class PersonaPrincipal(QMainWindow):
    def __init__(self):
        super(PersonaPrincipal, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.stb_estado.showMessage('Bienvenido', 2000)
        self.ui.btn_grabar.clicked.connect(self.grabar)
        self.ui.btn_buscar_cedula.clicked.connect(self.buscar_x_cedula)
        self.ui.btn_estatura.clicked.connect(self.calculos_estatura)
        self.ui.btn_peso.clicked.connect(self.calculos_peso)
        self.ui.btn_fnacimiento.clicked.connect(self.calculos_edad)
        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())

        correo_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[(A-Z|a-z]{2,7}\b'
        validator = QRegularExpressionValidator(correo_exp, self)
        self.ui.txt_email.setValidator(validator)

    def grabar(self):
        tipo_persona = self.ui.cb_tipo_persona.currentText()
        if self.ui.txt_nombre.text() == '' or self.ui.txt_apellido.text() == '' \
                or len(self.ui.txt_cedula.text()) < 10 or self.ui.txt_email.text() == '':
            print("Completar datos")
            QMessageBox.warning(self, 'Advertencia', 'Falta de llenar los datos obligatorios')
        else:
            persona = None
            if tipo_persona == 'Docente':
                persona = Docente()
                persona.nombre = self.ui.txt_nombre.text()
                persona.apellido = self.ui.txt_apellido.text()
                persona.cedula = self.ui.txt_cedula.text()
                persona.email = self.ui.txt_email.text()
                persona.estatura = self.ui.sp_estatura.text()
                persona.peso = self.ui.sp_peso.text()
                persona.fnacimiento = self.ui.fecha_nac.Text()
                # persona.carrera = self.ui.txt_carrera.text()
            else:
                persona = Estudiante()
                persona.nombre = self.ui.txt_nombre.text()
                persona.apellido = self.ui.txt_apellido.text()
                persona.cedula = self.ui.txt_cedula.text()
                persona.email = self.ui.txt_email.text()
                persona.estatura = self.ui.sp_estatura.text()
                persona.peso = self.ui.sp_peso.text()
                persona.fnacimiento = self.ui.fecha_nac.text()
                # persona.carrera = self.ui.txt_carrera.text()
                # insertar en la base de datos al estudiante
                respuesta = None
                respuesta = EstudianteDao.insertar_estudiante(persona)


            # archivo = None
            # try:
            # archivo = open('archivo.txt', mode='a')
            # archivo.write(persona.__str__())
            # archivo.write('\n')
            # except Exception as e:
            # print('No se pudo grabar.')
            # finally:
            # if archivo:
            # archivo.close()
            if respuesta['exito']:
                self.ui.txt_nombre.setText('')
                self.ui.txt_apellido.setText('')
                self.ui.txt_cedula.setText('')
                self.ui.txt_email.setText('')
                self.ui.sp_estatura.setValue(0)
                self.ui.sp_peso.setValue(0)
                #self.ui.fecha_nac.setDate()
                self.ui.stb_estado.showMessage('Grabado con éxito.', 2000)
            else:
                QMessageBox.critical(self, 'Error', respuesta['mensaje'])



    def buscar_x_cedula(self):
        cedula = self.ui.txt_cedula.text()
        e = Estudiante(cedula=cedula)
        e = EstudianteDao.seleccionar_por_cedula(e)
        self.ui.txt_nombre.setText(e.nombre)
        self.ui.txt_apellido.setText(e.apellido)
        self.ui.txt_email.setText(e.email)
        self.ui.cb_tipo_persona.setCurrentText('Estudiante')


    def calculos_estatura(self):
        global estudiante
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        suma_estaturas = 0
        estaturas= list()
        for estudiante in estudiantes:
            suma_estaturas += estudiante.estatura
            estaturas.append(estudiante.estatura)
        promedio_estatura = suma_estaturas/cantidad_estudiantes
        media_estatura = suma_estaturas/cantidad_estudiantes
        moda_estatura = mode(estaturas)
        minimo_estatura = min(estaturas)
        maximo_estatura = max(estaturas)
        print(f'El promedio de estaturas es: {promedio_estatura}')
        print(f'La media de estaturas es: {media_estatura}')
        print(f'La moda de estaturas es: {moda_estatura}')
        print(f'El valor minimo de estaturas es: {minimo_estatura}')
        print(f'El valor maximo de estaturas es: {maximo_estatura}')


    def calculos_peso(self):
        global estudiante
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        suma_peso = 0
        peso = list()
        for estudiante in estudiantes:
            suma_peso += estudiante.peso
            peso.append(estudiante.peso)
        promedio_peso = suma_peso / cantidad_estudiantes
        media_peso = suma_peso / cantidad_estudiantes
        moda_peso = mode(peso)
        minimo_peso = min(peso)
        maximo_peso = max(peso)
        print(f'El promedio de peso es: {promedio_peso}')
        print(f'La media de peso es: {media_peso}')
        print(f'La moda de peso es: {moda_peso}')
        print(f'El valor minimo de peso es: {minimo_peso}')
        print(f'El valor maximo de peso es: {maximo_peso}')



    def calculos_edad(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        fnacimiento = [estudiante.fnacimiento for estudiante in estudiantes]
        fecha_actual = date.today()

        edades = []
        for fecha in fnacimiento:
            edad = fecha_actual.year - fecha.year - ((fecha_actual.month, fecha_actual.day) < (fecha.month, fecha.day))
            edades.append(edad)

        # Calculando el promedio de edad
        promedio_edad = sum(edades) / len(edades)

        # Ordenando las edades y calculando la mediana
        edades_sorted = sorted(edades)
        n = len(edades_sorted)
        if n % 2 == 0:  # Cantidad par de edades
            mediana_edad = (edades_sorted[n // 2 - 1] + edades_sorted[n // 2]) / 2
        else:  # Cantidad impar de edades
            mediana_edad = edades_sorted[n // 2]

        # Calculando la moda
        edad_counts = {edad: edades.count(edad) for edad in edades}
        max_count = max(edad_counts.values())
        moda_edad = [edad for edad, count in edad_counts.items() if count == max_count]

        # Calculando la edad máxima y mínima
        max_edad = max(edades)
        min_edad = min(edades)

        # for estudiante, edad in zip(estudiantes, edades):
        # print(f'Estudiante: {estudiante.nombre}, Edad: {edad} años')

        print(f'El promedio de edades es: {promedio_edad:.2f} años')
        print(f'La mediana de edades es: {mediana_edad} años')
        print(f'La moda de edades es: {moda_edad}')
        print(f'La edad máxima es: {max_edad} años')
        print(f'La edad mínima es: {min_edad} años')

        #Castañeda Arteaga María José
        #Orrala Macias Tommy
        #Narváez Briones Gabriela
        #Macias Díaz Luis angel
        #Anchundia Ascencio Alex















