#!/usr/bin/python3
# -- coding: utf-8 --**

# Author   : JasonHung
# Date     : 20230220
# Update   : 20230309
# Function : monitor iAeris5 get data from JSON 


import pymysql , time , logging , sqlite3 , json , requests

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
        self.monitor_iaeris5()

    ####################
    # monitor_iaeris5
    ####################
    def monitor_iaeris5(self):
        
        ### record time
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%Y-%m" , time.localtime())
        r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
        
        ##############
        # JSON
        ##############
        iaeris5_url = requests.get(iaeris52['json_url'])
        json_val    = iaeris5_url.text.strip('(').strip(')')
        json_txt    = json.loads(json_val)

        try:
            
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
                    sql  = "insert into {0} (r_time , r_year , r_month , r_day , s_kind , s_content , s_protocol , val_1 , val_2 , val_3 , val_4) value('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(db_r_month , r_time , r_year , r_month , r_day , '維新iAeris5' , 'TEMP,RH,CO2,PM2.5','HTTP-JSON' , json_txt['Temperature'] , json_txt['RH'] , json_txt['CO2'] , json_txt['PM2_5'])
                    curr.execute(sql)
                
                ##############
                # write txt
                ##############
                add_content = str(json_txt['date']) + ' , 維新('+str(json_txt['PID'])+') , 溫度 ' + str(json_txt['Temperature']) + '°C , RH ' + str(json_txt['RH']) + ' % , CO2 ' + str(json_txt['CO2']) + ' ppm , PM2.5 ' + str(json_txt['PM2_5']) + ' ug/m3 \n'
                try:
                    self.add = open(txt_path['linux_txt_path'] + r_day + '_' + 'iAeris5.txt','a')
                    self.add.write(add_content)
                    self.add.close()
                except Exception as e:
                    logging.info("< Error > write txt : " + str(e))
                finally:
                    pass

                print('----------------------------------------------------------------------------------------------')
                print('iAeris 5 realtime monitor : ')
                print("\t\t\t\t iAeris 5 realtime monitor successful.")
                print('----------------------------------------------------------------------------------------------')
                                                                                                                                                                                                                                                
            except Exception as e:
                logging.info("< Error > iAeris 5 insert DB : " + str(e))
            finally:
                lds_db.commit()
                lds_db.close()
            

        except Exception as e:
            logging.info("< Error > start_iAeris5_monitor : " + str(e))
        finally:
            pass

########################################################################################################################
#
# start
#
########################################################################################################################
if __name__ == "__main__":
    start = main()

