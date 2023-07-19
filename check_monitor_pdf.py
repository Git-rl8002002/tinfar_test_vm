#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20221116
# Update   : 20230209
# Version  : 1.1
# Function : 大塚製藥 get I6 sensor value

import time , pymysql , platform , os , smtplib , datetime , pysftp as sftp
from pyModbusTCP.client import *
from control.dao import * 
from fpdf import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

########################################################################################################################
#
# monitor 
#
########################################################################################################################
class monitor():
    
    #########
    # init
    #########
    def __init__(self):
        self.send_email()

    ###############
    # send email
    ###############
    def send_email(self):
        
        ### variable
        self.receiver_mail = tinfar_email['jason']
        
        self.otsuka_mail1  = otsuka_email['bill']
        self.otsuka_mail2  = otsuka_email['ray']
        self.otsuka_mail3  = otsuka_email['allen']
        self.otsuka_mail4  = otsuka_email['yihsien']
        self.otsuka_mail5  = otsuka_email['richard']

        ### record time
        self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        self.r_year  = time.strftime("%Y" , time.localtime())
        self.r_month = time.strftime("%Y-%m" , time.localtime())
        self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

        self.backup_day = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        
        self.conver_pdf_day_s1    = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-1.pdf'
        self.conver_pdf_day_s2    = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-2.pdf'
        self.conver_pdf_day_s3    = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-3.pdf'
        self.conver_pdf_day_s4    = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-4.pdf'
        self.conver_pdf_day_s5    = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-5.pdf'
        self.conver_pdf_day_s6    = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-6.pdf'
        self.conver_pdf_day_s7    = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-7.pdf'
        self.conver_pdf_day_s8    = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-8.pdf'
        self.conver_pdf_day_s9    = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-9.pdf'
        self.conver_pdf_day_s10   = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-10.pdf'
        self.conver_pdf_day_s11_1 = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-11-1.pdf'
        self.conver_pdf_day_s11_2 = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-11-2.pdf'
        self.conver_pdf_day_s12   = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-12.pdf'
        self.conver_pdf_day_s13   = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-13.pdf'
        self.conver_pdf_day_s14   = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-14.pdf'
        self.conver_pdf_day_s15_1 = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-15-1.pdf'
        self.conver_pdf_day_s15_2 = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-15-2.pdf'
        self.conver_pdf_day_s15_3 = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-15-3.pdf'
        self.conver_pdf_day_s15_4 = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-15-4.pdf'
        self.conver_pdf_day_s15_5 = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-15-5.pdf'
        self.conver_pdf_day_s15_6 = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-15-6.pdf'
        self.conver_pdf_day_s16   = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-16.pdf'
        self.conver_pdf_day_s17   = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-17.pdf'
        self.conver_pdf_day_s18   = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d") + '_S-18.pdf'
        
        self.lost_date_s1      = self.conver_pdf_day_s1
        self.lost_date_s2      = self.conver_pdf_day_s2
        self.lost_date_s3      = self.conver_pdf_day_s3
        self.lost_date_s4      = self.conver_pdf_day_s4
        self.lost_date_s5      = self.conver_pdf_day_s5
        self.lost_date_s6      = self.conver_pdf_day_s6
        self.lost_date_s7      = self.conver_pdf_day_s7
        self.lost_date_s8      = self.conver_pdf_day_s8
        self.lost_date_s9      = self.conver_pdf_day_s9
        self.lost_date_s10     = self.conver_pdf_day_s10
        self.lost_date_s11_1   = self.conver_pdf_day_s11_1
        self.lost_date_s11_2   = self.conver_pdf_day_s11_2
        self.lost_date_s12     = self.conver_pdf_day_s12
        self.lost_date_s13     = self.conver_pdf_day_s13
        self.lost_date_s14     = self.conver_pdf_day_s14
        self.lost_date_s15_1   = self.conver_pdf_day_s15_1
        self.lost_date_s15_2   = self.conver_pdf_day_s15_2
        self.lost_date_s15_3   = self.conver_pdf_day_s15_3
        self.lost_date_s15_4   = self.conver_pdf_day_s15_4
        self.lost_date_s15_5   = self.conver_pdf_day_s15_5
        self.lost_date_s15_6   = self.conver_pdf_day_s15_6
        self.lost_date_s16     = self.conver_pdf_day_s16
        self.lost_date_s17     = self.conver_pdf_day_s17
        self.lost_date_s18     = self.conver_pdf_day_s18

        print('----------------------------------------------------------------------------------------------')

        ########################
        # check backup PDF S1
        #######################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s1)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S1 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ########################
        # check backup PDF S2
        #######################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s2)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S2 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ########################
        # check backup PDF S3
        #######################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s3)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S3 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ########################
        # check backup PDF S4
        #######################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s4)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S4 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ########################
        # check backup PDF S5
        #######################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s5)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S5 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ########################
        # check backup PDF S6
        #######################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s6)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()

        except Exception as e:
            print('<Error> check backup pdf S6 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ########################
        # check backup PDF S7
        #######################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s7)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S7 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ########################
        # check backup PDF S8
        #######################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s8)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S8 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ########################
        # check backup PDF S9
        #######################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s9)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-9 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ########################
        # check backup PDF S10
        #######################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s10)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-10 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ###########################
        # check backup PDF S11-1
        ###########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s11_1)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-11-1 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ###########################
        # check backup PDF S11-2
        ###########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s11_2)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-11-2 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        #########################
        # check backup PDF S12
        #########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s12)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-12 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        #########################
        # check backup PDF S13
        #########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s13)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-13 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        #########################
        # check backup PDF S14
        #########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s14)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-14 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ###########################
        # check backup PDF S15-1
        ###########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s15_1)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-15-1 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ###########################
        # check backup PDF S15-2
        ###########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s15_2)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-15-2 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ###########################
        # check backup PDF S15-3
        ###########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s15_3)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-15-3 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ###########################
        # check backup PDF S15-4
        ###########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s15_4)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-15-4 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ###########################
        # check backup PDF S15-5
        ###########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s15_5)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-15-5 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        ###########################
        # check backup PDF S15-6
        ###########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s15_6)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-15-6 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        #########################
        # check backup PDF S16
        #########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s16)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-16 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        #########################
        # check backup PDF S17
        #########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s17)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-17 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        #########################
        # check backup PDF S18
        #########################
        try:
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()
            
            self.sql2 = "select backup_time from backup_record where backup_time='{0}' order by no desc limit 0,1".format(self.conver_pdf_day_s18)
            self.curr2.execute(self.sql2)
            self.res = self.curr2.fetchone()
            print(self.r_time + ' : ' + str(self.res[0]) + ' , 已備份到 NAS.')
            
            ### success send email
            #self.success_send_email(self.r_time , self.lost_date_s2 , self.receiver_mail)
            #self.backup_success_s18 = self.conver_pdf_day_s18

            self.conn2.commit()
            self.conn2.close()
            
        except Exception as e:
            print('<Error> check backup pdf S-18 : ' + str(e))
            ### fail send email
            self.fail_send_email(self.r_time , self.lost_date_s1 , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)
        
        print('----------------------------------------------------------------------------------------------')

        #######################
        # success send email
        #######################
        self.success_send_email(self.r_time , self.backup_day , self.receiver_mail , self.otsuka_mail1 , self.otsuka_mail2 , self.otsuka_mail3 , self.otsuka_mail4 , self.otsuka_mail5)

    ####################
    # fail_send_email
    ####################
    def fail_send_email(self , r_time , lost_date , email1 , email2 , email3 , email4 , email5 , email6):
        try:
            ### variable
            self.r_time = r_time
            self.lost_date = lost_date
            
            self.email1 = email1
            self.email2 = email2
            self.email3 = email3
            self.email4 = email4
            self.email5 = email5
            self.email6 = email6
            
            ############
            # Email 1   
            ############
            smtpobj = smtplib.SMTP('smtp.office365.com' , 587)
            ### start smtp 
            smtpobj.ehlo() 
            ### use TLS transmission   
            smtpobj.starttls()

            smtpobj.login('Jason@tinfar.com.tw','Xad83370')
            
            msg = MIMEMultipart()
            #msg["subject"] = "Auto Backup Server - PDF fail Message"
            msg["subject"] = "大塚製藥 監控數值 PDF 自動備份"
            msg["from"]    = 'Jason@tinfar.com.tw'
            msg["to"]      = self.email1
            #msg.attach(MIMEText( str(self.lost_date) + " ,  backup PDF failed !"))
            msg.attach(MIMEText('備份記錄\n\t' + str(self.lost_date) + " , 監控數值 PDF 檔案 備份到 NAS 失敗."))
            smtpobj.send_message(msg=msg)

            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' : ' +  str('backup fail send ' + self.email1 + ' successful.'))
            print('----------------------------------------------------------------------------------------------')
            smtpobj.quit()

            ############
            # Email 2   
            ############
            smtpobj = smtplib.SMTP('smtp.office365.com' , 587)
            ### start smtp 
            smtpobj.ehlo() 
            ### use TLS transmission   
            smtpobj.starttls()

            smtpobj.login('Jason@tinfar.com.tw','Xad83370')
            
            msg = MIMEMultipart()
            #msg["subject"] = "Auto Backup Server - PDF fail Message"
            msg["subject"] = "大塚製藥 監控數值 PDF 自動備份"
            msg["from"]    = 'Jason@tinfar.com.tw'
            msg["to"]      = self.email2
            #msg.attach(MIMEText( str(self.lost_date) + " ,  backup PDF failed !"))
            msg.attach(MIMEText('備份記錄\n\t' + str(self.lost_date) + " , 監控數值 PDF 檔案 備份到 NAS 失敗."))
            smtpobj.send_message(msg=msg)

            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' : ' +  str('backup fail send ' + self.email2 + ' successful.'))
            print('----------------------------------------------------------------------------------------------')
            smtpobj.quit()

            ############
            # Email 3   
            ############
            smtpobj = smtplib.SMTP('smtp.office365.com' , 587)
            ### start smtp 
            smtpobj.ehlo() 
            ### use TLS transmission   
            smtpobj.starttls()

            smtpobj.login('Jason@tinfar.com.tw','Xad83370')
            
            msg = MIMEMultipart()
            #msg["subject"] = "Auto Backup Server - PDF fail Message"
            msg["subject"] = "大塚製藥 監控數值 PDF 自動備份"
            msg["from"]    = 'Jason@tinfar.com.tw'
            msg["to"]      = self.email3
            #msg.attach(MIMEText( str(self.lost_date) + " ,  backup PDF failed !"))
            msg.attach(MIMEText('備份記錄\n\t' + str(self.lost_date) + " , 監控數值 PDF 檔案 備份到 NAS 失敗."))
            smtpobj.send_message(msg=msg)

            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' : ' +  str('backup fail send ' + self.email3 + ' successful.'))
            print('----------------------------------------------------------------------------------------------')
            smtpobj.quit()
            
            ############
            # Email 4   
            ############
            smtpobj = smtplib.SMTP('smtp.office365.com' , 587)
            ### start smtp 
            smtpobj.ehlo() 
            ### use TLS transmission   
            smtpobj.starttls()

            smtpobj.login('Jason@tinfar.com.tw','Xad83370')
            
            msg = MIMEMultipart()
            #msg["subject"] = "Auto Backup Server - PDF fail Message"
            msg["subject"] = "大塚製藥 監控數值 PDF 自動備份"
            msg["from"]    = 'Jason@tinfar.com.tw'
            msg["to"]      = self.email4
            #msg.attach(MIMEText( str(self.lost_date) + " ,  backup PDF failed !"))
            msg.attach(MIMEText('備份記錄\n\t' + str(self.lost_date) + " , 監控數值 PDF 檔案 備份到 NAS 失敗."))
            smtpobj.send_message(msg=msg)

            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' : ' +  str('backup fail send ' + self.email4 + ' successful.'))
            print('----------------------------------------------------------------------------------------------')
            smtpobj.quit()

            ############
            # Email 5   
            ############
            smtpobj = smtplib.SMTP('smtp.office365.com' , 587)
            ### start smtp 
            smtpobj.ehlo() 
            ### use TLS transmission   
            smtpobj.starttls()

            smtpobj.login('Jason@tinfar.com.tw','Xad83370')
            
            msg = MIMEMultipart()
            #msg["subject"] = "Auto Backup Server - PDF fail Message"
            msg["subject"] = "大塚製藥 監控數值 PDF 自動備份"
            msg["from"]    = 'Jason@tinfar.com.tw'
            msg["to"]      = self.email5
            #msg.attach(MIMEText( str(self.lost_date) + " ,  backup PDF failed !"))
            msg.attach(MIMEText('備份記錄\n\t' + str(self.lost_date) + " , 監控數值 PDF 檔案 備份到 NAS 失敗."))
            smtpobj.send_message(msg=msg)

            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' : ' +  str('backup fail send ' + self.email5 + ' successful.'))
            print('----------------------------------------------------------------------------------------------')
            smtpobj.quit()

            ############
            # Email 6   
            ############
            smtpobj = smtplib.SMTP('smtp.office365.com' , 587)
            ### start smtp 
            smtpobj.ehlo() 
            ### use TLS transmission   
            smtpobj.starttls()

            smtpobj.login('Jason@tinfar.com.tw','Xad83370')
            
            msg = MIMEMultipart()
            #msg["subject"] = "Auto Backup Server - PDF fail Message"
            msg["subject"] = "大塚製藥 監控數值 PDF 自動備份"
            msg["from"]    = 'Jason@tinfar.com.tw'
            msg["to"]      = self.email6
            #msg.attach(MIMEText( str(self.lost_date) + " ,  backup PDF failed !"))
            msg.attach(MIMEText('備份記錄\n\t' + str(self.lost_date) + " , 監控數值 PDF 檔案 備份到 NAS 失敗.\n\t(系統自動發信，勿回覆)"))
            smtpobj.send_message(msg=msg)

            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' : ' +  str('backup fail send ' + self.email6 + ' successful.'))
            print('----------------------------------------------------------------------------------------------')
            smtpobj.quit()

        except smtplib.SMTPException as e:
            print("< Error > Fail SMTP : " + str(e))
    
    #######################
    # success_send_email
    #######################
    def success_send_email(self , r_time , lost_date , email1 , email2 , email3 , email4 , email5 , email6):
        try:
            ### variable
            self.r_time    = r_time
            self.lost_date = lost_date
            
            self.email1 = email1
            self.email2 = email2
            self.email3 = email3
            self.email4 = email4
            self.email5 = email5
            self.email6 = email6
            
            ############
            # Email 1  
            ############
            smtpobj = smtplib.SMTP('smtp.office365.com' , 587)
            ### start smtp 
            smtpobj.ehlo() 
            ### use TLS transmission   
            smtpobj.starttls()

            smtpobj.login('Jason@tinfar.com.tw','Xad83370')
            
            msg = MIMEMultipart()
            #msg["subject"] = "Auto Backup Server - PDF successful Message"
            msg["subject"] = "大塚製藥 監控數值 PDF 自動備份"
            msg["from"]    = 'Jason@tinfar.com.tw'
            msg["to"]      = self.email1
            msg.attach(MIMEText('備份記錄\n\t' + str(self.lost_date) + ' , 大塚製藥 感測器 No.1 ~ 18 位置 , 監控數值 PDF 檔案 備份到 NAS 成功.\n\t(系統自動發信，勿回覆)'))
            smtpobj.send_message(msg=msg)

            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' : ' + str('backup success send ' + self.email1 + ' successful.'))
            print('----------------------------------------------------------------------------------------------')
            smtpobj.quit()

            
            ############
            # Email 2  
            ############
            smtpobj = smtplib.SMTP('smtp.office365.com' , 587)
            ### start smtp 
            smtpobj.ehlo() 
            ### use TLS transmission   
            smtpobj.starttls()

            smtpobj.login('Jason@tinfar.com.tw','Xad83370')
            
            msg = MIMEMultipart()
            msg["subject"] = "大塚製藥 監控數值 PDF 自動備份"
            msg["from"]    = 'Jason@tinfar.com.tw'
            msg["to"]      = self.email2
            msg.attach(MIMEText('備份記錄\n\t' + str(self.lost_date) + " , 大塚製藥 感測器 No.1 ~ 18 位置 , 監控數值 PDF 檔案 備份到 NAS 成功."))
            smtpobj.send_message(msg=msg)

            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' : ' + str('backup success send ' + self.email2 + ' successful.'))
            print('----------------------------------------------------------------------------------------------')
            smtpobj.quit()

            ############
            # Email 3  
            ############
            smtpobj = smtplib.SMTP('smtp.office365.com' , 587)
            ### start smtp 
            smtpobj.ehlo() 
            ### use TLS transmission   
            smtpobj.starttls()

            smtpobj.login('Jason@tinfar.com.tw','Xad83370')
            
            msg = MIMEMultipart()
            msg["subject"] = "大塚製藥 監控數值 PDF 自動備份"
            msg["from"]    = 'Jason@tinfar.com.tw'
            msg["to"]      = self.email3
            msg.attach(MIMEText('備份記錄\n\t' + str(self.lost_date) + " , 大塚製藥 感測器 No.1 ~ 18 位置 , 監控數值 PDF 檔案 備份到 NAS 成功."))
            smtpobj.send_message(msg=msg)

            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' : ' + str('backup success send ' + self.email3 + ' successful.'))
            print('----------------------------------------------------------------------------------------------')
            smtpobj.quit()
            
            ############
            # Email 4
            ############
            smtpobj = smtplib.SMTP('smtp.office365.com' , 587)
            ### start smtp 
            smtpobj.ehlo() 
            ### use TLS transmission   
            smtpobj.starttls()

            smtpobj.login('Jason@tinfar.com.tw','Xad83370')
            
            msg = MIMEMultipart()
            msg["subject"] = "大塚製藥 監控數值 PDF 自動備份"
            msg["from"]    = 'Jason@tinfar.com.tw'
            msg["to"]      = self.email4
            msg.attach(MIMEText('備份記錄\n\t' + str(self.lost_date) + " , 大塚製藥 感測器 No.1 ~ 18 位置 , 監控數值 PDF 檔案 備份到 NAS 成功."))
            smtpobj.send_message(msg=msg)

            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' : ' + str('backup success send ' + self.email4 + ' successful.'))
            print('----------------------------------------------------------------------------------------------')
            smtpobj.quit()
            
            ############
            # Email 5
            ############
            smtpobj = smtplib.SMTP('smtp.office365.com' , 587)
            ### start smtp 
            smtpobj.ehlo() 
            ### use TLS transmission   
            smtpobj.starttls()

            smtpobj.login('Jason@tinfar.com.tw','Xad83370')
            
            msg = MIMEMultipart()
            msg["subject"] = "大塚製藥 監控數值 PDF 自動備份"
            msg["from"]    = 'Jason@tinfar.com.tw'
            msg["to"]      = self.email5
            msg.attach(MIMEText('備份記錄\n\t' + str(self.lost_date) + " , 大塚製藥 感測器 No.1 ~ 18 位置 , 監控數值 PDF 檔案 備份到 NAS 成功."))
            smtpobj.send_message(msg=msg)

            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' : ' + str('backup success send ' + self.email5 + ' successful.'))
            print('----------------------------------------------------------------------------------------------')
            smtpobj.quit()

            ############
            # Email 6
            ############
            smtpobj = smtplib.SMTP('smtp.office365.com' , 587)
            ### start smtp 
            smtpobj.ehlo() 
            ### use TLS transmission   
            smtpobj.starttls()

            smtpobj.login('Jason@tinfar.com.tw','Xad83370')
            
            msg = MIMEMultipart()
            msg["subject"] = "大塚製藥 監控數值 PDF 自動備份"
            msg["from"]    = 'Jason@tinfar.com.tw'
            msg["to"]      = self.email6
            msg.attach(MIMEText('備份記錄\n\t' + str(self.lost_date) + " , 大塚製藥 感測器 No.1 ~ 18 位置 , 監控數值 PDF 檔案 備份到 NAS 成功."))
            smtpobj.send_message(msg=msg)

            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' : ' + str('backup success send ' + self.email6 + ' successful.'))
            print('----------------------------------------------------------------------------------------------')
            smtpobj.quit()
            
        except smtplib.SMTPException as e:
            print("< Error > successful SMTP : " + str(e))
    

########################################################################################################################
#
# main
#
########################################################################################################################
if __name__ == '__main__':
    realtime = monitor()