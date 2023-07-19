#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20221116
# Update   : 20230209
# Version  : 1.1
# Function : Tinfar I6 , CB , IAQS monbudTCP test

import time , pymysql , platform , os , requests , logging , sqlite3 , sys
from pyModbusTCP.client import *
from control.dao import * 
from fpdf import *

###############################################################################################################################################
#
# monitor
#
###############################################################################################################################################
class monitor():
    
    ########
    # log
    ########
    log_format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%H:%M:%S")

    #########
    # init
    #########
    def __init__(self):
        pass

    ######################
    # read sensor value
    ######################
    def sensor(self):
        
        try:
            #########
            # loop
            #########
            #while True:
                
                ###########################
                # Tinfar CB by modbusTCP 
                ###########################
                try:
                    self.i6 = ModbusClient(host=i6_tcp_connect['ip'],port=i6_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = i6_tcp_param['kind']
                    self.s_protocol   = i6_tcp_param['protocol']
                    self.s_position   = i6_tcp_param['position']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(i6_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(i6_tcp_sensor['rh'],16),1)
                    ### 大氣壓力 pr
                    self.i6_val3 = self.i6.read_input_registers(int(i6_tcp_sensor['pr'],16),1)
                    ### 氨氣 nh3
                    self.i6_val4 = self.i6.read_input_registers(int(i6_tcp_sensor['nh3'],16),1)
                    ### 硫化氫 h2s
                    self.i6_val5 = self.i6.read_input_registers(int(i6_tcp_sensor['h2s'],16),1)
                    
                    ### print msg
                    print('\n')
                    
                    logging.info(self.s_kind + ' , ' + self.s_position + ' , Temp : ' + str(self.i6_val1[0]/10) + ' °C , RH : ' + str(self.i6_val2[0]/10) + ' %  , PR : ' + str(self.i6_val3[0]/10) + ' hPa , NH2 : ' + str(self.i6_val4[0]/10) + ' ppm , H2S : ' + str(self.i6_val5[0]/10) + ' ppm.')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temp : ' + str(self.i6_val1[0]/10) + ' °C , RH : ' + str(self.i6_val2[0]/10) + ' % , PR :  ' + str(self.i6_val3[0]/10) + ' hPa , NH3 : ' + str(self.i6_val4[0]/10) + ' ppm , H2S : ' + str(self.i6_val5[0]/10) + ' ppm\n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , self.i6_val3[0]/10 , self.i6_val4[0]/10 , self.i6_val5[0]/10 ,  'ok')    

                    ### write to sqlite 
                    self.insert_sqlite(str(self.i6_val1[0]/10) , str(self.i6_val2[0]/10) , str(self.i6_val3[0]/10) , str(self.i6_val4[0]/10) , str(self.i6_val5[0]/10))

                except Exception as e:
                    logging.info('< Error > CB , ' + self.s_position + ' : ' + str(e) + '\n')
        
        except Exception as e:
            logging.info('< Error > monbusTCP link : ' + str(e))
    
    ###############
    # show_mysql
    ###############
    def show_mysql(self):
        ### variables
        b_month  = time.strftime("%Y_%m" , time.localtime())    
        
        ### insert into MySQL by this month
        conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
        curr = conn.cursor()

        try:
            sql = "select * from {0} where s_kind='CB' order by r_time desc limit 0,100".format(b_month)
            curr.execute(sql)
            res = curr.fetchall()

            for val in res:
                print(str(val[1]) + ' , ' + str(val[5]) + ' , ' + str(val[7]) + ' , ' + str(val[8]) + ' , ' + str(val[9]) + ' , ' + str(val[10]) + ' , ' + str(val[11]) + ' , ' + str(val[12]))

        except Exception as e:
            logging.info("< Error > show_mysql : " + str(e))
        finally:
            conn.commit()
            conn.close()

    ################
    # show_sqlite
    ################
    def show_sqlite(self):

        ### variables
        b_month  = 'm_' + time.strftime("%Y_%m" , time.localtime())

        conn = sqlite3.connect(sqlite_path['linux'])
        curr = conn.cursor()
        try:
            sql = "select * from {0} order by r_time desc limit 0,20".format(b_month)
            curr.execute(sql)
            res = curr.fetchall()

            for val in res:
                print(str(val[1]) + ' , ' + str(val[5]) + ' , ' + str(val[7]) + ' , ' + str(val[8]) + ' , ' + str(val[9]) + ' , ' + str(val[10]) + ' , ' + str(val[11]) + ' , ' + str(val[12]))
                
        except Exception as e:
            logging.info("< Error > show_sqlite : " + str(e))
        finally:
            conn.commit()
            conn.close()

    ##################
    # insert_sqlite
    ##################
    def insert_sqlite(self,val1,val2,val3,val4,val5):
        
        ### variables
        b_month  = 'm_' + time.strftime("%Y_%m" , time.localtime())
        
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%Y-%m" , time.localtime())
        r_day   = time.strftime("%Y-%m-%d" , time.localtime())
        
        
        conn = sqlite3.connect(sqlite_path['linux'])

        curr = conn.cursor()
        curr.execute('VACUUM')

        try:
            sql = "insert into {0}(r_time,r_year,r_month,r_day,s_protocol,s_kind,s_content,val_1,val_2,val_3,val_4,val_5,r_status) values('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')".format(b_month , r_time , r_year , r_month , r_day , 'ModbusTCP' , 'CW9' , 'TEMP,RH,PR,NH3,H2S' , val1 , val2 , val3 , val4 , val5 , 'ok')
            res = curr.execute(sql)

            if res:
                logging.info("insert into sqlite successful.\n")
            else:
                logging.info("insert into sqlite failed\n")

        except Exception as e:
            logging.info("< Error > insert_sqlite : " + str(e))
        finally:
            conn.commit()
            conn.close()

    ##############
    # insert_db
    ##############
    def insert_db(self,add_content , r_time , r_year , r_month , r_day , protocol , kind , content , val1 , val2 , val3 , val4 , val5 , status):
        
        try:
            ##################
            # write to file
            ##################
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y-%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
            self.os_sys  = platform.system()
            
            ### save file path - Linux
            if self.os_sys == 'Linux':
                
                ### check txt document exists
                #self.floderpath = txt_path['linux_txt_path'] + self.r_day
                #try:
                    #os.makedirs(self.floderpath)
                #except FileExistsError:
                try:
                    self.add = open(txt_path['linux_txt_path'] + self.r_day + '_' + kind + '.txt','a')
                    self.add.write(add_content)

                    ### insert into txt
                    logging.info('insert into ' + str(self.r_day) + '.txt successful.')
                except Exception as e:
                    logging.info("< Error > open file : " + str(e))
                finally:
                    self.add.close()

            ###################
            # write to MySQL
            ###################
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
                self.build_sql = "create table {0}(no int not null primary key AUTO_INCREMENT,r_time datetime null,r_year varchar(100) null,r_month varchar(100) null,r_day varchar(100) null,s_kind varchar(200) null,s_content varchar(200) null,s_protocol varchar(200) null,val_1 varchar(200) null,val_2 varchar(200) null,val_3 varchar(200) null,val_4 varchar(200) null,val_5 varchar(200) null,val_6 varchar(200) null,val_7 varchar(200) null,val_8 varchar(200) null,val_9 varchar(200) null,val_10 varchar(200) null,val_11 varchar(200) null,val_12 varchar(200) null,val_13 varchar(200) null,val_14 varchar(200) null,val_15 varchar(200) null,val_16 varchar(200) null,val_17 varchar(200) null,val_18 varchar(200) null,val_19 varchar(200) null,val_20 varchar(200) null,val_21 varchar(200) null,val_22 varchar(200) null,val_23 varchar(200) null,val_24 varchar(200) null,val_25 varchar(200) null,r_status varchar(50) null)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci".format(self.b_month)
                self.curr2.execute(self.build_sql)
            except Exception as e:
                self.sql2 = "insert into {0}(r_time,r_year,r_month,r_day,s_protocol,s_kind,s_content,val_1,val_2,val_3,val_4,val_5,r_status) value('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')".format(self.b_month , self.r_time , self.r_year , self.r_month , self.r_day , self.protocol , self.kind , self.content , self.val1 , self.val2 , self.val3 , self.val4 , self.val5 , self.status)
                self.curr2.execute(self.sql2)
            
            ### insert into database
            logging.info('insert into MySQL successful.')

        except Exception as e:
            logging.info('< Error > insert_db : ' + str(e))
        finally:
            self.conn2.commit()
            self.conn2.close()

###############################################################################################################################################
#
# start
#
###############################################################################################################################################
if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('####################################################################################')
        print('# Tinfar_test_VM')
        print('# usage : ')
        print('#\t\t ./monitor.py        (run monitor CB realtime data')
        print('#\t\t ./monitor.py sqlite (show sqlite data)')
        print('#\t\t ./monitor.py mysql  (show sqlite data)')
        print('####################################################################################')
        realtime = monitor()
        realtime.sensor()
    elif sys.argv[1] == "sqlite":
        realtime = monitor()
        realtime.show_sqlite()
    elif sys.argv[1] == "mysql":
        realtime = monitor()
        realtime.show_mysql()
    