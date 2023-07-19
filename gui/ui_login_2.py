# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_medicine_login(object):
    def setupUi(self, medicine_login):
        if not medicine_login.objectName():
            medicine_login.setObjectName(u"medicine_login")
        medicine_login.resize(687, 415)
        medicine_login.setStyleSheet(u"#login_user:hover , #login_pwd:hover ,  #btn_login:hover , #btn_cancel:hover , #btn_register:hover{\n"
"border:2px solid black;\n"
"background-color:white;\n"
"}\n"
"#login_user , #login_pwd , #btn_login , #btn_cancel , #btn_register{\n"
"background-color:#cccccc;\n"
"border-bottom-right-radius:20px;\n"
"border:2px solid #cccccc;\n"
"padding:4px 4px;\n"
"}\n"
"#login_user_title , #login_pwd_title{\n"
"background-color:#cccccc;\n"
"border-bottom-right-radius:20px;\n"
"padding:4px 4px;\n"
"}\n"
"#login_bg{\n"
"background-color:white;\n"
"border-radius:20px;\n"
"}")
        medicine_login.setFrameShape(QFrame.StyledPanel)
        medicine_login.setFrameShadow(QFrame.Raised)
        self.login_bg = QLabel(medicine_login)
        self.login_bg.setObjectName(u"login_bg")
        self.login_bg.setGeometry(QRect(30, 20, 631, 371))
        self.label = QLabel(medicine_login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 40, 221, 51))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.login_user_title = QLabel(medicine_login)
        self.login_user_title.setObjectName(u"login_user_title")
        self.login_user_title.setGeometry(QRect(140, 110, 101, 31))
        self.login_pwd_title = QLabel(medicine_login)
        self.login_pwd_title.setObjectName(u"login_pwd_title")
        self.login_pwd_title.setGeometry(QRect(140, 150, 101, 31))
        self.login_user = QLineEdit(medicine_login)
        self.login_user.setObjectName(u"login_user")
        self.login_user.setGeometry(QRect(250, 110, 311, 31))
        self.login_pwd = QLineEdit(medicine_login)
        self.login_pwd.setObjectName(u"login_pwd")
        self.login_pwd.setGeometry(QRect(250, 150, 311, 31))
        self.login_pwd.setEchoMode(QLineEdit.Password)
        self.login_msg = QLabel(medicine_login)
        self.login_msg.setObjectName(u"login_msg")
        self.login_msg.setGeometry(QRect(100, 300, 511, 31))
        self.login_msg.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(medicine_login)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(150, 200, 381, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_login = QPushButton(self.layoutWidget)
        self.btn_login.setObjectName(u"btn_login")

        self.horizontalLayout.addWidget(self.btn_login)

        self.btn_cancel = QPushButton(self.layoutWidget)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_register = QPushButton(self.layoutWidget)
        self.btn_register.setObjectName(u"btn_register")

        self.horizontalLayout.addWidget(self.btn_register)


        self.retranslateUi(medicine_login)

        QMetaObject.connectSlotsByName(medicine_login)
    # setupUi

    def retranslateUi(self, medicine_login):
        medicine_login.setWindowTitle(QCoreApplication.translate("medicine_login", u"Frame", None))
        self.login_bg.setText("")
        self.label.setText(QCoreApplication.translate("medicine_login", u"\u5927\u585a\u88fd\u85e5 I6 \u5075\u6e2c\u8cc7\u6599\u81ea\u52d5\u5099\u4efd", None))
        self.login_user_title.setText(QCoreApplication.translate("medicine_login", u"\u5e33\u865f", None))
        self.login_pwd_title.setText(QCoreApplication.translate("medicine_login", u"\u5bc6\u78bc", None))
        self.login_msg.setText("")
        self.btn_login.setText(QCoreApplication.translate("medicine_login", u"\u767b\u5165", None))
        self.btn_cancel.setText(QCoreApplication.translate("medicine_login", u"\u53d6\u6d88", None))
        self.btn_register.setText(QCoreApplication.translate("medicine_login", u"\u8a3b\u518a", None))
    # retranslateUi

