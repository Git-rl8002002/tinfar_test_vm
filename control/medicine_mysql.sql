/*
* Author   : JasonHung
* Date     : 20221116
* Update   : 20221116
* Function : JNC CB and sensor value
*/

/*
 * database  tinfar_medicine
 */ 
create database tinfar_medicine DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
use tinfar_medicine;




/* 
 * backup_record
 */
create table backup_record(
no int not null primary key AUTO_INCREMENT,
r_time datetime null,
backup_time varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/* 
 * medicine
 */
create table medicine(
no int not null primary key AUTO_INCREMENT,
r_time datetime null,
r_year varchar(100) null,
r_month varchar(100) null,
r_day varchar(100) null,
s_kind varchar(200) null,
s_content varchar(200) null,
s_protocol varchar(200) null,
val_1 varchar(200) null,
val_2 varchar(200) null,
val_3 varchar(200) null,
val_4 varchar(200) null,
val_5 varchar(200) null,
val_6 varchar(200) null,
val_7 varchar(200) null,
val_8 varchar(200) null,
val_9 varchar(200) null,
val_10 varchar(200) null,
val_11 varchar(200) null,
val_12 varchar(200) null,
val_13 varchar(200) null,
val_14 varchar(200) null,
val_15 varchar(200) null,
val_16 varchar(200) null,
val_17 varchar(200) null,
val_18 varchar(200) null,
val_19 varchar(200) null,
val_20 varchar(200) null,
val_21 varchar(200) null,
val_22 varchar(200) null,
val_23 varchar(200) null,
val_24 varchar(200) null,
val_25 varchar(200) null,
r_status varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/* 
 * login_out_record
 */
create table login_out_record(
no int not null primary key AUTO_INCREMENT,
login_time datetime null,
logout_time datetime null,
a_user varchar(200) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/* 
 * account
 */
create table account(
no int not null primary key AUTO_INCREMENT,
r_time datetime null,
r_year varchar(100) null,
r_month varchar(100) null,
r_day varchar(100) null,
a_user varchar(200) null,
a_pwd varchar(200) null,
a_lv varchar(10) null,
a_status varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into account (a_user , a_pwd , a_lv , a_status) VALUES('admin','1qaz#123','1','run');