#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20230220ㄊㄊ
# Update   : 20230220
# Function : money manager


import pymysql , time , logging , sqlite3 , requests , json

from pyModbusTCP.client import *
from control.dao import *

#########################################################################################################
#
# 根基營造 JNC Server JSON API
#
#########################################################################################################
class kedge:
    
    ### log 
    log_format = "%(asctime)s %(message)s"
    logging.basicConfig(format=log_format,level=logging.INFO,datefmt="%Y-%m-%d %H:%M:%S")
    
    #########
    # init
    #########
    def __init__(self):
        self.main()
    
    #################
    # add_kedge_db
    #################
    def add_kedge_db(self , position , val1 , val2 , val3 , status):
        
        ### record time
        r_time  = time.strftime("%H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%m" , time.localtime())
        r_day   = time.strftime("%d" , time.localtime()) 
        b_month = time.strftime("%Y_%m" , time.localtime())

        #############
        # kedge DB
        #############
        conn = pymysql.connect(host=kedge_connect['host'] , port=kedge_connect['port'] , user=kedge_connect['user'] , passwd=kedge_connect['pwd'] , database=kedge_connect['db'] , charset=kedge_connect['charset'])
        curr = conn.cursor()

        try:
            b_sql = "create table {0}(no int not null primary key AUTO_INCREMENT,r_time time null,r_year varchar(100) null,r_month varchar(100) null,r_day varchar(100) null,s_kind varchar(200) null,s_content varchar(200) null,s_protocol varchar(200) null,tag_name varchar(200) null,val varchar(200) null,unit varchar(200) null,r_status varchar(50) null)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci".format(b_month)
            curr.execute(b_sql)

        except Exception as e:
            b_sql = "insert into {0}(r_time,r_year,r_month,r_day,s_protocol,s_kind,s_content,tag_name,val,unit,r_status) value('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(b_month , r_time , r_year , r_month , r_day , 'HTTP JSON' , 'CB' , position , val1 , val2 , val3 , status)
            curr.execute(b_sql)
            
        finally:
            conn.commit()
            conn.close()
    
    #########
    # main
    #########
    def main(self):

        #######################
        # Device 1 : 南門市場
        #######################
        d_url_1      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=0&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_1     = requests.get(d_url_1)
        d_r_data_1   = d_data_1.text
        d_data_val_1 = json.loads(d_r_data_1)

        url_1      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=0&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_1     = requests.get(url_1)
        r_data_1   = data_1.text
        data_val_1 = json.loads(r_data_1)

        for val in data_val_1["Device"]:
            logging.info(str(d_data_val_1['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_1['Connect']))
            self.add_kedge_db(d_data_val_1['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_1['Connect'])

        print('\n')
        
        #######################
        # Device 2 : 桃園會展
        #######################
        d_url_2      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=1&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_2     = requests.get(d_url_2)
        d_r_data_2   = d_data_2.text
        d_data_val_2 = json.loads(d_r_data_2)

        url_2      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=1&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_2     = requests.get(url_2)
        r_data_2   = data_2.text
        data_val_2 = json.loads(r_data_2)

        for val in data_val_2["Device"]:
            logging.info(str(d_data_val_2['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_2['Connect']))
            self.add_kedge_db(d_data_val_2['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_2['Connect'])

        print('\n')
        
        #######################
        # Device 3 : 泰山社宅
        #######################
        d_url_3      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=2&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_3     = requests.get(d_url_3)
        d_r_data_3   = d_data_3.text
        d_data_val_3 = json.loads(d_r_data_3)

        url_3      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=2&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_3     = requests.get(url_3)
        r_data_3   = data_3.text
        data_val_3 = json.loads(r_data_3)

        for val in data_val_3["Device"]:
            logging.info(str(d_data_val_3['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_3['Connect']))
            self.add_kedge_db(d_data_val_3['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_3['Connect'])

        print('\n')
        
        #####################
        # Device 4 : 二重埔
        #####################
        d_url_4      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=3&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_4     = requests.get(d_url_4)
        d_r_data_4   = d_data_4.text
        d_data_val_4 = json.loads(d_r_data_4)

        url_4      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=3&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_4     = requests.get(url_4)
        r_data_4   = data_4.text
        data_val_4 = json.loads(r_data_4)

        for val in data_val_4["Device"]:
            logging.info(str(d_data_val_4['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_4['Connect']))
            self.add_kedge_db(d_data_val_4['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_4['Connect'])

        print('\n')
        
        ########################
        # Device 5 : 民權東路案
        ########################
        d_url_5      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=4&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_5     = requests.get(d_url_5)
        d_r_data_5   = d_data_5.text
        d_data_val_5 = json.loads(d_r_data_5)

        url_5      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=4&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_5     = requests.get(url_5)
        r_data_5   = data_5.text
        data_val_5 = json.loads(r_data_5)

        for val in data_val_5["Device"]:
            logging.info(str(d_data_val_5['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_5['Connect']))
            self.add_kedge_db(d_data_val_5['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_5['Connect'])

        print('\n')
        
        #######################
        # Device 6 : 秀朗橋案
        #######################
        d_url_6      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=5&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_6     = requests.get(d_url_6)
        d_r_data_6   = d_data_6.text
        d_data_val_6 = json.loads(d_r_data_6)

        url_6      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=5&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_6     = requests.get(url_6)
        r_data_6   = data_6.text
        data_val_6 = json.loads(r_data_6)

        for val in data_val_6["Device"]:
            logging.info(str(d_data_val_6['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_6['Connect']))
            self.add_kedge_db(d_data_val_6['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_6['Connect'])

        print('\n')

        #####################
        # Device 7 : 裕毛屋
        #####################
        d_url_7      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=6&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_7     = requests.get(d_url_7)
        d_r_data_7   = d_data_7.text
        d_data_val_7 = json.loads(d_r_data_7)

        url_7      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=6&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_7     = requests.get(url_7)
        r_data_7   = data_7.text
        data_val_7 = json.loads(r_data_7)

        for val in data_val_7["Device"]:
            logging.info(str(d_data_val_7['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_7['Connect']))
            self.add_kedge_db(d_data_val_7['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_7['Connect'])

        print('\n')

        #######################
        # Device 8 : 後龍大橋
        #######################
        d_url_8      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=7&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_8     = requests.get(d_url_8)
        d_r_data_8   = d_data_8.text
        d_data_val_8 = json.loads(d_r_data_8)

        url_8      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=7&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_8     = requests.get(url_8)
        r_data_8   = data_8.text
        data_val_8 = json.loads(r_data_8)

        for val in data_val_8["Device"]:
            logging.info(str(d_data_val_8['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_8['Connect']))
            self.add_kedge_db(d_data_val_8['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_8['Connect'])

        print('\n')
        
        ################################
        # Device 9 : 嘉義車站C611世賢南
        ################################
        d_url_9      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=8&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_9     = requests.get(d_url_9)
        d_r_data_9   = d_data_9.text
        d_data_val_9 = json.loads(d_r_data_9)

        url_9      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=8&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_9     = requests.get(url_9)
        r_data_9   = data_9.text
        data_val_9 = json.loads(r_data_9)

        for val in data_val_9["Device"]:
            logging.info(str(d_data_val_9['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_9['Connect']))
            self.add_kedge_db(d_data_val_9['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_9['Connect'])

        print('\n')

        ##################################
        # Device 10 : 嘉義車站C611宏仁女中
        ##################################
        d_url_10      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=9&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_10     = requests.get(d_url_10)
        d_r_data_10   = d_data_10.text
        d_data_val_10 = json.loads(d_r_data_10)

        url_10      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=9&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_10     = requests.get(url_10)
        r_data_10   = data_10.text
        data_val_10 = json.loads(r_data_10)

        for val in data_val_10["Device"]:
            logging.info(str(d_data_val_10['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_10['Connect']))
            self.add_kedge_db(d_data_val_10['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_10['Connect'])

        print('\n')

        ##################################
        # Device 11 : 嘉義車站C612嘉北車站
        ##################################
        d_url_11      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=10&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_11     = requests.get(d_url_11)
        d_r_data_11   = d_data_11.text
        d_data_val_11 = json.loads(d_r_data_11)

        url_11      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=10&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_11     = requests.get(url_11)
        r_data_11   = data_11.text
        data_val_11 = json.loads(r_data_11)

        for val in data_val_11["Device"]:
            logging.info(str(d_data_val_11['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_11['Connect']))
            self.add_kedge_db(d_data_val_11['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_11['Connect'])

        print('\n')
        
        ###############################
        # Device 12 : 嘉義車站C612北興
        ###############################
        d_url_12      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=11&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_12     = requests.get(d_url_12)
        d_r_data_12   = d_data_12.text
        d_data_val_12 = json.loads(d_r_data_12)

        url_12      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=11&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_12     = requests.get(url_12)
        r_data_12   = data_12.text
        data_val_12 = json.loads(r_data_12)

        for val in data_val_12["Device"]:
            logging.info(str(d_data_val_12['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_12['Connect']))
            self.add_kedge_db(d_data_val_12['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_12['Connect'])

        print('\n')
        
        #############################
        # Device 13 : 台南車站一號口
        #############################
        d_url_13      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=12&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_13     = requests.get(d_url_13)
        d_r_data_13   = d_data_13.text
        d_data_val_13 = json.loads(d_r_data_13)

        url_13      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=12&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_13     = requests.get(url_13)
        r_data_13   = data_13.text
        data_val_13 = json.loads(r_data_13)

        for val in data_val_13["Device"]:
            logging.info(str(d_data_val_13['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_13['Connect']))
            self.add_kedge_db(d_data_val_13['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_13['Connect'])

        print('\n')

        #############################
        # Device 14 : 台南車站四號口
        #############################
        d_url_14      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=13&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_14     = requests.get(d_url_14)
        d_r_data_14   = d_data_14.text
        d_data_val_14 = json.loads(d_r_data_14)

        url_14      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=13&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_14     = requests.get(url_14)
        r_data_14   = data_14.text
        data_val_14 = json.loads(r_data_14)

        for val in data_val_14["Device"]:
            logging.info(str(d_data_val_14['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_14['Connect']))
            self.add_kedge_db(d_data_val_14['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_14['Connect'])

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
        lds_i6_tcp = ModbusClient(host=lds_i6['ip'],port=lds_i6['port'],timeout=10.0,auto_open=True,auto_close=True,debug=False)
        
        try:
            ### PH 酸鹼
            lds_i6_val1 = lds_i6_tcp.read_input_registers(int(lds_i6['ph'],16),1)
            ### EC 導電度
            lds_i6_val2 = lds_i6_tcp.read_input_registers(int(lds_i6['ec'],16),1)
            ### watch temp 水溫
            lds_i6_val3 = lds_i6_tcp.read_input_registers(int(lds_i6['temp'],16),1)
            ### mf 瞬間流量
            lds_i6_val4 = lds_i6_tcp.read_input_registers(int(lds_i6['mt'],16),1)
            ### cf 累計流量
            lds_i6_val5 = lds_i6_tcp.read_input_registers(int(lds_i6['cf'],16),1)
            
            
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
                
                sql  = "insert into {0} (r_time , r_year , r_month , r_day , s_kind , s_content , s_protocol , val_1 , val_2 , val_3 , val_4 , val_5) value('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')".format(db_r_month , r_time , r_year , r_month , r_day , '連大興-I6' , 'PH,EC,TEMP,MT,CF','modbusTCP' , str(lds_i6_val1[0]/100) , str(lds_i6_val2[0]) , str(lds_i6_val3[0]/10) ,  str(lds_i6_val4[0]/100) ,  str(lds_i6_val5[0]))
                curr.execute(sql)

                ##############
                # write txt
                ##############
                add_content = r_time + ' , 連大興-I6 , 酸鹼度 ' + str(lds_i6_val1[0]/100) + ' pH , 導電度 ' + str(lds_i6_val2[0]) + ' us/cm , 水溫 ' + str(lds_i6_val3[0]/10) + ' °C , 瞬間流量 ' + str(lds_i6_val4[0]/100) + ' M3/H , 累計流量 ' + str(lds_i6_val5[0]) + ' M3\n'
                try:
                    self.add = open(txt_path['linux_txt_path'] + r_day + '_' + 'lds_i6.txt','a')
                    self.add.write(add_content)
                    self.add.close()
                except Exception as e:
                    logging.info("< Error > write txt : " + str(e))
                finally:
                    pass

                print('----------------------------------------------------------------------------------------------')
                print('連大興 I6 realtime monitor : ')
                print("\t\t\t\t lds i6 realtime monitor successful.")
                print('----------------------------------------------------------------------------------------------')
                                                                                                                                                                                                                                                
            except Exception as e:
                logging.info("< Error > lds i6 insert DB : " + str(e))
            finally:
                lds_db.commit()
                lds_db.close()
            

        except Exception as e:
            logging.info("< Error > start_lds_i6_monitor : " + str(e))
        finally:
            lds_i6_tcp.close()
            
########################################################################################################################
#
# start
#
########################################################################################################################
if __name__ == "__main__":
    start = kedge()

