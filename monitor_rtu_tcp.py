#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20230220
# Update   : 20230220
# Function : money manager


import pymysql , time , logging , sqlite3

from pyModbusTCP.client import *
from control.dao import *

########################################################################################################################
#
# main
#
########################################################################################################################
class main():
    
    ########
    # log
    ########
    log_format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%Y-%m-%d %H:%M:%S")

    #########
    # init
    #########
    def __init__(self):
        #while True:
        self.monitor_rtu_tcp()
        #    time.sleep(3)


    ####################
    # monitor_rtu_tcp
    ####################
    def monitor_rtu_tcp(self):
        
        ### record time
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%Y-%m" , time.localtime())
        r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
        
        ##############
        # modbusTCP
        ##############
        lds_i6_tcp = ModbusClient(host=rtu_tcp_converter['ip'],port=rtu_tcp_converter['port'],unit_id=rtu_tcp_converter['id'],auto_open=True,auto_close=True,debug=False)
        
        try:
            ### temp 
            lds_i6_val1 = lds_i6_tcp.read_input_registers(int(rtu_tcp_converter['temp'],16),1)
            ### rh
            lds_i6_val2 = lds_i6_tcp.read_input_registers(int(rtu_tcp_converter['rh'],16),1)
            ### nh3
            lds_i6_val3 = lds_i6_tcp.read_input_registers(int(rtu_tcp_converter['nh3'],16),1)
            ### h2s
            lds_i6_val4 = lds_i6_tcp.read_input_registers(int(rtu_tcp_converter['h2s'],16),1)
            ### pr
            lds_i6_val5 = lds_i6_tcp.read_input_registers(int(rtu_tcp_converter['pr'],16),1)

            logging.info('Temp ' + str(lds_i6_val1[0]/10))
            logging.info('NH3 ' + str(lds_i6_val3[0]/10))
            logging.info('PR ' + str(lds_i6_val5[0]/10))

            ##############
            # insert DB
            ##############
            lds_db = pymysql.connect(host=db_connect['host'] , port=db_connect['port'] , user=db_connect['user'] , passwd=db_connect['pwd'] , database=db_connect['db'] , charset=db_connect['charset'])
            curr = lds_db.cursor()

            try:
                r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                r_year  = time.strftime("%Y" , time.localtime())
                r_month = time.strftime("%Y-%m" , time.localtime())
                db_r_month = time.strftime("%Y_%m" , time.localtime())
                r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                
                try:
                    self.build_sql = "create table {0}(no int not null primary key AUTO_INCREMENT,r_time datetime null,r_year varchar(100) null,r_month varchar(100) null,r_day varchar(100) null,s_kind varchar(200) null,s_content varchar(200) null,s_protocol varchar(200) null,val_1 varchar(200) null,val_2 varchar(200) null,val_3 varchar(200) null,val_4 varchar(200) null,val_5 varchar(200) null,val_6 varchar(200) null,val_7 varchar(200) null,val_8 varchar(200) null,val_9 varchar(200) null,val_10 varchar(200) null,r_status varchar(50) null)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci".format(db_r_month)
                    curr.execute(self.build_sql)
                except Exception as e:
                    sql  = "insert into {0} (r_time , r_year , r_month , r_day , s_kind , s_content , s_protocol , val_1 , val_2 , val_3 , r_status) value('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(db_r_month , r_time , r_year , r_month , r_day , 'RTU-TCP converter' , 'Temp,PR,NH3','modbusTCP' , str(lds_i6_val1[0]/10) , str(lds_i6_val5[0]/10) , str(lds_i6_val3[0]/10) , 'ok')
                    curr.execute(sql)

                ##############
                # write txt
                ##############
                add_content = r_time + ' , RTU-TCP converter , 溫度 ' + str(lds_i6_val1[0]/10) + ' °C , 大氣壓力 ' + str(lds_i6_val5[0]/10) + ' hPa , NH3 ' + str(lds_i6_val3[0]/10) + ' ppm \n'
                try:
                    self.add = open(txt_path['linux_txt_path'] + r_day + '_' + 'rtu_tcp_converter.txt','a')
                    self.add.write(add_content)
                    self.add.close()
                except Exception as e:
                    logging.info("< Error > write txt : " + str(e))
                finally:
                    pass

                print('----------------------------------------------------------------------------------------------')
                print('RTU-TCP converter realtime monitor : ')
                print("\t\t\t\t RTU-TCP converter realtime monitor successful.")
                print('----------------------------------------------------------------------------------------------')
            
            except Exception as e:
                logging.info("< Error > RTU-TCP converter insert DB : " + str(e))
            finally:
                lds_db.commit()
                lds_db.close()                                                                                                                                                                                                                     
            

        except Exception as e:
            logging.info("< Error > monitor_rtu_tcp : " + str(e))
        finally:
            lds_i6_tcp.close()
            
########################################################################################################################
#
# start
#
########################################################################################################################
if __name__ == "__main__":
    start = main()

