#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20221116
# Update   : 20230207
# Version  : 1.1
# Function : 大塚製藥 get I6 sensor value

################
#
# sqlite_path
#
################
sqlite_path = {'linux':'/var/www/html/tinfar_test_vm/control/monitor_jnc.db'}

#######
#
# OS
#
#######
os = {'ubuntu_host':'192.168.111.13' , 'ubuntu_gw':'192.168.111.254' ,  
      'ubuntu_u1':'allen' , 'ubuntu_p1':'OtsukatW168!' , 
      'ubuntu_u2':'root' , 'ubuntu_p2':'OtsukatW168!123' , 
      'win_host':'192.168.111.12' , 'win_u':'user' , 'win_p':'' ,
      'jnc_u':'admin' , 'jnc_p':'1qaz2wsx'}

##########
#
# MySQL
#
##########
### Tinfar_test
db_connect = {'host':'61.220.205.143' , 'port':5306 ,'user':'backup' , 'pwd':'SLbackup#123' , 'db':'tinfar_test' , 'charset':'utf8'}
### Tinfar_kedge
kedge_connect = {'host':'61.220.205.143' , 'port':5306,'user':'backup' , 'pwd':'SLbackup#123' , 'db':'tinfar_kedge' , 'charset':'utf8'}

##########
# Email
##########
tinfar_email = {'jason':'Jason@tinfar.com.tw'}

#############
#
# txt path
#
#############
txt_path = {'linux_txt_path':'/var/www/html/tinfar_test_vm/txt/' , 'linux_pdf_path':'/var/www/html/medicine/pdf/nas/backup_record.txt'}

################
#
# 維新 iAeris5
#
################
iaeris52 = {'json_url':'http://61.220.205.1/read?callback?'}


#############
#
# AirCloud
#
#############
#air_cloud_iaqs = {'ip':'192.168.1.140' , 'port':502 , 'id':1 ,'temp':'0x0' , 'rh':'0x1' , 'co2':'0x2' , 'pm25':'0x3' , 'other':'0x4'}
#air_cloud_iaqs = {'ip':'61.220.205.144' , 'port':502 , 'id':1 ,'temp':'0x0' , 'rh':'0x1' , 'co2':'0x2' , 'pm25':'0x3' , 'other':'0x4'}
air_cloud_iaqs = {'ip':'192.168.1.199' , 'port':502 , 'id':1 ,'temp':'0x0' , 'rh':'0x1' , 'co2':'0x2' , 'pm25':'0x3' , 'other':'0x4'}

######################
#
# rtu tcp converter
#
######################
rtu_tcp_converter = {'ip':'61.220.205.143' , 'port':502 , 'id':3 ,'temp':'0x0' , 'rh':'0x1' , 'pr':'0x10' , 'nh3':'0xA' , 'h2s':'0xB'}

#############
#
# 連大興 I6
#
#############
lds_i6 = {'ip':'60.248.16.152' , 'port':502 , 'ph':'0x0000' , 'ec':'0x0001' , 'temp':'0x0002' , 'mt':'0x0003' , 'cf':'0x0004' , 'other':'0x0005'}

############
#
# 富泰 I6
#
############
ft_i6 = {'ip':'60.250.232.118' , 'port':502 , 'ph':'0x0000' , 'ec':'0x0001' , 'temp':'0x0002' , 'mt':'0x0003' , 'cf':'0x0004' , 'other':'0x0005'}

#############
#
# PDF path
#
#############
pdf_path = {'mac_pdf_month_path':'/Users/user/eclipse-workspace/tinfar/medicine/pdf/month/' , 
            'linux_pdf_month_path':'/var/www/html/medicine/pdf/month/' , 
            'windows_pdf_month_path':'d:/medicine\pdf/month/' , 
            'mac_pdf_day_path':'/Users/user/eclipse-workspace/tinfar/medicine/pdf/day/' , 
            'linux_pdf_day_path':'/var/www/html/medicine/pdf/day/' ,
            'windows_pdf_day_path':'d:/medicine/pdf/day/'}

#################
#
# monitor parm
#
#################
### polling time default 60 sec.
polling_time = {'sec':60}

###########
#
# Tinfar
#
###########
### by modbusTCP - Tinfar
i6_tcp_connect = {'ip':'61.220.205.144','port':502}
i6_tcp_param   = {'kind':'CB','protocol':'modbusTCP','position':'TEMP , RH , PR , NH3 , H2S'}
i6_tcp_sensor  = {'temp':'0x0000','rh':'0x0001','pr':'0x0002','nh3':'0x0003','h2s':'0x0004'}


