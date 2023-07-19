# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_medicine_login(object):
    def setupUi(self, medicine_login):
        if not medicine_login.objectName():
            medicine_login.setObjectName(u"medicine_login")
        medicine_login.resize(566, 331)
        self.centralwidget = QWidget(medicine_login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(18)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.login_pwd = QLineEdit(self.groupBox)
        self.login_pwd.setObjectName(u"login_pwd")
        self.login_pwd.setFont(font)
        self.login_pwd.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.login_pwd, 4, 0, 1, 1)

        self.login_msg = QLabel(self.groupBox)
        self.login_msg.setObjectName(u"login_msg")
        self.login_msg.setFont(font)
        self.login_msg.setStyleSheet(u"")
        self.login_msg.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.login_msg, 5, 0, 1, 1)

        self.login_user = QLineEdit(self.groupBox)
        self.login_user.setObjectName(u"login_user")
        self.login_user.setFont(font)

        self.gridLayout.addWidget(self.login_user, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_login = QPushButton(self.groupBox)
        self.btn_login.setObjectName(u"btn_login")
        font1 = QFont()
        font1.setPointSize(16)
        self.btn_login.setFont(font1)
        icon = QIcon()
        icon.addFile(u"icon/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_login.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_login)

        self.btn_cancel = QPushButton(self.groupBox)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_register = QPushButton(self.groupBox)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_register)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(24)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        medicine_login.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(medicine_login)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 566, 24))
        medicine_login.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(medicine_login)
        self.statusbar.setObjectName(u"statusbar")
        medicine_login.setStatusBar(self.statusbar)

        self.retranslateUi(medicine_login)

        QMetaObject.connectSlotsByName(medicine_login)
    # setupUi

    def retranslateUi(self, medicine_login):
        medicine_login.setWindowTitle(QCoreApplication.translate("medicine_login", u"Login", None))
#if QT_CONFIG(tooltip)
        medicine_login.setToolTip(QCoreApplication.translate("medicine_login", u"\u5927\u585a\u88fd\u85e5", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle("")
#if QT_CONFIG(tooltip)
        self.login_pwd.setToolTip(QCoreApplication.translate("medicine_login", u"insert password", None))
#endif // QT_CONFIG(tooltip)
        self.login_pwd.setPlaceholderText(QCoreApplication.translate("medicine_login", u"password", None))
        self.login_msg.setText("")
#if QT_CONFIG(tooltip)
        self.login_user.setToolTip(QCoreApplication.translate("medicine_login", u"insert username", None))
#endif // QT_CONFIG(tooltip)
        self.login_user.setPlaceholderText(QCoreApplication.translate("medicine_login", u"username", None))
#if QT_CONFIG(tooltip)
        self.btn_login.setToolTip(QCoreApplication.translate("medicine_login", u"\u767b\u5165", None))
#endif // QT_CONFIG(tooltip)
        self.btn_login.setText(QCoreApplication.translate("medicine_login", u"\u767b\u5165", None))
        self.btn_cancel.setText(QCoreApplication.translate("medicine_login", u"\u53d6\u6d88", None))
        self.btn_register.setText(QCoreApplication.translate("medicine_login", u"\u8a3b\u518a", None))
        self.label.setText(QCoreApplication.translate("medicine_login", u"\u5927\u585a\u88fd\u85e5 I6 \u8cc7\u6599\u81ea\u52d5\u5099\u4efd", None))
        self.label_2.setText(QCoreApplication.translate("medicine_login", u"\u5e33\u865f", None))
        self.label_3.setText(QCoreApplication.translate("medicine_login", u"\u5bc6\u78bc", None))
    # retranslateUi

