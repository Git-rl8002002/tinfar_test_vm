#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20230220
# Update   : 20230309
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
    log_format = "%(asctime)s , %(message)s"
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%H:%M:%S")

    #########
    # init
    #########
    def __init__(self):
        self.monitor_lds()

    ################
    # monitor_lds
    ################
    def monitor_lds(self):
        
        ### record time
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%Y-%m" , time.localtime())
        r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
        
        ##############
        # modbusTCP
        ##############
        ft_i6_tcp = ModbusClient(host=ft_i6['ip'],port=ft_i6['port'],timeout=10.0,auto_open=True,auto_close=True,debug=False)
        
        try:
            ### PH 酸鹼
            ft_i6_val1 = ft_i6_tcp.read_input_registers(int(ft_i6['ph'],16),1)
            ### EC 導電度
            ft_i6_val2 = ft_i6_tcp.read_input_registers(int(ft_i6['ec'],16),1)
            ### watch temp 水溫
            ft_i6_val3 = ft_i6_tcp.read_input_registers(int(ft_i6['temp'],16),1)
            ### mf 瞬間流量
            ft_i6_val4 = ft_i6_tcp.read_input_registers(int(ft_i6['mt'],16),1)
            ### cf 累計流量
            ft_i6_val5 = ft_i6_tcp.read_input_registers(int(ft_i6['cf'],16),1)
            
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
                    sql  = "insert into {0} (r_time , r_year , r_month , r_day , s_kind , s_content , s_protocol , val_1 , val_2 , val_3 , val_4 , val_5 , r_status) value('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')".format(db_r_month , r_time , r_year , r_month , r_day , '富泰-I6' , 'PH,EC,TEMP,MT,CF','modbusTCP' , str(ft_i6_val1[0]/100) , str(ft_i6_val2[0]) , str(ft_i6_val3[0]/10) ,  str(ft_i6_val4[0]/100) ,  str(ft_i6_val5[0]) , 'ok')
                    curr.execute(sql)
                
                ##############
                # write txt
                ##############
                add_content = r_time + ' , 富泰-I6 , 酸鹼度 ' + str(ft_i6_val1[0]/100) + ' pH , 導電度 ' + str(ft_i6_val2[0]) + ' us/cm , 水溫 ' + str(ft_i6_val3[0]/10) + ' °C , 瞬間流量 ' + str(ft_i6_val4[0]/100) + ' M3/H , 累計流量 ' + str(ft_i6_val5[0]) + ' M3\n'
                try:
                    self.add = open(txt_path['linux_txt_path'] + r_day + '_' + 'ft_i6.txt','a')
                    self.add.write(add_content)
                    self.add.close()
                except Exception as e:
                    logging.info("< Error > write txt : " + str(e))
                finally:
                    pass

                print('----------------------------------------------------------------------------------------------')
                print('富泰 I6 realtime monitor : ')
                print("\t\t\t\t lds i6 realtime monitor successful.")
                print('----------------------------------------------------------------------------------------------')
                                                                                                                                                                                                                                                
            except Exception as e:
                logging.info("< Error > ft i6 insert DB : " + str(e))
            finally:
                lds_db.commit()
                lds_db.close()
            

        except Exception as e:
            logging.info("< Error > start_lds_i6_monitor : " + str(e))
        finally:
            pass

########################################################################################################################
#
# start
#
########################################################################################################################
if __name__ == "__main__":
    start = main()

