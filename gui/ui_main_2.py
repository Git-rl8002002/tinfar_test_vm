# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_2.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_medicine_main(object):
    def setupUi(self, medicine_main):
        if not medicine_main.objectName():
            medicine_main.setObjectName(u"medicine_main")
        medicine_main.setEnabled(True)
        medicine_main.resize(800, 626)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(medicine_main.sizePolicy().hasHeightForWidth())
        medicine_main.setSizePolicy(sizePolicy)
        medicine_main.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../icon/database.png", QSize(), QIcon.Normal, QIcon.Off)
        medicine_main.setWindowIcon(icon)
        medicine_main.setStyleSheet(u"#btn_start_monitor_i6:hover , #btn_stop_monitor_i6:hover , #btn_reoad_by_month:hover , #rts_1:hover , #rts_2:hover , #rts_3:hover , #rts_4:hover , #rts_5:hover , #rts_6:hover , #rts_7:hover , #rts_8:hover , #rts_9:hover , #rts_10:hover , #rts_11:hover , #rts_12:hover , #rts_13:hover , #rts_14:hover , #rts_15:hover , #rts_16:hover , #rts_17:hover ,  #rts_18:hover{\n"
"background-color:gray;\n"
"color:white;\n"
"}\n"
"#btn_start_monitor_i6 , #btn_stop_monitor_i6 , #btn_reoad_by_month{\n"
"background-color:#cccccc;\n"
"border-radius:10px;\n"
"padding:3px 3px;\n"
"}\n"
"#monitor_item1:hover, #monitor_item2:hover , #monitor_item3:hover , #monitor_item4:hover , #monitor_item5:hover , #monitor_item1_2:hover , #monitor_item2_2:hover , #monitor_item3_2:hover , #monitor_item4_2:hover, #monitor_item5_2:hover , #a_user:hover , #a_pwd:hover , #a_r_time:hover , #a_status:hover , #reload_final_record_by_month:hover , #btn_i6_1_temp_chart:hover , #btn_i6_1_rh_chart:hover , #btn_i6_1_pr_chart:hover , #btn_i6_1_nh3_chart:hover "
                        ", #btn_i6_1_h2s_chart:hover , #btn_i6_1_temp_stop_chart:hover , #realtime_i6_2_statusbar:hover , #i6_1_amount_chart:hover ,  #btn_start_rtms:hover , #btn_stop_rtms:hover{\n"
"background-color:gray;\n"
"color:white;\n"
"}\n"
"#monitor_item1 , #monitor_item2 , #monitor_item3 , #monitor_item4 , #monitor_item5 , #monitor_item1_2 , #monitor_item2_2 , #monitor_item3_2 , #monitor_item4_2 , #monitor_item5_2 , #reload_final_record_by_month , #a_user , #a_pwd , #a_r_time , #a_status , #btn_i6_1_temp_chart , #btn_i6_1_rh_chart , #btn_i6_1_pr_chart , #btn_i6_1_nh3_chart , #btn_i6_1_h2s_chart , #realtime_i6_2_statusbar , #btn_i6_1_temp_stop_chart , #i6_1_amount_chart , #btn_start_rtms , #btn_stop_rtms , #rts_1, #rts_2, #rts_3, #rts_4, #rts_5, #rts_6, #rts_7, #rts_8, #rts_9, #rts_10, #rts_11, #rts_12 , #rts_13 , #rts_14 , #rts_15 , #rts_16 , #rts_17 ,  #rts_18{\n"
"background-color:#cccccc;\n"
"border-radius:10px;\n"
"padding:3px 3px;\n"
"}\n"
"")
        self.tab_realtime_monitor = QWidget()
        self.tab_realtime_monitor.setObjectName(u"tab_realtime_monitor")
        self.gridLayout_3 = QGridLayout(self.tab_realtime_monitor)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.tab_realtime_monitor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 1, 3, 1)
        self.rts_time_1 = QLabel(self.groupBox_2)
        self.rts_time_1.setObjectName(u"rts_time_1")

        self.verticalLayout_2.addWidget(self.rts_time_1)

        self.rts_1 = QLabel(self.groupBox_2)
        self.rts_1.setObjectName(u"rts_1")
        self.rts_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.rts_1)

        self.rts_2 = QLabel(self.groupBox_2)
        self.rts_2.setObjectName(u"rts_2")
        self.rts_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.rts_2)

        self.rts_3 = QLabel(self.groupBox_2)
        self.rts_3.setObjectName(u"rts_3")
        self.rts_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.rts_3)

        self.rts_4 = QLabel(self.groupBox_2)
        self.rts_4.setObjectName(u"rts_4")
        self.rts_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.rts_4)

        self.rts_5 = QLabel(self.groupBox_2)
        self.rts_5.setObjectName(u"rts_5")
        self.rts_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.rts_5)

        self.rts_6 = QLabel(self.groupBox_2)
        self.rts_6.setObjectName(u"rts_6")
        self.rts_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.rts_6)

        self.rts_7 = QLabel(self.groupBox_2)
        self.rts_7.setObjectName(u"rts_7")
        self.rts_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.rts_7)

        self.rts_8 = QLabel(self.groupBox_2)
        self.rts_8.setObjectName(u"rts_8")
        self.rts_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.rts_8)


        self.gridLayout_3.addWidget(self.groupBox_2, 2, 1, 1, 1)

        self.medicine_img = QGraphicsView(self.tab_realtime_monitor)
        self.medicine_img.setObjectName(u"medicine_img")
        self.medicine_img.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.medicine_img, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.tab_realtime_monitor)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 1, 3, 1)
        self.rts_time_2 = QLabel(self.groupBox)
        self.rts_time_2.setObjectName(u"rts_time_2")

        self.verticalLayout.addWidget(self.rts_time_2)

        self.rts_9 = QLabel(self.groupBox)
        self.rts_9.setObjectName(u"rts_9")
        self.rts_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.rts_9)

        self.rts_10 = QLabel(self.groupBox)
        self.rts_10.setObjectName(u"rts_10")
        self.rts_10.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.rts_10)

        self.rts_11 = QLabel(self.groupBox)
        self.rts_11.setObjectName(u"rts_11")
        self.rts_11.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.rts_11)

        self.rts_12 = QLabel(self.groupBox)
        self.rts_12.setObjectName(u"rts_12")
        self.rts_12.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.rts_12)

        self.rts_13 = QLabel(self.groupBox)
        self.rts_13.setObjectName(u"rts_13")
        self.rts_13.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.rts_13)

        self.rts_14 = QLabel(self.groupBox)
        self.rts_14.setObjectName(u"rts_14")
        self.rts_14.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.rts_14)

        self.rts_15 = QLabel(self.groupBox)
        self.rts_15.setObjectName(u"rts_15")
        self.rts_15.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.rts_15)

        self.rts_16 = QLabel(self.groupBox)
        self.rts_16.setObjectName(u"rts_16")
        self.rts_16.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.rts_16)


        self.gridLayout_3.addWidget(self.groupBox, 2, 2, 1, 1)

        self.btn_stop_rtms = QPushButton(self.tab_realtime_monitor)
        self.btn_stop_rtms.setObjectName(u"btn_stop_rtms")
        self.btn_stop_rtms.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"../icon/icons8-close-window-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_stop_rtms.setIcon(icon1)

        self.gridLayout_3.addWidget(self.btn_stop_rtms, 1, 2, 1, 1)

        self.btn_start_rtms = QPushButton(self.tab_realtime_monitor)
        self.btn_start_rtms.setObjectName(u"btn_start_rtms")
        self.btn_start_rtms.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"../icon/icons8-start-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start_rtms.setIcon(icon2)

        self.gridLayout_3.addWidget(self.btn_start_rtms, 1, 1, 1, 1)

        icon3 = QIcon()
        icon3.addFile(u"../icon/icons8-sync-48.png", QSize(), QIcon.Normal, QIcon.Off)
        medicine_main.addTab(self.tab_realtime_monitor, icon3, "")
        self.tab_realtime = QWidget()
        self.tab_realtime.setObjectName(u"tab_realtime")
        self.gridLayout_2 = QGridLayout(self.tab_realtime)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_5 = QGroupBox(self.tab_realtime)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.realtime_monitor_i6_list_2 = QListWidget(self.groupBox_5)
        self.realtime_monitor_i6_list_2.setObjectName(u"realtime_monitor_i6_list_2")
        font = QFont()
        font.setFamilies([u"Microsoft JhengHei"])
        font.setPointSize(12)
        self.realtime_monitor_i6_list_2.setFont(font)

        self.verticalLayout_5.addWidget(self.realtime_monitor_i6_list_2)


        self.gridLayout_2.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_4 = QGroupBox(self.tab_realtime)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.realtime_monitor_i6_list = QTreeWidget(self.groupBox_4)
        self.realtime_monitor_i6_list.setObjectName(u"realtime_monitor_i6_list")
        self.realtime_monitor_i6_list.setFont(font)
        self.realtime_monitor_i6_list.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.realtime_monitor_i6_list)


        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        icon4 = QIcon()
        icon4.addFile(u"../icon/school-material.png", QSize(), QIcon.Normal, QIcon.Off)
        medicine_main.addTab(self.tab_realtime, icon4, "")
        self.tab_backup_month = QWidget()
        self.tab_backup_month.setObjectName(u"tab_backup_month")
        self.gridLayout_6 = QGridLayout(self.tab_backup_month)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_10 = QGroupBox(self.tab_backup_month)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_9 = QGroupBox(self.groupBox_10)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.backup_by_month = QTreeWidget(self.groupBox_9)
        self.backup_by_month.setObjectName(u"backup_by_month")
        self.backup_by_month.setFont(font)
        self.backup_by_month.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.backup_by_month)

        self.groupBox_12 = QGroupBox(self.groupBox_9)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_2 = QLabel(self.groupBox_12)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_12.addWidget(self.label_2)


        self.verticalLayout_9.addWidget(self.groupBox_12)


        self.verticalLayout_11.addWidget(self.groupBox_9)

        self.groupBox_8 = QGroupBox(self.groupBox_10)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.backup_by_month_day = QTreeWidget(self.groupBox_8)
        self.backup_by_month_day.setObjectName(u"backup_by_month_day")
        self.backup_by_month_day.setFont(font)
        self.backup_by_month_day.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.backup_by_month_day)

        self.groupBox_13 = QGroupBox(self.groupBox_8)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_4 = QLabel(self.groupBox_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_13.addWidget(self.label_4)


        self.verticalLayout_8.addWidget(self.groupBox_13)


        self.verticalLayout_11.addWidget(self.groupBox_8)

        self.groupBox_11 = QGroupBox(self.groupBox_10)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.reload_final_record_by_month = QLabel(self.groupBox_11)
        self.reload_final_record_by_month.setObjectName(u"reload_final_record_by_month")
        self.reload_final_record_by_month.setFont(font)
        self.reload_final_record_by_month.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.reload_final_record_by_month)

        self.btn_reoad_by_month = QCommandLinkButton(self.groupBox_11)
        self.btn_reoad_by_month.setObjectName(u"btn_reoad_by_month")
        self.btn_reoad_by_month.setFont(font)
        self.btn_reoad_by_month.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"../icon/icons8-backup-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reoad_by_month.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.btn_reoad_by_month)


        self.verticalLayout_11.addWidget(self.groupBox_11)


        self.gridLayout_5.addWidget(self.groupBox_10, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        icon6 = QIcon()
        icon6.addFile(u"../icon/db_storage.ico", QSize(), QIcon.Normal, QIcon.Off)
        medicine_main.addTab(self.tab_backup_month, icon6, "")

        self.retranslateUi(medicine_main)

        medicine_main.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(medicine_main)
    # setupUi

    def retranslateUi(self, medicine_main):
        medicine_main.setWindowTitle(QCoreApplication.translate("medicine_main", u"\u5927\u585a\u88fd\u85e5\u81ea\u52d5\u5099\u4efd", None))
#if QT_CONFIG(tooltip)
        medicine_main.setToolTip(QCoreApplication.translate("medicine_main", u"\u5927\u585a\u88fd\u85e5\u81ea\u52d5\u5099\u4efd", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("medicine_main", u"I6-1", None))
        self.rts_time_1.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_1.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_2.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_3.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_4.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_5.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_6.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_7.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_8.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.groupBox.setTitle(QCoreApplication.translate("medicine_main", u"I6-2", None))
        self.rts_time_2.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_9.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_10.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_11.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_12.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_13.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_14.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_15.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.rts_16.setText(QCoreApplication.translate("medicine_main", u"TextLabel", None))
        self.btn_stop_rtms.setText(QCoreApplication.translate("medicine_main", u"\u505c\u6b62", None))
        self.btn_start_rtms.setText(QCoreApplication.translate("medicine_main", u"\u555f\u52d5", None))
        medicine_main.setTabText(medicine_main.indexOf(self.tab_realtime_monitor), QCoreApplication.translate("medicine_main", u"\u5373\u6642\u6578\u64da", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("medicine_main", u"I6 - 2", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("medicine_main", u"I6 - 1", None))
        ___qtreewidgetitem = self.realtime_monitor_i6_list.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("medicine_main", u"\u786b\u5316\u6c2b", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("medicine_main", u"\u6c28\u6c23", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("medicine_main", u"\u5927\u6c23\u58d3\u529b", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("medicine_main", u"\u6fd5\u5ea6", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("medicine_main", u"\u6eab\u5ea6", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("medicine_main", u"\u76e3\u63a7\u6642\u9593", None));
        medicine_main.setTabText(medicine_main.indexOf(self.tab_realtime), QCoreApplication.translate("medicine_main", u"\u6578\u64da\u6e05\u55ae", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("medicine_main", u"\u5099\u4efd", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("medicine_main", u"\u6708\u5099\u4efd\u7d71\u8a08\u6e05\u55ae", None))
        ___qtreewidgetitem1 = self.backup_by_month.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("medicine_main", u"\u7e3d\u7b46\u6578", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("medicine_main", u"\u65e5\u671f", None));
        self.groupBox_12.setTitle(QCoreApplication.translate("medicine_main", u"\u8aaa\u660e", None))
        self.label_2.setText(QCoreApplication.translate("medicine_main", u"( \u6309\u4e00\u4e0b ) \u986f\u793a\u7576\u6708\u6bcf\u65e5\u8a18\u9304\uff0c( \u6309\u5169\u4e0b ) \u4e0b\u8f09\u7576\u6708PDF\u5099\u4efd\u8a18\u9304", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("medicine_main", u"\u65e5\u5099\u4efd\u7d71\u8a08\u6e05\u55ae", None))
        ___qtreewidgetitem2 = self.backup_by_month_day.headerItem()
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("medicine_main", u"\u7e3d\u7b46\u6578", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("medicine_main", u"\u65e5\u671f", None));
        self.groupBox_13.setTitle(QCoreApplication.translate("medicine_main", u"\u8aaa\u660e", None))
        self.label_4.setText(QCoreApplication.translate("medicine_main", u"( \u6309\u5169\u4e0b ) \u4e0b\u8f09\u7576\u65e5PDF\u5099\u4efd\u8a18\u9304", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("medicine_main", u"\u5237\u65b0", None))
        self.reload_final_record_by_month.setText("")
        self.btn_reoad_by_month.setText(QCoreApplication.translate("medicine_main", u"\u91cd\u65b0\u6574\u7406\u6708\u5099\u4efd\u7e3d\u6578", None))
        medicine_main.setTabText(medicine_main.indexOf(self.tab_backup_month), QCoreApplication.translate("medicine_main", u"\u5099\u4efd", None))
    # retranslateUi

