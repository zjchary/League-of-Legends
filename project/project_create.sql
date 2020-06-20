########################################
# LSS   Mysql
# https://github.com/zjchary/League-of-Legends
# Example table creation scripts
########################################

########################
# Create information table
########################
create database project;
use project;

create table information
(
  info_id			int				not null auto_increment,
  info_name			varchar(20)		not null,
  info_unit			text(255)		not null,
  info_phone		char(100)		not null,
  info_location		text(255)		not null,
  info_introduction	text(255)		not null,
  primary key(info_id, info_name)
)engine=MyISAM;

########################
# Create schedule table
########################
create table schedule
(
  sche_id			int				not null auto_increment,
  sche_name			varchar(50)		not null,
  sche_stage		text(255)		not null,
  sche_start		datetime		not null,
  sche_end			datetime		not null,
  sche_endtime		datetime		null,
  sche_designer		varchar(50)		not null,
  sche_auditor		varchar(50)		not null,
  sche_annex		mediumblob		null,
  primary key(sche_id, sche_name)
)engine=InnoDB;

