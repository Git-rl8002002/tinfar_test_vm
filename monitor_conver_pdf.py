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

class monitor():
    
    #########
    # init
    #########
    def __init__(self):
        self.conver_pdf()

    ######################
    # read sensor value
    ######################
    def conver_pdf(self):
        
        try:
            ###########################
            #
            # 大塚製藥 TXT conver PDF
            #
            ###########################
            
            ### record time
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y-%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())
            self.conver_pdf_day = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")

            ### print msg
            print('----------------------------------------------------------------------------------------------')

            ##########################
            # conver PDF sensor S-1 
            ##########################
            try:
                ### variables
                self.s_txt = '_S-1.txt'
                self.s_pdf = '_S-1.pdf'
                self.path   = 'S1'
                self.err    = 'S-1'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-2
            ##########################
            try:
                ### variables
                self.s_txt = '_S-2.txt'
                self.s_pdf = '_S-2.pdf'
                self.path   = 'S2'
                self.err    = 'S-2'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-3
            ##########################
            try:
                ### variables
                self.s_txt = '_S-3.txt'
                self.s_pdf = '_S-3.pdf'
                self.path   = 'S3'
                self.err    = 'S-3'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-4
            ##########################
            try:
                ### variables
                self.s_txt = '_S-4.txt'
                self.s_pdf = '_S-4.pdf'
                self.path   = 'S4'
                self.err    = 'S-4'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-5
            ##########################
            try:
                ### variables
                self.s_txt = '_S-5.txt'
                self.s_pdf = '_S-5.pdf'
                self.path   = 'S5'
                self.err    = 'S-5'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-6
            ##########################
            try:
                ### variables
                self.s_txt = '_S-6.txt'
                self.s_pdf = '_S-6.pdf'
                self.path   = 'S6'
                self.err    = 'S-6'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-7
            ##########################
            try:
                ### variables
                self.s_txt = '_S-7.txt'
                self.s_pdf = '_S-7.pdf'
                self.path   = 'S7'
                self.err    = 'S-7'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-8
            ##########################
            try:
                ### variables
                self.s_txt = '_S-8.txt'
                self.s_pdf = '_S-8.pdf'
                self.path   = 'S8'
                self.err    = 'S-8'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-9
            ##########################
            try:
                ### variables
                self.s_txt = '_S-9.txt'
                self.s_pdf = '_S-9.pdf'
                self.path   = 'S9'
                self.err    = 'S-9'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-10
            ##########################
            try:
                ### variables
                self.s_txt = '_S-10.txt'
                self.s_pdf = '_S-10.pdf'
                self.path   = 'S10'
                self.err    = 'S-10'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-11-1
            #############################
            try:
                ### variables
                self.s_txt = '_S-11-1.txt'
                self.s_pdf = '_S-11-1.pdf'
                self.path   = 'S11-1'
                self.err    = 'S-11-1'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-11-2
            #############################
            try:
                ### variables
                self.s_txt = '_S-11-2.txt'
                self.s_pdf = '_S-11-2.pdf'
                self.path  = 'S11-2'
                self.err   = 'S-11-2'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-12
            #############################
            try:
                ### variables
                self.s_txt = '_S-12.txt'
                self.s_pdf = '_S-12.pdf'
                self.path  = 'S12'
                self.err   = 'S-12'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-13
            #############################
            try:
                ### variables
                self.s_txt = '_S-13.txt'
                self.s_pdf = '_S-13.pdf'
                self.path  = 'S13'
                self.err   = 'S-13'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-14
            #############################
            try:
                ### variables
                self.s_txt = '_S-14.txt'
                self.s_pdf = '_S-14.pdf'
                self.path  = 'S14'
                self.err   = 'S-14'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-15-1
            #############################
            try:
                ### variables
                self.s_txt = '_S-15-1.txt'
                self.s_pdf = '_S-15-1.pdf'
                self.path  = 'S15-1'
                self.err   = 'S-15-1'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-15-2
            #############################
            try:
                ### variables
                self.s_txt = '_S-15-2.txt'
                self.s_pdf = '_S-15-2.pdf'
                self.path  = 'S15-2'
                self.err   = 'S-15-2'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-15-3
            #############################
            try:
                ### variables
                self.s_txt = '_S-15-3.txt'
                self.s_pdf = '_S-15-3.pdf'
                self.path  = 'S15-3'
                self.err   = 'S-15-3'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-15-4
            #############################
            try:
                ### variables
                self.s_txt = '_S-15-4.txt'
                self.s_pdf = '_S-15-4.pdf'
                self.path  = 'S15-4'
                self.err   = 'S-15-4'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-15-5
            #############################
            try:
                ### variables
                self.s_txt = '_S-15-5.txt'
                self.s_pdf = '_S-15-5.pdf'
                self.path  = 'S15-5'
                self.err   = 'S-15-5'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-15-6
            #############################
            try:
                ### variables
                self.s_txt = '_S-15-6.txt'
                self.s_pdf = '_S-15-6.pdf'
                self.path  = 'S15-6'
                self.err   = 'S-15-6'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-16
            #############################
            try:
                ### variables
                self.s_txt = '_S-16.txt'
                self.s_pdf = '_S-16.pdf'
                self.path  = 'S16'
                self.err   = 'S-16'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-17
            #############################
            try:
                ### variables
                self.s_txt = '_S-17.txt'
                self.s_pdf = '_S-17.pdf'
                self.path  = 'S17'
                self.err   = 'S-17'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-18
            #############################
            try:
                ### variables
                self.s_txt = '_S-18.txt'
                self.s_pdf = '_S-18.pdf'
                self.path  = 'S18'
                self.err   = 'S-18'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))

            print('----------------------------------------------------------------------------------------------')

            ###################
            # put PDF in NAS
            ###################
            try:
                cnopts = sftp.CnOpts()
                cnopts.hostkeys = None
                
                print('----------------------------------------------------------------------------------------------')

                #######
                # S-1
                #######
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s1'])
                self.sftp.put(nas_para['linux_path_s1']+self.conver_pdf_day + '_S-1.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-1.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-1')
                
                #######
                # S-2
                #######
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s2'])
                self.sftp.put(nas_para['linux_path_s2']+self.conver_pdf_day+'_S-2.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-2.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-2')

                #######
                # S-3
                #######
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s3'])
                self.sftp.put(nas_para['linux_path_s3']+self.conver_pdf_day+'_S-3.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-3.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-3')

                #######
                # S-4
                #######
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s4'])
                self.sftp.put(nas_para['linux_path_s4']+self.conver_pdf_day+'_S-4.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-4.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-4')

                #######
                # S-5
                #######
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s5'])
                self.sftp.put(nas_para['linux_path_s5']+self.conver_pdf_day+'_S-5.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-5.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-5')

                #######
                # S-6
                #######
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s6'])
                self.sftp.put(nas_para['linux_path_s6']+self.conver_pdf_day+'_S-6.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-6.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-6')

                #######
                # S-7
                #######
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s7'])
                self.sftp.put(nas_para['linux_path_s7']+self.conver_pdf_day+'_S-7.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-7.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-7')

                #######
                # S-8
                #######
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s8'])
                self.sftp.put(nas_para['linux_path_s8']+self.conver_pdf_day+'_S-8.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-8.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-8')

                #######
                # S-9
                #######
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s9'])
                self.sftp.put(nas_para['linux_path_s9']+self.conver_pdf_day+'_S-9.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-9.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-9')

                ########
                # S-10
                ########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s10'])
                self.sftp.put(nas_para['linux_path_s10']+self.conver_pdf_day+'_S-10.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-10.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-10')

                ##########
                # S-11-1
                ##########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s11-1'])
                self.sftp.put(nas_para['linux_path_s11-1']+self.conver_pdf_day+'_S-11-1.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-11-1.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-11-1')

                ##########
                # S-11-2
                ##########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s11-2'])
                self.sftp.put(nas_para['linux_path_s11-2']+self.conver_pdf_day+'_S-11-2.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-11-2.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-11-2')

                ########
                # S-12
                ########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s12'])
                self.sftp.put(nas_para['linux_path_s12']+self.conver_pdf_day+'_S-12.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-12.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-12')

                ########
                # S-13
                ########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s13'])
                self.sftp.put(nas_para['linux_path_s13']+self.conver_pdf_day+'_S-13.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-13.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-13')

                ########
                # S-14
                ########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s14'])
                self.sftp.put(nas_para['linux_path_s14']+self.conver_pdf_day+'_S-14.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-14.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-14')

                ##########
                # S-15-1
                ##########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s15-1'])
                self.sftp.put(nas_para['linux_path_s15-1']+self.conver_pdf_day+'_S-15-1.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-15-1.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-15-1')

                ##########
                # S-15-2
                ##########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s15-2'])
                self.sftp.put(nas_para['linux_path_s15-2']+self.conver_pdf_day+'_S-15-2.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-15-2.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-15-2')

                ##########
                # S-15-3
                ##########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s15-3'])
                self.sftp.put(nas_para['linux_path_s15-3']+self.conver_pdf_day+'_S-15-3.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-15-3.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-15-3')

                ##########
                # S-15-4
                ##########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s15-4'])
                self.sftp.put(nas_para['linux_path_s15-4']+self.conver_pdf_day+'_S-15-4.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-15-4.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-15-4')

                ##########
                # S-15-5
                ##########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s15-5'])
                self.sftp.put(nas_para['linux_path_s15-5']+self.conver_pdf_day+'_S-15-5.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-15-5.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-15-5')

                ##########
                # S-15-6
                ##########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s15-6'])
                self.sftp.put(nas_para['linux_path_s15-6']+self.conver_pdf_day+'_S-15-6.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-15-6.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-15-6')

                ########
                # S-16
                ########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s16'])
                self.sftp.put(nas_para['linux_path_s16']+self.conver_pdf_day+'_S-16.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-16.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-16')

                ########
                # S-17
                ########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s17'])
                self.sftp.put(nas_para['linux_path_s17']+self.conver_pdf_day+'_S-17.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-17.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-17')

                ########
                # S-18
                ########
                self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                self.sftp.chdir(nas_para['nas_path_s18'])
                self.sftp.put(nas_para['linux_path_s18']+self.conver_pdf_day+'_S-18.pdf')
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + '_S-18.pdf sftp put NAS successful.')
                self.sftp.close()
                ### backup record
                self.backup_pdf_nas('S-18')

                ### backup PDF to NAS
                #self.backup_pdf_nas()

            except Exception as e:
                print('< Error > Sftp put NAS Error : ' + str(e))
            
            ### print msg
            print('----------------------------------------------------------------------------------------------')
            
        except Exception as e:
            print('< Error > conver_pdf : ' + str(e))

    ###################
    # backup_pdf_nas
    ###################
    def backup_pdf_nas(self , sensor):
        
        ### variables
        self.sensor  = sensor
        self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        self.r_year  = time.strftime("%Y" , time.localtime())
        self.r_month = time.strftime("%Y-%m" , time.localtime())
        self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
        self.backup_pdf_day    = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        self.os_sys            = platform.system()
        self.record_backup_nas = self.r_time + ' , ' + self.backup_pdf_day + '_' + self.sensor +'.pdf\n'
        self.pdf               = self.backup_pdf_day + '_' + self.sensor  + '.pdf'
        
        ##################
        # write to file
        ##################
        
        ### save file path - Linux
        try:
            if self.os_sys == 'Linux':
                
                ### check txt document exists
                #self.floderpath = txt_path['linux_txt_path'] + self.r_month
                #try:
                    #os.makedirs(self.floderpath)
                #except FileExistsError:

                self.add = open(txt_path['linux_pdf_path'] ,'a')
                self.add.write(self.record_backup_nas)
                self.add.close()

                ### insert into txt
                print(str(self.r_time) + ' , record backup ' + str(self.pdf) + ' to NAS txt log successful.')
        except Exception as e:
            print('< Error > record backup PDF to NAS txt log : ' + str(e))
        
        try:
            ###################
            # write to MySQL
            ###################

            ### insert into MySQL by this month
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()

            self.sql2 = "insert into backup_record(r_time,backup_time) value('{0}','{1}')".format(self.r_time , self.pdf)
            self.curr2.execute(self.sql2)
            self.conn2.commit()
            self.conn2.close()
            
            ### insert into database
            print(str(self.r_time) + ' , record backup ' + str(self.pdf) + ' to NAS DB log successful.')

        except Exception as e:
            print('< Error > record backup PDF to NAS DB log : ' + str(e))
        finally:
            pass

#########
# main
#########
def main():
    realtime = monitor()

if __name__ == '__main__':
    main()