#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20221116
# Update   : 20221201
# Function : 大塚製藥 get I6 sensor value


import sys , time , pymysql , minimalmodbus , re
from pyModbusTCP.client import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from fpdf import *

from control.dao import * 
from gui.ui_login import *
from gui.ui_login_2 import *
from gui.ui_main import *
from gui.ui_main_2 import *
from gui.ui_main_3 import *


##################################################################################################################
# main_content
##################################################################################################################
class main_content(QMainWindow):
    #########
    # init
    #########
    def __init__(self , parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.main_init()
    
    ##############
    # main_init
    ##############
    def main_init(self):
        
        ####################
        # tab 1 - account
        ####################
        self.main_tab1_account()

        #######################
        # tab 2 - monitor I6
        #######################
        self.ui.btn_stop_monitor_i6.setDisabled(True)
        ### start realtime monitor I6-1
        self.ui.btn_start_monitor_i6.clicked.connect(self.start_cmd_realtime_main_tab3_backup)
        ### stop realtime monitor I6-1 and I6-2
        self.ui.btn_stop_monitor_i6.clicked.connect(self.stop_cmd_realtime_main_tab3_backup)
        ### show I6 - 1 realtime monitor chart
        

        ####################################
        # tab 3 - backup by month and day
        ####################################
        ### load backup data 
        self.gui_realtime_main_tab3_backup()
        ### reload backup data
        self.ui.btn_reoad_by_month.clicked.connect(self.reload_main_tab3_backup)


    def reload_main_tab3_backup(self):
        #### record time
        self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        self.ui.reload_final_record_by_month.setText(self.r_time)
        
        ### clear 
        self.ui.backup_by_month.clear()

        ### reload by month
        self.gui_realtime_main_tab3_backup()

    def stop_cmd_realtime_main_tab3_backup(self):
        try:
            ### disable and enable btn
            self.ui.btn_start_monitor_i6.setEnabled(True)
            self.ui.btn_stop_monitor_i6.setEnabled(False)

            ### stop QTimer    
            self.start_cmd.stop()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > stop_cmd_realtime_main_tab3_backup : ' + str(e))
        finally:
            pass

    def start_cmd_realtime_main_tab3_backup(self):
        try:
            ### disable and enable btn
            self.ui.btn_start_monitor_i6.setEnabled(False)
            self.ui.btn_stop_monitor_i6.setEnabled(True)

            ### start QTimer
            self.start_cmd = QTimer()
            self.start_cmd.timeout.connect(self.cmd_realtime_main_tab3_backup)
            self.start_cmd.start(60000)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > start_cmd_realtime_main_tab3_backup : ' + str(e))
        finally:
            pass

    def cmd_realtime_main_tab3_backup(self):
        try:
            ### record time
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime()) 
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y_%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr = self.conn.cursor()
            
            ### i6-1
            self.i6_1_sql = "select r_time , val_1 , val_2 , val_3 , val_4 , val_5 from {0} where r_day='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.r_month , self.r_day , 'animals-CW9')
            self.curr.execute(self.i6_1_sql)
            self.res1 = self.curr.fetchall()
            
            for val in self.res1:
                self.ui.monitor_now_time.setText(str(val[0]))
                self.ui.monitor_item1.setText('TEMP : ' + str(val[1]) + ' °C')
                self.ui.monitor_item2.setText('RH : ' + str(val[2]) + ' %')
                self.ui.monitor_item3.setText('PR : ' + str(val[3]) + ' ppm')
                self.ui.monitor_item4.setText('NH3 : ' + str(val[4]) + ' ug/m3')
                self.ui.monitor_item5.setText('H2S : ' + str(val[5]) + ' ppm')

                self.ui.realtime_monitor_i6_list.addItem(str(val[0]))
                self.ui.realtime_monitor_i6_list.addItem('TEMP : ' + str(val[1]) + ' °C , RH :' + str(val[2]) + ' % , PR : ' + str(val[3]) + ' hPa , NH3 : ' + str(val[4]) + ' ppm , H2S : ' + str(val[5]) + ' ppm')

            ### i6-2
            self.i6_2_sql = "select r_time , val_1 , val_2 , val_3 , val_4 , val_5 from {0} where r_day='{1}' and s_kind='{2}' order by r_time desc limit 0,1".format(self.r_month , self.r_day , 'iAQS-1')
            self.curr.execute(self.i6_2_sql)
            self.res2 = self.curr.fetchall()
            
            for val in self.res2:
                self.ui.monitor_now_time_2.setText(str(val[0]))
                self.ui.monitor_item1_2.setText('TEMP : ' + str(val[1]) + ' °C')
                self.ui.monitor_item2_2.setText('RH : ' + str(val[2]) + ' %')

                self.ui.realtime_monitor_i6_list_2.addItem(str(val[0]))
                self.ui.realtime_monitor_i6_list_2.addItem('TEMP : ' + str(val[1]) + ' °C , RH :' + str(val[2]) + ' %')

            self.conn.commit()
            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > cmd realtime main tab3 backup : ' + str(e))
        finally:
            pass
    
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
                
                if self.data2.isdigit():
                    self.data3 = self.data.split('_')
                    self.by_month = self.data3[0] + '-' + self.data3[1]

                    ### total by month
                    self.sql2 = "select count(*) from {0}".format(self.data)
                    self.curr.execute(self.sql2)
                    self.res2 = self.curr.fetchone()

                    self.ui.backup_by_month.addItem(str(self.by_month) + ' , 共 ' + str(self.res2[0]) + ' 筆')

            ### click show total in day by month
            self.ui.backup_by_month.itemClicked.connect(self.show_total_in_day_by_month)

            ### double click download PDF by month
            self.ui.backup_by_month.itemDoubleClicked.connect(self.export_month_to_pdf)

            self.conn.close()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > main tab3 backup : ' + str(e))
        finally:
            pass
    
    def show_total_in_day_by_month(self , item):
        try:
            self.data = item.text().split(',')
            self.data2 = self.data[0].split('-')
            self.data3 = self.data2[0] + '_' + self.data2[1]

            ### clear
            self.ui.backup_by_month_day.clear()

            self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr = self.conn.cursor()
            self.sql = "select r_day , count(*) from {0} group by r_day order by r_day desc".format(self.data3)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            for val in self.res:
                self.ui.backup_by_month_day.addItem(str(val[0]) + ' , 共 ' + str(val[1]) + ' 筆')

            ### double click download PDF by day
            self.ui.backup_by_month_day.itemDoubleClicked.connect(self.export_day_to_pdf)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > show_total_in_day_by_month : ' + str(e))
        finally:
            pass

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

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '<<< Error >>> stop per 5 sec timing realtime value : ' + str(e))
        finally:
            pass

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
    

    def main_tab5_monitor_i6_start(self):

        try:
            ### modbusTCP
            self.cb = ModbusClient(host=i6_tcp_connect2['ip'],port=i6_tcp_connect2['port'],auto_open=True,auto_close=True,debug=False)

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
    
    def export_month_to_pdf(self , item):
        try:
            ### variable
            self.data  = item.text().split(',')
            self.data2 = self.data[0].split('-')
            self.data3 = self.data2[0] + '_' + self.data2[1]

            ### 去掉後面空白
            self.data3 = self.data3.strip()

            ### record time
            self.r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            
            try:
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
                self.curr = self.conn.cursor()
                self.sql = "select * from {0} where r_status='ok' order by r_time desc".format(self.data3)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()
                
                ### convert PDF
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial',size=10)

                for val in self.res:
                    pdf.cell(200 , 10 , txt=str(val[1]).encode('utf8').decode('latin1')+' , '+str(val[5]).encode('utf8').decode('latin1')+' , '+str(val[13]).encode('utf-8').decode('latin1')+' , '+str(val[6]).encode('utf8').decode('latin1')+' , '+str(val[7]).encode('utf8').decode('latin1')+' , '+str(val[8]).encode('utf8').decode('latin1')+' , '+str(val[9]).encode('utf8').decode('latin1')+' , '+str(val[10]).encode('utf8').decode('latin1')+' , '+str(val[11]).encode('utf8').decode('latin1') , ln=1 , align='left')
                
                ### mac path
                pdf.output(pdf_path['mac_pdf_month_path'] + self.data3 + '.pdf')
                ### linux path
                #pdf.output(pdf_path['linux_pdf_month_path'] + self.data3 + '.pdf')
                
                ### backup record
                self.sql2 = "insert into backup_record(r_time,backup_time) value('{0}','{1}')".format(self.r_time , self.data3)
                self.res2 = self.curr.execute(self.sql2)
                self.conn.commit()

                if self.res2:
                    QMessageBox.information(self , 'Msg' , self.data3 + '.pdf backup successful.')    

                self.conn.close()

            except Exception as e:
                
                QMessageBox.information(self , 'Msg' , '< Error > export month to pdf backup record : ' + str(e))
            finally:
                pass

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > export month to pdf : ' + str(e))
        finally:
            pass
    
    def export_day_to_pdf(self , item):
        try:
            ### variable
            self.data  = item.text().split(',')
            self.data2 = self.data[0].split('-')
            self.data3 = self.data2[0] + '_' + self.data2[1]
            self.data4 = self.data[0] 

            ### 去掉後面空白
            self.data3 = self.data3.strip()
            self.data4 = self.data4.strip()

            ### record time
            self.r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            
            try:
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
                self.curr = self.conn.cursor()
                self.sql = "select * from {0} where r_day='{1}' and r_status='ok' order by r_time desc".format(self.data3 , self.data4)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchall()
                
                ### convert PDF
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial',size=10)

                for val in self.res:
                    pdf.cell(200 , 10 , txt=str(val[1]).encode('utf8').decode('latin1')+' , '+str(val[5]).encode('utf8').decode('latin1')+' , '+str(val[13]).encode('utf-8').decode('latin1')+' , '+str(val[6]).encode('utf8').decode('latin1')+' , '+str(val[7]).encode('utf8').decode('latin1')+' , '+str(val[8]).encode('utf8').decode('latin1')+' , '+str(val[9]).encode('utf8').decode('latin1')+' , '+str(val[10]).encode('utf8').decode('latin1')+' , '+str(val[11]).encode('utf8').decode('latin1') , ln=1 , align='left')
                
                ### mac path
                pdf.output(pdf_path['mac_pdf_day_path'] + self.data4 + '.pdf')
                ### linux path
                #pdf.output(pdf_path['linux_pdf_day_path'] + self.data4 + '.pdf')
                
                ### backup record
                self.sql2 = "insert into backup_record(r_time,backup_time) value('{0}','{1}')".format(self.r_time , self.data4)
                self.res2 = self.curr.execute(self.sql2)
                self.conn.commit()

                if self.res2:
                    QMessageBox.information(self , 'Msg' , self.data4 + '.pdf backup successful.')    

                self.conn.close()

            except Exception as e:
                
                QMessageBox.information(self , 'Msg' , '< Error > export day to pdf backup record : ' + str(e))
            finally:
                pass

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > export month to pdf : ' + str(e))
        finally:
            pass
        
    
    
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
            
                if self.res:
                    ### reload main tab1 account list
                    self.main_tab1_account()
                    

            except Exception as e:
                self.conn.close()
                QMessageBox.information(self , 'Msg' , '< Error > Delete account : ' + str(e))
            finally:
                pass
        
    
    def submit_del_account(self , item):
        # variable
        self.item = item
        QMessageBox.information(self , 'Msg' , 'del : ' + self.item)

    def main_tab1_account(self):
        
        # clear 
        self.ui.main_account_list.clear()

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
                    #QMessageBox.information(self , 'Msg' , '< Error > main_tab1_account : ' + str(e))
                    print('< Error > main_tab1_account : ' + str(e))

        except Exception as e:
            #QMessageBox.information(self , 'Msg' , '< Error > main_tab1_account : ' + str(e))
            print('< Error > main_tab1_account : ' + str(e))

        finally:
            self.conn.commit()
            self.conn.close()

    def click_main_list(self , item):
        # variable
        self.val = item.text().split(',')
        self.user = self.val[1]
        
        QMessageBox.information(self , 'Msg' , '< Error > click_main_list : ' + str(self.user))

