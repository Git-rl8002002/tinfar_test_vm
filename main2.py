#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20221116
# Update   : 20230207
# Version  : 1.1
# Function : 大塚製藥 get I6 sensor value

import sys , time , pymysql , platform
from pyModbusTCP.client import *
from PyQt6 import QtCore , QtGui , QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCharts import QChart , QChartView , QLineSeries , QScatterSeries , QDateTimeAxis , QValueAxis
from fpdf import *
import matplotlib.pyplot as plt

from control.dao import *
from gui.ui_main_2 import *
from gui.ui_main_3 import *

########################################################################################################################
# main_content
########################################################################################################################
class main_content(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_medicine_main()
        self.ui.setupUi(self)
        self.main_init()

    ##############
    # main_init
    ##############
    def main_init(self):
        
        #############################
        # tab 1 - realtime_monitor
        #############################
        ### show floor plan and monitor data
        self.realtime_monitor()
        ### start realtime monitor
        self.ui.btn_start_rtms.clicked.connect(self.start_cmd_realtime_main_tab3_backup)
        ### stop realtime monitor
        self.ui.btn_stop_rtms.clicked.connect(self.stop_cmd_realtime_main_tab3_backup)

        #######################################
        # tab 2 - realtime monitor data list
        #######################################

        ####################################
        # tab 3 - backup by month and day
        ####################################
        ### load backup data 
        self.gui_realtime_main_tab3_backup()
        ### reload backup data
        self.ui.btn_reoad_by_month.clicked.connect(self.reload_main_tab3_backup)

    #####################
    # realtime_monitor
    #####################
    def realtime_monitor(self):
        try:
            ################################
            # realtime monitor floor plan
            ################################
            
            self.os_sys = platform.system()

            ### Mac
            if self.os_sys == "Darwin":
                self.img = QtGui.QPixmap('/Users/user/eclipse-workspace/tinfar/medicine/img/medicine_platform_2.jpg')
            ### Win
            elif self.os_sys == 'Windows':
                self.img   = QtGui.QPixmap('d:/medicine/img/medicine_platform_2.jpg')

            self.img_w = 1440
            self.img_h = 1280
            self.img   = self.img.scaled(self.img_w, self.img_h)

            self.scene = QtWidgets.QGraphicsScene()
            self.scene.addPixmap(self.img)

            self.ui.medicine_img.setScene(self.scene)
            self.ui.medicine_img.show()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , str(e))
        finally:
            pass

        #################################
        # realtime monitor I6-1 , I6-2 
        #################################
        try:
            ### record time
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime()) 
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y_%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

            ### realtime time I6-1 , I6-2
            self.ui.rts_time_1.setText(str(self.r_time))
            self.ui.rts_time_2.setText(str(self.r_time))

            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr = self.conn.cursor()

            ### I6 - 1
            self.sql = "select val_1 , val_2 from {0} where r_day='{1}' order by r_day desc limit 0,1".format(self.r_month , self.r_day)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                self.ui.rts_1.setText('1).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_2.setText('2).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_3.setText('3).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_4.setText('4).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_5.setText('5).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_6.setText('6).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_7.setText('7).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_8.setText('8).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
            
            ### I6 - 2
            self.sql = "select val_1 , val_2 from {0} where r_day='{1}' order by r_day desc limit 0,1".format(self.r_month , self.r_day)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                self.ui.rts_9.setText('9).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_10.setText('10).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_11.setText('11).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_12.setText('12).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_13.setText('13).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_14.setText('14).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_15.setText('15).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
                self.ui.rts_16.setText('16).' + str(val[0]) + ' °C , ' + str(val[1]) + ' %')
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , str(e))
        finally:
            pass

    ###############
    # i6_1_chart
    ###############
    def i6_1_chart(self , item):
        try:
            self.kind   = 'I6-1' 
            self.item   = item
            self.amount = self.ui.i6_1_amount_chart.currentText()

            if len(self.amount) == 0:
                QMessageBox.information(self , 'Msg' , str('先選顯示筆數 !'))
            
            else:
                ### record time
                self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime()) 
                self.r_year  = time.strftime("%Y" , time.localtime())
                self.r_month = time.strftime("%Y_%m" , time.localtime())
                self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
                self.curr = self.conn.cursor()
                
                if self.item == 'temp':
                    self.sql = "select val_1 , r_time from {0} order by r_time desc limit 0,{1}".format(self.r_month , self.amount)
                if self.item == 'rh':
                    self.sql = "select val_2 , r_time from {0} order by r_time desc limit 0,{1}".format(self.r_month , self.amount)

                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()

                ##################
                # data to chart
                ##################
                self.charts     = QChart()
                self.charts.legend().hide()
                self.charts.setTitle(self.kind)
                self.charts.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

                self.chart_view = QChartView(self.charts)
                #self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

                ### 曲線
                self.series0       = QLineSeries()
                #self.series0.setPen(QPen(QColor('skyblue') , 3))

                ### 顯示點的值
                self.series1       = QScatterSeries()
                #self.series1.setColor(QColor('skyblue'))
                #self.series1.setPen(QPen(QColor('skyblue') , 1))

                for val in self.res:
                    if self.item == 'temp':
                        ### temp chart para
                        self.series0.setName('溫度線')
                        self.series1.setName('目前TEMP(°C)')
                        self.date_fmt = "HH:mm:ss"
                        self.data = str(val[1]).split(" ")
                        self.time = self.data[1]
                        self.x = QDateTime().fromString(self.time , self.date_fmt).toMSecsSinceEpoch()
                        self.y = float(val[0])
                        self.series0.append(self.x , self.y)
                        self.series1.append(self.x , self.y)
                        self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_temp)

                    elif self.item == 'rh':
                        ### rh chart para
                        self.series0.setName('濕度線')
                        self.series1.setName('目前RH(%)')
                        self.date_fmt = "HH:mm:ss"
                        self.data = str(val[1]).split(" ")
                        self.time = self.data[1]
                        self.x = QDateTime().fromString(self.time , self.date_fmt).toMSecsSinceEpoch()
                        self.y = float(val[0])
                        self.series0.append(self.x , self.y)
                        self.series1.append(self.x , self.y)
                        self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_rh)
                
                self.charts.addSeries(self.series0)
                self.charts.addSeries(self.series1)
                
                ### TEMP X-axis
                self.axis_x = QDateTimeAxis()
                self.axis_x.setTickCount(20)
                self.axis_x.setFormat("HH:mm:ss")
                self.axis_x.setTitleText("時間")
                self.charts.addAxis(self.axis_x , Qt.AlignmentFlag.AlignBottom)
                self.series0.attachAxis(self.axis_x)
            
                ### TEMP Y-axis
                self.axis_y = QValueAxis()
                self.axis_y.setTickCount(20)
                self.axis_y.setLabelFormat("%.1f")
                self.axis_y.setTitleText("數值")
                self.charts.addAxis(self.axis_y , Qt.AlignmentFlag.AlignLeft)
                self.series0.attachAxis(self.axis_y)

                ### chart TEMP
                self.chart_ph = QWidget()
                self.sub_ph   = QHBoxLayout()
                self.sub_ph.addWidget(self.chart_view)
                self.chart_ph.setLayout(self.sub_ph)
                self.chart_ph.setContentsMargins(0, 0, 0,0)
                self.chart_ph.resize(800,600)
                self.chart_ph.show()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > i6_1_chart : ' + str(e))
        finally:
            pass

    ###########################################
    # history record to chart mouse hover RH
    ###########################################
    def history_record_to_chart_mouse_hover_rh(self , point):
        self.n_time = QDateTime.fromMSecsSinceEpoch(int(point.x())).toString('HH:mm:ss')
        self.series1.setName( self.n_time + ' , 目前 RH ' + str(point.y()) + ' %') 

    ###########################################
    # history record to chart mouse hover TEMP
    ###########################################
    def history_record_to_chart_mouse_hover_temp(self , point):
        self.n_time = QDateTime.fromMSecsSinceEpoch(int(point.x())).toString('HH:mm:ss')
        self.series1.setName( self.n_time + ' , 目前 TEMP ' + str(point.y()) + ' °C') 

    ############################
    # reload_main_tab3_backup
    ############################
    def reload_main_tab3_backup(self):
        #### record time
        self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        self.ui.reload_final_record_by_month.setText(self.r_time)
        
        ### clear 
        self.ui.backup_by_month.clear()

        ### reload by month
        self.gui_realtime_main_tab3_backup()

    #######################################
    # stop_cmd_realtime_main_tab3_backup
    #######################################
    def stop_cmd_realtime_main_tab3_backup(self):
        try:
            ### disable and enable btn
            self.ui.btn_start_rtms.setEnabled(True)
            self.ui.btn_stop_rtms.setEnabled(False)

            ### stop realtime monitor sensor
            self.start_rtms.stop()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > stop_cmd_realtime_main_tab3_backup : ' + str(e))
        finally:
            pass

    ########################################
    # start_cmd_realtime_main_tab3_backup
    ########################################
    def start_cmd_realtime_main_tab3_backup(self):
        try:
            ### disable and enable btn
            self.ui.btn_start_rtms.setEnabled(False)
            self.ui.btn_stop_rtms.setEnabled(True)

            ### start realtime monitor sensor
            self.start_rtms = QTimer()
            self.start_rtms.timeout.connect(self.realtime_monitor)
            self.start_rtms.timeout.connect(self.cmd_realtime_main_tab3_backup)
            self.start_rtms.start(60000)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > start_cmd_realtime_main_tab3_backup : ' + str(e))
        finally:
            pass

    ##################################
    # cmd_realtime_main_tab3_backup
    ##################################
    def cmd_realtime_main_tab3_backup(self):
        try:
            ### variable
            self.kind  = 'CB'
            self.kind2 = 'I6-2'

            ### record time
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime()) 
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y_%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr = self.conn.cursor()
            
            #########
            # i6-1
            #########
            self.i6_1_sql = "select r_time , val_1 , val_2 , val_3 , val_4 , val_5 from {0} where r_day='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.r_month , self.r_day , self.kind)
            self.curr.execute(self.i6_1_sql)
            self.res1 = self.curr.fetchall()

            self.ui.realtime_monitor_i6_list.setHeaderLabels(['監控時間','溫度','濕度','大氣壓力','氨氣','硫化氫'])
            self.ui.realtime_monitor_i6_list.setColumnWidth(0 , 220)
            
            for val in self.res1:
                self.root = QTreeWidgetItem(self.ui.realtime_monitor_i6_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]) + ' °C')
                self.root.setText(2 , str(val[2]) + ' %')
                self.root.setText(3 , str(val[3]) + ' ppm')
                self.root.setText(4 , str(val[4]) + ' ug/m3')
                self.root.setText(5 , str(val[5]) + ' ppm' )

            #########
            # i6-2
            #########
            self.i6_2_sql = "select r_time , val_1 , val_2 , val_3 , val_4 , val_5 from {0} where r_day='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.r_month , self.r_day , self.kind2)
            self.curr.execute(self.i6_2_sql)
            self.res2 = self.curr.fetchall()
            
            for val in self.res2:
                
                self.ui.realtime_monitor_i6_list_2.addItem(str(val[0]))
                self.ui.realtime_monitor_i6_list_2.addItem('TEMP : ' + str(val[1]) + ' °C , RH :' + str(val[2]) + ' %')

            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > cmd realtime main tab3 backup : ' + str(e))
        finally:
            pass
    
    ##################################
    # gui_realtime_main_tab3_backup
    ##################################
    def gui_realtime_main_tab3_backup(self):
        
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr = self.conn.cursor()
            self.sql = "show tables"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()
            self.conn.commit()

            for val in self.res:
                
                self.data = val[0]
                self.data2 = str(self.data[0:1])

                self.ui.backup_by_month.setHeaderLabels(['日期','總筆數'])
                self.ui.backup_by_month.setColumnWidth(0 , 150)
                
                if self.data2.isdigit():
                    self.data3 = self.data.split('_')
                    self.by_month = self.data3[0] + '-' + self.data3[1]

                    ### total by month
                    self.sql2 = "select count(*) from {0}".format(self.data)
                    self.curr.execute(self.sql2)
                    self.res2 = self.curr.fetchone()

                    self.root = QTreeWidgetItem(self.ui.backup_by_month)
                    self.root.setText(0 , str(self.by_month))
                    self.root.setText(1 , str(self.res2[0]) + ' 筆記錄')

            ### click show total in day by month
            self.ui.backup_by_month.clicked.connect(self.show_total_in_day_by_month)

            ### double click download PDF by month
            self.ui.backup_by_month.doubleClicked.connect(self.export_month_to_pdf)

            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > main tab3 backup : ' + str(e))
        finally:
            pass
    
    ###############################
    # show_total_in_day_by_month
    ###############################
    def show_total_in_day_by_month(self):
        try:
            self.data  = self.ui.backup_by_month.currentItem()
            self.data1 = self.data.text(0)
            self.data2 = self.data1.split('-')
            self.data3 = self.data2[0] + '_' + self.data2[1]

            ### clear
            self.ui.backup_by_month_day.clear()

            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr = self.conn.cursor()
            self.sql = "select r_day , count(*) from {0} group by r_day order by r_day asc".format(self.data3)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.backup_by_month_day.setHeaderLabels(['日期','總筆數'])
            self.ui.backup_by_month_day.setColumnWidth(0 , 150)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.backup_by_month_day)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]) + ' 筆記錄')

            ### double click download PDF by day
            self.ui.backup_by_month_day.doubleClicked.connect(self.export_day_to_pdf)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > show_total_in_day_by_month : ' + str(e))
        finally:
            pass

    ########################
    # file_detail_content
    ########################
    def file_detail_content(self , item):
        try:
            self.data = item.text().split(',')
            self.date = self.data[0]
            # 去掉尾部空白
            self.date = self.date.rstrip()

            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr = self.conn.cursor()
            self.sql = "select r_time from medicine where r_day='{0}' order by r_time desc limit 0,1".format(self.date)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchone()
            self.conn.commit()
            # show download first record
            self.ui.download_last_record.setText('Last record : ' + str(self.res[0]))
            self.conn.close()

            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            self.sql2 = "select r_time from medicine where r_day='{0}' order by r_time asc limit 0,1".format(self.date)
            self.curr2.execute(self.sql2)
            self.res2 = self.curr2.fetchone()
            self.conn2.commit()
            # show download first record
            self.ui.downloa_first_record.setText('First record : ' + str(self.res2[0]))
            self.conn2.close()


        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > file detail content : ' + str(e))
        finally:
            pass

    ##############################
    # stop_timing_read_cb_value
    ##############################
    def stop_timing_read_cb_value(self):
        try:
            # disable and enable btn
            self.ui.btn_start_monitor_i6.setEnabled(True)
            self.ui.btn_stop_monitor_i6.setDisabled(True)

            #QMessageBox.information(self , 'Msg' , 'stop per 5 sec realtime value')
            #self.ui.statusbar.showMessage('stop per 5 sec realtime value')

            # stop per 5 sec read cb value
            self.timer.stop()
            self.timer2.stop()
            self.timer_rtm_sensor.stop()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '<<< Error >>> stop per 5 sec timing realtime value : ' + str(e))
        finally:
            pass

    #########################
    # timing_read_i6_value
    #########################
    def timing_read_i6_value(self):
        try:
            # disable and enable btn
            self.ui.btn_start_monitor_i6.setDisabled(True)
            self.ui.btn_stop_monitor_i6.setEnabled(True)

            #QMessageBox.information(self , 'Msg' , 'start I6 per 5 sec realtime value')
            #self.ui.statusbar.showMessage('start I6 per 5 sec realtime value')

            # start per 5 sec read cb value
            self.timer2 = QTimer()
            self.timer2.timeout.connect(self.main_tab5_monitor_i6_2_thread_start)
            self.timer2.start(10000)

            

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '<<< Error >>> start get I6 per 5 sec timing realtime value : ' + str(e))
        finally:
            pass        

    #########################
    # timing_read_cb_value
    #########################
    def timing_read_cb_value(self):
        try:
            
            ### disable and enable btn
            self.ui.btn_start_monitor_i6.setDisabled(True)
            self.ui.btn_stop_monitor_i6.setEnabled(True)

            ### start per 5 sec read cb value
            self.timer = QTimer()
            self.timer.timeout.connect(self.main_tab5_monitor_i6_thread_start)
            self.timer.start(10000)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '<<< Error >>> start get CB per 5 sec timing realtime value : ' + str(e))
        finally:
            pass

    def main_tab5_monitor_i6_2_thread_start(self):
        
        # status bar
        #self.ui.statusbar.showMessage('realtime monitor I6 page')
        try:
            
            ### thread wait
            self.host_cb.wait()
            
            ### realtime monitor I6-2 sensor 
            #self.ui.statusbar.showMessage('realtime monitor I6-2 sensor')

            ### thread    
            self.host_i6_2 = QThread()
            self.host_i6_2.run = self.main_tab5_monitor_i6_2_start
            self.host_i6_2.start()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '<Error> main_tab5_monitor_i6_2_thread_start : ' + str(e))
        finally:
            pass

    ######################################
    # main_tab5_monitor_i6_thread_start
    ######################################
    def main_tab5_monitor_i6_thread_start(self):
        try:
            ### realtime monitor I6-1 sensor 
            self.ui.realtime_statusbar.setText(str('啟動即時監控 I6 - 1 偵測器'))
            
            ### Thread 
            self.host_cb = QThread()
            self.host_cb.run = self.main_tab5_monitor_i6_start
            self.host_cb.start() 

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > main_tab5_monitor_i6_thread_start : ' + str(e))
        finally:
            pass

    #################################
    # main_tab5_monitor_i6_2_start
    #################################
    def main_tab5_monitor_i6_2_start(self):
        
        try:
            # modbusTCP
            self.cb = ModbusClient(host=i6_tcp_connect['ip'],port=i6_tcp_connect['port'],unit_id=i6_tcp_connect['id'],auto_open=True,auto_close=True,debug=False)
            #self.cb = ModbusClient(host='61.220.205.3',port=502,auto_open=True,auto_close=True,debug=False)

            # record time
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y-%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

            ### realtime monitor I6 - 2 sensor 
            self.ui.realtime_i6_2_statusbar.setText(str(self.r_time) + ' , ' + str('啟動即時監控 I6 - 2 偵測器'))

            # read register value
            try:
                # 溫度
                self.cb_val1 = self.cb.read_input_registers(int(i6_tcp_sensor['temp'],16),1)
                # 濕度
                self.cb_val2 = self.cb.read_input_registers(int(i6_tcp_sensor['rh'],16),1)
                # co2
                self.cb_val3 = self.cb.read_input_registers(int(i6_tcp_sensor['co2'],16),1)
                # PM2.5
                self.cb_val4 = self.cb.read_input_registers(int(i6_tcp_sensor['pm2.5'],16),1)
                # HCHO
                self.cb_val5 = self.cb.read_input_registers(int(i6_tcp_sensor['hcho'],16),1)

                # realtime all value list
                self.ui.realtime_monitor_i6_list_2.addItem(self.r_time)
                self.ui.realtime_monitor_i6_list_2.addItem('TEMP : ' + str(self.cb_val1[0]/10) + ' °C , RH : ' + str(self.cb_val2[0]/10) + ' ％ , CO2 : ' + str(self.cb_val3[0]/10) + ' ppm , PM2.5 : ' + str(self.cb_val4[0]/10) + ' ug/m3 , HCHO : ' + str(self.cb_val5[0]/10) + ' ppm')
                
                # realtime now value
                self.ui.monitor_now_time_2.setText(self.r_time)
                self.ui.monitor_item1_2.setText('TEMP : ' + str(self.cb_val1[0]/10) + ' °C')
                self.ui.monitor_item2_2.setText('RH : ' + str(self.cb_val2[0]/10) + ' %')
                self.ui.monitor_item3_2.setText('CO2 : ' + str(self.cb_val3[0]/10) + ' ppm')
                self.ui.monitor_item4_2.setText('PM2.5 : ' + str(self.cb_val4[0]/10) + ' ug/m3')
                self.ui.monitor_item5_2.setText('HCHO : ' + str(self.cb_val5[0]/10) + ' ppm')

                # write to file & write to MySQL
                self.add_content = self.r_time + ' , modbusTCP , I6 - TEMP : ' + str(self.cb_val1[0]/10) + ' °C , RH : ' + str(self.cb_val2[0]/10) + ' ％ ,  CO2 : ' + str(self.cb_val3[0]/10) + ' ppm , PM2.5 : ' + str(self.cb_val4[0]/10) + ' ug/m3 , HCHO : ' + str(self.cb_val5[0]/10) + ' ppm'
                self.cb_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , 'modbusTCP' ,'I6', 'TEMP , RH , CO2 , PM2.5 , HCHO ' , self.cb_val1[0]/10 , self.cb_val2[0]/10 , self.cb_val3[0]/10 , self.cb_val4[0]/10 , self.cb_val5[0]/10 ,  'ok')    

            except Exception as e:
                # read register fail write to file and write to MySQL
                self.add_content = self.r_time + ' , modbusTCP , I6 - TEMP : ' + str(0) + ' °C , RH : ' + str(0) + ' ％ ,  CO2 : ' + str(0) + ' ppm , PM2.5 : ' + str(0) + ' ug/m3 , HCHO : ' + str(0) + ' ppm'
                self.cb_read_failed_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , 'modbusTCP' , 'I6' , 'TEMP , RH , CO2 , PM2.5 , HCHO ' , str(0),str(0),str(0),str(0),str(0) ,  'failed')    
                QMessageBox.information(self , 'Msg' , 'main_tab5_monitor_i6_2_start ModbusTCP read register failed : ' + str(e))

        except Exception as e:
            # read register fail write to file and write to MySQL
            self.add_content = self.r_time + ' , modbusTCP , I6 - TEMP : ' + str(0) + ' °C , RH : ' + str(0) + ' ％ ,  CO2 : ' + str(0) + ' ppm , PM2.5 : ' + str(0) + ' ug/m3 , HCHO : ' + str(0) + ' ppm'
            self.cb_read_failed_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , 'modbusTCP' , 'I6' , 'TEMP , RH , CO2 , PM2.5 , HCHO ' , str(0),str(0),str(0),str(0),str(0) ,  'failed')    
            QMessageBox.information(self , 'Msg' , 'main_tab5_monitor_i6_2_start connect failed : ' + str(e))

    def main_tab5_monitor_i6_thread_start(self):
        try:
            self.host_cb = QThread()
            self.host_cb.run = self.main_tab5_monitor_i6_start
            self.host_cb.start() 
        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > main_tab5_monitor_i6_thread_start : ' + str(e))
        finally:
            pass
    

    ###############################
    # main_tab5_monitor_i6_start
    ###############################
    def main_tab5_monitor_i6_start(self):

        try:
            ### modbusTCP
            self.cb = ModbusClient(host=i6_tcp_connect['ip'],port=i6_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

            ### record time
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y-%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

            ### realtime monitor I6 - 1 sensor 
            self.ui.realtime_i6_1_statusbar.setText(str(self.r_time) + ' , ' + str('啟動即時監控 I6 - 1 偵測器'))

            ### read register value
            try:
                # PM2.5
                self.cb_val6 = self.cb.read_input_registers(int(i6_tcp_sensor['pm2.5'],16),1)
                # PM1.0
                self.cb_val7 = self.cb.read_input_registers(int(i6_tcp_sensor['pm1.0'],16),1)
                # 噪音
                self.cb_val8 = self.cb.read_input_registers(int(i6_tcp_sensor['noise'],16),1)

                # realtime all value list
                self.ui.realtime_monitor_i6_list.addItem(self.r_time)
                self.ui.realtime_monitor_i6_list.addItem('PM2.5 : ' + str(self.cb_val6[0]/10) + ' ug/m3 , PM1.0 : ' + str(self.cb_val7[0]/10) + ' ug/m3 , NOISE : ' + str(self.cb_val8[0]/10) + ' dB')
                
                # realtime now value
                self.ui.monitor_now_time.setText(self.r_time)
                self.ui.monitor_item1.setText('PM2.5 : ' + str(self.cb_val6[0]/10) + ' ug/m3')
                self.ui.monitor_item2.setText('PM1.0 : ' + str(self.cb_val7[0]/10) + ' ug/m3')
                self.ui.monitor_item3.setText('NOISE : ' + str(self.cb_val8[0]/10) + ' dB')

                # write to file & write to MySQL
                self.add_content = self.r_time + ' , modbusTCP , CB-PM2.5 : ' + str(self.cb_val6[0]/10) + ' μg/m3 , PM1.0 : ' + str(self.cb_val7[0]/10) + ' μg/m3 ,  NOISE : ' + str(self.cb_val8[0]/10) + ' dB \n'
                self.cb_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , 'modbusTCP' , 'CB' , 'PM2.5 , PM1.0 , NOISE ' , self.cb_val6[0]/10 , self.cb_val7[0]/10 , self.cb_val8[0]/10 , 0 , 0 ,  'ok')    

            except Exception as e:
                # read register fail write to file and write to MySQL
                self.add_content = self.r_time + ' , modbusTCP , CB-PM2.5 : ' + str(0) + ' μg/m3 , PM1.0 : ' + str(0) + ' μg/m3 ,  NOISE : ' + str(0) + ' dB \n'
                self.cb_read_failed_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , 'modbusTCP' , 'CB' , 'PM2.5 , PM1.0 , NOISE ' , str(0) , str(0) , str(0) , str(0) , str(0) ,  'failed')    
                QMessageBox.information(self , 'Msg' , 'ModbusTCP read register failed : ' + str(e))

        except Exception as e:
            # read register fail write to file and write to MySQL
            self.add_content = self.r_time + ' , modbusTCP , CB-PM2.5 : ' + str(0) + ' μg/m3 , PM1.0 : ' + str(0) + ' μg/m3 ,  NOISE : ' + str(0) + ' dB \n'
            self.cb_read_failed_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , 'modbusTCP' , 'CB' , 'PM2.5 , PM1.0 , NOISE ' , str(0) , str(0) , str(0) , str(0) , str(0) ,  'failed')    
            QMessageBox.information(self , 'Msg' , 'ModbusTCP connect failed : ' + str(e))
    
    ###############################
    # CB read failed insert file
    ###############################
    def cb_read_failed_insert_file(self,add_content , r_time , r_year , r_month , r_day , protocol , kind , content , val1 , val2 , val3 , val4 , val5 , status):
        try:
            # write to file
            #self.add = open('/var/www/html/plc_web/control/modbusTCP_record.txt','a')
            #self.add.write(add_content)
            #self.add.close()

            # write to MySQL
            self.r_time    = r_time
            self.r_year    = r_year
            self.r_month   = r_month
            self.r_day     = r_day
            self.kind      = kind 
            self.content   = content
            self.protocol  = protocol
            self.val1      = 0
            self.val2      = 0
            self.val3      = 0
            self.val4      = 0
            self.val5      = 0
            self.status    = status

            ### create table by month
            self.data = self.r_month.split('-')
            self.b_month = self.data[0]+'_'+self.data[1]

            ### insert into MySQL by this month
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()

            try:
                self.build_sql = "create table {0}(no int not null primary key AUTO_INCREMENT,r_time datetime null,r_year varchar(100) null,r_month varchar(100) null,r_day varchar(100) null,s_kind varchar(200) null,s_content varchar(200) null,s_protocol varchar(200) null,val_1 varchar(200) null,val_2 varchar(200) null,val_3 varchar(200) null,val_4 varchar(200) null,val_5 varchar(200) null,r_status varchar(50) null)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci".format(self.b_month)
                self.curr2.execute(self.build_sql)
                self.conn2.commit()
                self.conn2.close()
            except Exception as e:
                self.sql2 = "insert into {0}(r_time,r_year,r_month,r_day,s_protocol,s_kind,s_content,val_1,val_2,val_3,val_4,val_5,r_status) value('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')".format(self.b_month , self.r_time , self.r_year , self.r_month , self.r_day , self.protocol , self.kind , self.content , self.val1 , self.val2 , self.val3 , self.val4 , self.val5 , self.status)
                self.curr2.execute(self.sql2)
                self.conn2.commit()
                self.conn2.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > CB read failed insert file : ' + str(e))
        finally:
            pass

    ###################
    # CB insert file
    ###################
    def cb_insert_file(self,add_content , r_time , r_year , r_month , r_day , protocol , kind , content , val1 , val2 , val3 , val4 , val5 , status):
        try:
            # write to file
            #self.add = open('/var/www/html/plc_web/control/modbusTCP_record.txt','a')
            #self.add.write(add_content)
            #self.add.close()

            ### write to MySQL
            self.r_time    = r_time
            self.r_year    = r_year
            self.r_month   = r_month
            self.r_day     = r_day
            self.kind      = kind 
            self.content   = content 
            self.protocol  = protocol
            self.val1      = val1
            self.val2      = val2
            self.val3      = val3
            self.val4      = val4
            self.val5      = val5
            self.status    = status

            ### create table by month
            self.data = self.r_month.split('-')
            self.b_month = self.data[0]+'_'+self.data[1]

            ### insert into MySQL by this month
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()

            try:
                self.build_sql = "create table {0}(no int not null primary key AUTO_INCREMENT,r_time datetime null,r_year varchar(100) null,r_month varchar(100) null,r_day varchar(100) null,s_kind varchar(200) null,s_content varchar(200) null,s_protocol varchar(200) null,val_1 varchar(200) null,val_2 varchar(200) null,val_3 varchar(200) null,val_4 varchar(200) null,val_5 varchar(200) null,r_status varchar(50) null)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci".format(self.b_month)
                self.curr2.execute(self.build_sql)
                self.conn2.commit()
                self.conn2.close()
            except Exception as e:
                self.sql2 = "insert into {0}(r_time,r_year,r_month,r_day,s_protocol,s_kind,s_content,val_1,val_2,val_3,val_4,val_5,r_status) value('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')".format(self.b_month , self.r_time , self.r_year , self.r_month , self.r_day , self.protocol , self.kind , self.content , self.val1 , self.val2 , self.val3 , self.val4 , self.val5 , self.status)
                self.curr2.execute(self.sql2)
                self.conn2.commit()
                self.conn2.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > CB insert file : ' + str(e))
        finally:
            pass
    
    ########################
    # export_month_to_pdf
    ########################
    def export_month_to_pdf(self):
        try:
            ### variable
            self.data  = self.ui.backup_by_month.currentItem()
            self.data1 = self.data.text(0)
            self.data2 = self.data1.split('-')
            self.data3 = self.data2[0] + '_' + self.data2[1]

            ### 去掉後面空白
            self.data3 = self.data3.strip()

            ### record time
            self.r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            
            try:
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
                self.curr = self.conn.cursor()
                self.sql  = "select * from {0} where r_status='ok' order by r_time desc".format(self.data3)
                self.curr.execute(self.sql)
                self.res  = self.curr.fetchall()
                
                ### convert PDF
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial',size=10)

                for val in self.res:
                    pdf.cell(200 , 10 , txt=str(val[1]).encode('utf8').decode('latin1')+' , '+str(val[5]).encode('utf8').decode('latin1')+' , '+str(val[13]).encode('utf-8').decode('latin1')+' , '+str(val[6]).encode('utf8').decode('latin1')+' , '+str(val[7]).encode('utf8').decode('latin1')+' , '+str(val[8]).encode('utf8').decode('latin1')+' , '+str(val[9]).encode('utf8').decode('latin1')+' , '+str(val[10]).encode('utf8').decode('latin1')+' , '+str(val[11]).encode('utf8').decode('latin1') , ln=1 , align='left')
                
                ### month pdf export path
                pdf.output(pdf_path['windows_pdf_month_path'] + self.data3 + '.pdf')
                
                ### backup record
                self.sql2 = "insert into backup_record(r_time,backup_time) value('{0}','{1}')".format(self.r_time , self.data3)
                self.res2 = self.curr.execute(self.sql2)
                self.conn.commit()

                if self.res2:
                    self.ui.reload_final_record_by_month.setText(self.data3 + '.pdf , 下載完成。')

                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , str('< Error > export month to pdf backup record : ' + e))
            finally:
                pass

        except Exception as e:
            QMessageBox.information(self , 'Msg' , str('< Error > export month to pdf : ' + e))
        finally:
            pass
    
    ######################
    # export_day_to_pdf
    ######################
    def export_day_to_pdf(self):
        try:
            ### variable
            self.data  = self.ui.backup_by_month_day.currentItem()
            self.data1 = self.data.text(0)
            self.data2 = self.data1.split('-')
            self.data3 = self.data2[0] + '_' + self.data2[1]
            self.data4 = self.data1 

            ### 去掉後面空白
            self.data3 = self.data3.strip()
            self.data4 = self.data4.strip()

            ### record time
            self.r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            
            try:
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
                self.curr = self.conn.cursor()
                self.sql  = "select * from {0} where r_day='{1}' and r_status='ok' order by r_time asc".format(self.data3 , self.data4)
                self.curr.execute(self.sql)
                self.res  = self.curr.fetchall()
                
                ### convert PDF
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial',size=10)

                for val in self.res:
                    pdf.cell(200 , 10 , txt=str(val[1]).encode('utf8').decode('latin1')+' , '+str(val[5]).encode('utf8').decode('latin1')+' , '+str(val[13]).encode('utf-8').decode('latin1')+' , '+str(val[6]).encode('utf8').decode('latin1')+' , '+str(val[7]).encode('utf8').decode('latin1')+' , '+str(val[8]).encode('utf8').decode('latin1')+' , '+str(val[9]).encode('utf8').decode('latin1')+' , '+str(val[10]).encode('utf8').decode('latin1')+' , '+str(val[11]).encode('utf8').decode('latin1') , ln=1 , align='left')
                
                ### day pdf export path
                pdf.output(pdf_path['windows_pdf_day_path'] + self.data4 + '.pdf')
                
                ### backup record
                self.sql2 = "insert into backup_record(r_time,backup_time) value('{0}','{1}')".format(self.r_time , self.data4)
                self.res2 = self.curr.execute(self.sql2)
                self.conn.commit()

                if self.res2:
                    self.ui.reload_final_record_by_month.setText(self.data4 + '.pdf , 下載完成。')

                self.conn.close()

            except Exception as e:
                QMessageBox.information(self , 'Msg' , str('< Error > export day to pdf backup record : ' + e))
            finally:
                pass

        except Exception as e:
            QMessageBox.information(self , 'Msg' , str('< Error > export day to pdf : ' + e))
        finally:
            pass
        
    
    ############################
    # show_day_total_by_month
    ############################
    def show_day_total_by_month(self,item):
        
        ### clear
        self.ui.backup_by_month_day.clear()

        ### variable
        self.data = item.text().split(',')
        self.data2 = self.data[0].split('-')
        self.data3 = self.data2[0]+'_'+self.data2[1]
        self.month = self.data3
        
        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr = self.conn.cursor()
            self.sql = "select r_day , count(*) from {0} group by r_day".format(self.month)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()
            self.conn.commit()

            for val in self.res:
                self.ui.backup_by_month_day.addItem(str(val[0]) + ' , 共 ' + str(val[1]) + ' 筆')
            
            ### export year PDF and backup record
            #self.ui.backup_by_year.itemDoubleClicked.connect(self.export_year_to_pdf)

            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > main_tab2_backup_by_year : ' + str(e))    
        finally:
            pass

    ###################
    # detail_account
    ###################
    def detail_account(self , item):
        
        # variable
        self.val = item.text().split(',')
        self.user = self.val[1]
        # 去掉前空白
        self.user = self.user.lstrip()

        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr = self.conn.cursor()
            
            ### account status
            self.sql = "select r_time , a_user , a_pwd , a_lv , a_status from account where a_user='{0}'".format(self.user)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()
            
            for val in self.res:
                self.ui.a_r_time.setText('Create time : ' + str(val[0]))
                self.ui.a_user.setText('Username : ' + str(val[1]))
                self.ui.a_pwd.setText('Password : ' + str(val[2]))
                
                ### check account status run or stop
                if val[4] == 'stop':
                    self.ui.a_status.setStyleSheet("color:red")
                    self.ui.a_status.setText('Status : ' + str(val[4]))
                else:
                    self.ui.a_status.setStyleSheet("color:green")
                    self.ui.a_status.setText('Status : ' + str(val[4]))

            ### login out record
            self.sql2 = "select login_time from login_out_record where a_user='{0}' order by login_time desc limit 0,20".format(self.user)
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()

            # clear account login list
            self.ui.account_login_record.clear()
            
            for val2 in self.res2:
                self.ui.account_login_record.addItem(str(val2[0]))
            
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > detail account : ' + str(e))
        finally:
            pass
    
    ###################
    # delete_account
    ###################
    def delete_account(self , item):
        
        # variable
        self.val = item.text().split(',')
        self.user = self.val[1]
        # 去掉前空白
        self.user = self.user.lstrip()
        
        self.ask = QMessageBox.question(self , 'Msg' , '刪除帳號 : ' + self.user + ' ?' , QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if self.ask == QMessageBox.StandardButton.Yes:

            try:
                # load account data
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
                self.curr = self.conn.cursor()
                self.sql = "update account set a_status='stop' where a_user='{0}'".format(self.user)
                self.res = self.curr.execute(self.sql)
                self.conn.commit()
            
                #if self.res:
                    ### reload main tab1 account list
                    #self.main_tab1_account()
                    

            except Exception as e:
                self.conn.close()
                QMessageBox.information(self , 'Msg' , '< Error > Delete account : ' + str(e))
            finally:
                pass
        
    #######################
    # submit_del_account
    #######################
    def submit_del_account(self , item):
        
        ### variable
        self.item = item
        QMessageBox.information(self , 'Msg' , 'del : ' + self.item)

    ######################
    # main_tab1_account
    ######################
    def main_tab1_account(self):
        
        ### variables
        global s_user 
        s_user = 'admin'

        ### clear 
        #self.ui.main_account_list.clear()

        try:
            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr = self.conn.cursor()
            self.sql = "select a_lv from account where a_user='{0}'".format(s_user)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchone()

            ### account lv = 1 is admin account
            if self.res[0] == str(1):

                try:
                    self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
                    self.curr = self.conn.cursor()
                    self.sql = "select r_time , a_user , a_pwd , a_status , no from account where a_user!='{0}' order by r_time desc".format(s_user)
                    self.curr.execute(self.sql)
                    self.res = self.curr.fetchall()

                    for val in self.res:
                        self.ui.main_account_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' , ( ' + str(val[3])  + ' )')
                    
                    # click 
                    self.ui.main_account_list.itemClicked.connect(self.detail_account)
                    # double click
                    self.ui.main_account_list.itemDoubleClicked.connect(self.delete_account)

                except Exception as e:
                    QMessageBox.information(self , 'Msg' , '< Error > main_tab1_account : ' + str(e))

            ### account lv = 2 is normal account
            elif self.res[0] == str(2):
                
                try:
                    self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
                    self.curr = self.conn.cursor()
                    self.sql = "select r_time , a_user , a_pwd , a_status , no from account where a_user='{0}' and a_lv='2' and a_status='run' order by r_time desc".format(s_user)
                    self.curr.execute(self.sql)
                    self.res = self.curr.fetchall()

                    for val in self.res:
                        self.ui.main_account_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' , ( ' + str(val[3])  + ' )')
                    
                    # click 
                    self.ui.main_account_list.itemClicked.connect(self.detail_account)
                    # double click 
                    #self.ui.main_account_list.itemDoubleClicked.connect(self.delete_account)

                except Exception as e:
                    print('< Error > main_tab1_account : ' + str(e))

        except Exception as e:
            print('< Error > main_tab1_account : ' + str(e))

        finally:
            self.conn.commit()
            self.conn.close()

    ####################
    # click_main_list
    ####################
    def click_main_list(self , item):
        
        ### variable
        self.val = item.text().split(',')
        self.user = self.val[1]
        
        QMessageBox.information(self , 'Msg' , '< Error > click_main_list : ' + str(self.user))

########################################################################################################################
# main 
########################################################################################################################
def main():
    app  = QApplication(sys.argv)
    main = main_content()
    main.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()