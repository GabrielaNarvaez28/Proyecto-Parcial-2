# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QWidget)

class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.setEnabled(True)
        vtn_principal.resize(586, 480)
        self.centralwidget = QWidget(vtn_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txt_nombre = QLineEdit(self.centralwidget)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(220, 50, 113, 20))
        self.txt_nombre.setMaxLength(50)
        self.txt_apellido = QLineEdit(self.centralwidget)
        self.txt_apellido.setObjectName(u"txt_apellido")
        self.txt_apellido.setGeometry(QRect(220, 90, 113, 20))
        self.txt_apellido.setMaxLength(50)
        self.lbl_nombre = QLabel(self.centralwidget)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(150, 50, 71, 21))
        self.lbl_apellido = QLabel(self.centralwidget)
        self.lbl_apellido.setObjectName(u"lbl_apellido")
        self.lbl_apellido.setGeometry(QRect(150, 90, 47, 21))
        self.btn_grabar = QPushButton(self.centralwidget)
        self.btn_grabar.setObjectName(u"btn_grabar")
        self.btn_grabar.setGeometry(QRect(194, 390, 141, 41))
        self.cb_tipo_persona = QComboBox(self.centralwidget)
        self.cb_tipo_persona.addItem("")
        self.cb_tipo_persona.addItem("")
        self.cb_tipo_persona.setObjectName(u"cb_tipo_persona")
        self.cb_tipo_persona.setGeometry(QRect(220, 10, 111, 22))
        self.lbl_tipo_persona = QLabel(self.centralwidget)
        self.lbl_tipo_persona.setObjectName(u"lbl_tipo_persona")
        self.lbl_tipo_persona.setGeometry(QRect(150, 10, 71, 21))
        self.lbl_cedula = QLabel(self.centralwidget)
        self.lbl_cedula.setObjectName(u"lbl_cedula")
        self.lbl_cedula.setGeometry(QRect(150, 130, 71, 21))
        self.lbl_email = QLabel(self.centralwidget)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(150, 170, 71, 21))
        self.txt_cedula = QLineEdit(self.centralwidget)
        self.txt_cedula.setObjectName(u"txt_cedula")
        self.txt_cedula.setGeometry(QRect(220, 130, 113, 20))
        self.txt_cedula.setMaxLength(10)
        self.txt_email = QLineEdit(self.centralwidget)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(220, 170, 113, 20))
        self.txt_email.setMaxLength(100)
        self.btn_buscar_cedula = QPushButton(self.centralwidget)
        self.btn_buscar_cedula.setObjectName(u"btn_buscar_cedula")
        self.btn_buscar_cedula.setGeometry(QRect(380, 100, 121, 23))
        self.lbl_estatura = QLabel(self.centralwidget)
        self.lbl_estatura.setObjectName(u"lbl_estatura")
        self.lbl_estatura.setGeometry(QRect(130, 230, 71, 21))
        self.sp_estatura = QSpinBox(self.centralwidget)
        self.sp_estatura.setObjectName(u"sp_estatura")
        self.sp_estatura.setGeometry(QRect(220, 230, 42, 22))
        self.sp_estatura.setMaximum(300)
        self.btn_estatura = QPushButton(self.centralwidget)
        self.btn_estatura.setObjectName(u"btn_estatura")
        self.btn_estatura.setGeometry(QRect(320, 230, 75, 23))
        self.lbl_peso = QLabel(self.centralwidget)
        self.lbl_peso.setObjectName(u"lbl_peso")
        self.lbl_peso.setGeometry(QRect(130, 270, 71, 21))
        self.sp_peso = QSpinBox(self.centralwidget)
        self.sp_peso.setObjectName(u"sp_peso")
        self.sp_peso.setGeometry(QRect(220, 270, 42, 22))
        self.sp_peso.setMaximum(300)
        self.btn_peso = QPushButton(self.centralwidget)
        self.btn_peso.setObjectName(u"btn_peso")
        self.btn_peso.setGeometry(QRect(320, 270, 75, 23))
        self.fecha_nac = QDateEdit(self.centralwidget)
        self.fecha_nac.setObjectName(u"fecha_nac")
        self.fecha_nac.setGeometry(QRect(310, 310, 110, 22))
        self.fecha_nac.setDate(QDate(1900, 1, 1))
        self.lbl_fecha_nac = QLabel(self.centralwidget)
        self.lbl_fecha_nac.setObjectName(u"lbl_fecha_nac")
        self.lbl_fecha_nac.setGeometry(QRect(130, 310, 71, 21))
        self.btn_fnacimiento = QPushButton(self.centralwidget)
        self.btn_fnacimiento.setObjectName(u"btn_fnacimiento")
        self.btn_fnacimiento.setGeometry(QRect(214, 342, 91, 21))
        vtn_principal.setCentralWidget(self.centralwidget)
        self.mnb_menu_principal = QMenuBar(vtn_principal)
        self.mnb_menu_principal.setObjectName(u"mnb_menu_principal")
        self.mnb_menu_principal.setGeometry(QRect(0, 0, 586, 21))
        vtn_principal.setMenuBar(self.mnb_menu_principal)
        self.stb_estado = QStatusBar(vtn_principal)
        self.stb_estado.setObjectName(u"stb_estado")
        vtn_principal.setStatusBar(self.stb_estado)
        QWidget.setTabOrder(self.txt_apellido, self.btn_grabar)
        QWidget.setTabOrder(self.btn_grabar, self.txt_nombre)

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)
    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"Ventana Principal", None))
        self.lbl_nombre.setText(QCoreApplication.translate("vtn_principal", u"Nombre:", None))
        self.lbl_apellido.setText(QCoreApplication.translate("vtn_principal", u"Apellido:", None))
        self.btn_grabar.setText(QCoreApplication.translate("vtn_principal", u"Grabar", None))
        self.cb_tipo_persona.setItemText(0, QCoreApplication.translate("vtn_principal", u"Docente", None))
        self.cb_tipo_persona.setItemText(1, QCoreApplication.translate("vtn_principal", u"Estudiante", None))

        self.lbl_tipo_persona.setText(QCoreApplication.translate("vtn_principal", u"Tipo:", None))
        self.lbl_cedula.setText(QCoreApplication.translate("vtn_principal", u"Cedula:", None))
        self.lbl_email.setText(QCoreApplication.translate("vtn_principal", u"Email:", None))
        self.btn_buscar_cedula.setText(QCoreApplication.translate("vtn_principal", u"Buscar por Cedula", None))
        self.lbl_estatura.setText(QCoreApplication.translate("vtn_principal", u"Estatura: (cm)", None))
        self.btn_estatura.setText(QCoreApplication.translate("vtn_principal", u"E.D.Estatura", None))
        self.lbl_peso.setText(QCoreApplication.translate("vtn_principal", u"Peso: (libras)", None))
        self.btn_peso.setText(QCoreApplication.translate("vtn_principal", u"E.D.Peso", None))
        self.lbl_fecha_nac.setText(QCoreApplication.translate("vtn_principal", u"Fecha_nac", None))
        self.btn_fnacimiento.setText(QCoreApplication.translate("vtn_principal", u"Calcular Edad ", None))
    # retranslateUi

