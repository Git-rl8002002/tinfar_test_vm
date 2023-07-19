# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_3.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_medicine_main_3(object):
    def setupUi(self, medicine_main_3):
        if not medicine_main_3.objectName():
            medicine_main_3.setObjectName(u"medicine_main_3")
        medicine_main_3.resize(800, 600)
        medicine_main_3.setStyleSheet(u" #a_user , #a_pwd , #a_r_time , #a_status{\n"
"background-color:#cccccc;\n"
"border-bottom-right-radius:20px;\n"
"padding:3px 3px;\n"
"}")
        self.action_realtime_monitor = QAction(medicine_main_3)
        self.action_realtime_monitor.setObjectName(u"action_realtime_monitor")
        self.action_account = QAction(medicine_main_3)
        self.action_account.setObjectName(u"action_account")
        self.action_logout = QAction(medicine_main_3)
        self.action_logout.setObjectName(u"action_logout")
        self.action_backup = QAction(medicine_main_3)
        self.action_backup.setObjectName(u"action_backup")
        self.centralwidget = QWidget(medicine_main_3)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_title = QWidget()
        self.page_title.setObjectName(u"page_title")
        self.verticalLayout_5 = QVBoxLayout(self.page_title)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.main_title = QLabel(self.page_title)
        self.main_title.setObjectName(u"main_title")
        font = QFont()
        font.setPointSize(36)
        self.main_title.setFont(font)
        self.main_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.main_title)

        self.stackedWidget.addWidget(self.page_title)
        self.page_account = QWidget()
        self.page_account.setObjectName(u"page_account")
        self.horizontalLayout_2 = QHBoxLayout(self.page_account)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.page_account)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_account_list = QListWidget(self.groupBox)
        self.main_account_list.setObjectName(u"main_account_list")

        self.verticalLayout_2.addWidget(self.main_account_list)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.page_account)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.a_r_time = QLabel(self.groupBox_2)
        self.a_r_time.setObjectName(u"a_r_time")

        self.verticalLayout_3.addWidget(self.a_r_time)

        self.a_user = QLabel(self.groupBox_2)
        self.a_user.setObjectName(u"a_user")

        self.verticalLayout_3.addWidget(self.a_user)

        self.a_pwd = QLabel(self.groupBox_2)
        self.a_pwd.setObjectName(u"a_pwd")

        self.verticalLayout_3.addWidget(self.a_pwd)

        self.a_status = QLabel(self.groupBox_2)
        self.a_status.setObjectName(u"a_status")

        self.verticalLayout_3.addWidget(self.a_status)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.page_account)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.account_login_record = QListWidget(self.groupBox_3)
        self.account_login_record.setObjectName(u"account_login_record")

        self.verticalLayout_4.addWidget(self.account_login_record)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.stackedWidget.addWidget(self.page_account)

        self.horizontalLayout.addWidget(self.stackedWidget)

        medicine_main_3.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(medicine_main_3)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        medicine_main_3.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(medicine_main_3)
        self.statusbar.setObjectName(u"statusbar")
        medicine_main_3.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.action_account)
        self.menu.addSeparator()
        self.menu.addAction(self.action_logout)
        self.menu_2.addAction(self.action_realtime_monitor)
        self.menu_3.addAction(self.action_backup)

        self.retranslateUi(medicine_main_3)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(medicine_main_3)
    # setupUi

    def retranslateUi(self, medicine_main_3):
        medicine_main_3.setWindowTitle(QCoreApplication.translate("medicine_main_3", u"MainWindow", None))
        self.action_realtime_monitor.setText(QCoreApplication.translate("medicine_main_3", u"\u5373\u6642\u76e3\u63a7", None))
#if QT_CONFIG(tooltip)
        self.action_realtime_monitor.setToolTip(QCoreApplication.translate("medicine_main_3", u"\u5373\u6642\u76e3\u63a7", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_realtime_monitor.setShortcut(QCoreApplication.translate("medicine_main_3", u"Alt+M", None))
#endif // QT_CONFIG(shortcut)
        self.action_account.setText(QCoreApplication.translate("medicine_main_3", u"\u5e33\u865f", None))
#if QT_CONFIG(tooltip)
        self.action_account.setToolTip(QCoreApplication.translate("medicine_main_3", u"\u5e33\u865f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_account.setShortcut(QCoreApplication.translate("medicine_main_3", u"Alt+A", None))
#endif // QT_CONFIG(shortcut)
        self.action_logout.setText(QCoreApplication.translate("medicine_main_3", u"\u767b\u51fa", None))
#if QT_CONFIG(tooltip)
        self.action_logout.setToolTip(QCoreApplication.translate("medicine_main_3", u"\u767b\u51fa", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_logout.setShortcut(QCoreApplication.translate("medicine_main_3", u"Alt+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_backup.setText(QCoreApplication.translate("medicine_main_3", u"\u5099\u4efd\u7ba1\u7406", None))
#if QT_CONFIG(tooltip)
        self.action_backup.setToolTip(QCoreApplication.translate("medicine_main_3", u"\u5099\u4efd\u7ba1\u7406", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_backup.setShortcut(QCoreApplication.translate("medicine_main_3", u"Alt+B", None))
#endif // QT_CONFIG(shortcut)
        self.main_title.setText(QCoreApplication.translate("medicine_main_3", u"\u5927\u585a\u88fd\u85e5  I6 \u81ea\u52d5\u8cc7\u6599\u5099\u4efd", None))
        self.groupBox.setTitle(QCoreApplication.translate("medicine_main_3", u"\u5e33\u865f\u6e05\u55ae", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("medicine_main_3", u"\u8a73\u7d30\u8cc7\u6599", None))
        self.a_r_time.setText(QCoreApplication.translate("medicine_main_3", u"record time", None))
        self.a_user.setText(QCoreApplication.translate("medicine_main_3", u"user", None))
        self.a_pwd.setText(QCoreApplication.translate("medicine_main_3", u"pwd", None))
        self.a_status.setText(QCoreApplication.translate("medicine_main_3", u"status", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("medicine_main_3", u"\u767b\u5165\u8a18\u9304", None))
        self.menu.setTitle(QCoreApplication.translate("medicine_main_3", u"\u4eba\u54e1\u7ba1\u7406", None))
        self.menu_2.setTitle(QCoreApplication.translate("medicine_main_3", u"\u76e3\u63a7", None))
        self.menu_3.setTitle(QCoreApplication.translate("medicine_main_3", u"\u5099\u4efd", None))
    # retranslateUi