##################################################################################################################
# login
##################################################################################################################
#class main_login(QMainWindow):
class main_login(QFrame):
    #########
    # init
    #########
    def __init__(self , parent=None):
        super().__init__(parent)
        self.ui = Ui_medicine_login()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.login_init()

    ###############
    # init_login
    ###############
    def login_init(self):
        
        ### status bar
        #self.ui.statusbar.showMessage('Ready')

        ################################
        # btn register account submit
        ################################
        self.ui.btn_register.clicked.connect(self.register_account_submit)

        #####################
        # btn login submit
        #####################
        self.ui.btn_login.clicked.connect(self.login_submit)

        ######################
        # btn cancel submit
        ######################
        self.ui.btn_cancel.clicked.connect(self.cancel_submit)
        
    ##################
    # cancel submit
    ##################
    def cancel_submit(self , event):
        QApplication.closeAllWindows()

    #################
    # login_submit
    #################
    def login_submit(self):
        
        ### user and pwd
        self.user = self.ui.login_user.text()
        self.pwd  = self.ui.login_pwd.text()

        self.ui.login_msg.setText(str(self.user) + ' / ' + str(self.pwd))

        if len(self.user) == 0 or len(self.pwd) == 0:
            self.ui.login_msg.clear()
            self.ui.login_msg.setStyleSheet('color:red;')
            self.ui.login_msg.setText('登入 帳號 or 密碼不能空白 !')
            #QMessageBox.information(self , 'Msg' , '登入 帳號 or 密碼不能空白 !')

        else:
            
            try:
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])    
                self.curr = self.conn.cursor()
                self.sql = "select a_user from account where a_user='{0}' and a_pwd='{1}' and a_status='run'".format(self.user , self.pwd)
                self.curr.execute(self.sql)
                self.res = self.curr.fetchone()
                
                if len(self.res[0]):
                    
                    try:
                        ### login record
                        self.r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                        self.sql2   = "insert into login_out_record(login_time , a_user) value('{0}','{1}')".format(self.r_time , self.res[0])
                        self.curr.execute(self.sql2)

                        ### global variable
                        global s_user
                        s_user = self.res[0]
                        
                        ### login successful    
                        self.ui.login_msg.clear()
                        self.ui.login_msg.setStyleSheet('color:blue;')
                        self.ui.login_msg.setText('登入成功 , 馬上進入主頁')
                        #QMessageBox.information(self , 'Msg' , '登入成功 , 馬上進入主頁')

                        #####################
                        # old main content
                        #####################
                        #self.main = main_content()
                        #self.main.setFixedSize(1024,768)
                        #self.main.show()

                        #####################
                        # new main content
                        #####################
                        self.main = main_content()
                        self.main.show()

                        #####################
                        # close login form
                        #####################
                        self.close()
                        
                    except Exception as e:
                        self.ui.login_msg.setText('< Error > ' + str(e))
                        print('< Error > '+ str(e))
                        #QMessageBox.information(self , 'Msg' , str(e) , QMessageBox.StandardButton.Close)
                    finally:
                        pass

            except Exception as e:
                self.ui.login_msg.clear()
                self.ui.login_msg.setStyleSheet('color:red;')
                self.ui.login_msg.setText('帳號  : ' + self.user + ' 沒有註冊過，無此帳號 !')
                #QMessageBox.information(self , 'Msg' , '帳號  : ' + self.user + ' 沒有註冊過，無此帳號 !')

            finally:
                self.conn.commit()
                self.conn.close()
        
        
                
    
    ############################
    # register_account_submit
    ############################
    def register_account_submit(self):
            ### user and pwd
            self.user = self.ui.login_user.text()
            self.pwd  = self.ui.login_pwd.text()

            if len(self.user) == 0 or len(self.pwd) == 0:
                self.ui.login_msg.clear()
                self.ui.login_msg.setStyleSheet('color:red;')
                self.ui.login_msg.setText('註冊 帳號 or 密碼 不能空白 !')
                QMessageBox.information(self , 'Msg' , '註冊 帳號 or 密碼 不能空白 !')

            else:
                self.conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
                self.curr = self.conn.cursor()

                try:
                    ### check account then add account
                    self.sql = "select a_user from account where a_user='{0}'".format(self.user , self.pwd)
                    self.curr.execute(self.sql)
                    self.res = self.curr.fetchone()

                    if len(self.res[0]) or self.res == 'admin':
                        
                        self.ui.login_msg.clear()
                        self.ui.login_msg.setStyleSheet('color:red')
                        self.ui.login_msg.setText('帳號 : ' + self.user + ' 已被使用 !')
                        #QMessageBox.information(self , 'Msg' , '帳號 : ' + self.user + ' 已被使用 !')
                        

                except Exception as e:

                    ### record time
                    self.r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day = time.strftime("%Y-%m-%d" , time.localtime())

                    ### check account then add account
                    self.sql = "insert into account(r_time , r_year , r_month , r_day , a_user , a_pwd , a_lv , a_status) value('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(self.r_time , self.r_year , self.r_month , self.r_day , self.user , self.pwd , '2' , 'run')
                    self.res = self.curr.execute(self.sql)

                    if self.res:
                        self.ui.login_msg.clear()
                        self.ui.login_msg.setStyleSheet('color:blue')
                        self.ui.login_msg.setText('帳號 : ' + self.user + ' 新增成功.')
                        #QMessageBox.information(self , 'Msg' , '帳號 : ' + self.user + ' 新增成功.')

                finally:
                    self.conn.commit()
                    self.conn.close()


    

#########
# main
#########
def main():
    app = QApplication(sys.argv)
    login = main_login()
    login.show()
    #main = main_content()
    #main.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
    

