########################################
# LSS   Mysql
# https://github.com/zjchary/League-of-Legends
# Example table population scripts
########################################


##########################
# Populate infomation table
##########################
INSERT INTO information(info_id, info_name, info_unit, info_phone, info_location, info_introduction)
VALUES(1, '项目管理系统', '轻工大', '15171514957', '家', '独立开发');
INSERT INTO information(info_id, info_name, info_unit, info_phone, info_location, info_introduction)
VALUES(2, 'fcn人脸识别', 'whpu', '15111112222', '学校', '合作开发');
INSERT INTO information(info_id, info_name, info_unit, info_phone, info_location, info_introduction)
VALUES(3, 'cnn字符识别', '轻工大', '15122223333', '实习单位', '混合开发');
INSERT INTO information(info_id, info_name, info_unit, info_phone, info_location, info_introduction)
VALUES(4, 'deeplab花分割', 'whpu', '15133334444', '工作单位', '系统开发');
INSERT INTO information(info_id, info_name, info_unit, info_phone, info_location, info_introduction)
VALUES(5, '分水岭分割', '轻工大', '15144445555', '在人间', '恭喜发财');


########################
# Populate schedule table
########################
INSERT INTO schedule(sche_id, sche_name, sche_stage, sche_start, sche_end, sche_endtime, sche_designer, sche_auditor)
VALUES(1,'项目管理系统','方案阶段','2020-06-22','2020-07-03', '2020-07-01', '刘守帅', '周吉成');
INSERT INTO schedule(sche_id, sche_name, sche_stage, sche_start, sche_end, sche_endtime, sche_designer, sche_auditor)
VALUES(2,'项目管理系统','可研设计阶段','2020-06-21','2020-07-02', '2020-07-03', '一根草', '牛');
INSERT INTO schedule(sche_id, sche_name, sche_stage, sche_start, sche_end, sche_endtime, sche_designer, sche_auditor)
VALUES(3,'fcn人脸识别','初步阶段','2020-06-20','2020-07-02', '2020-07-03', '一根葱', '吸血鬼');
INSERT INTO schedule(sche_id, sche_name, sche_stage, sche_start, sche_end, sche_endtime, sche_designer, sche_auditor)
VALUES(4,'cnn字符识别','施工设计图阶段','2020-06-19','2020-07-02', null, '一朵花', '牛粪');
INSERT INTO schedule(sche_id, sche_name, sche_stage, sche_start, sche_end, sche_endtime, sche_designer, sche_auditor)
VALUES(5,'deeplab花分割','施工阶段','2020-06-18', '2020-07-01', null, '一棵树', '电锯');
INSERT INTO schedule(sche_id, sche_name, sche_stage, sche_start, sche_end, sche_endtime, sche_designer, sche_auditor)
VALUES(6,'分水岭分割','施工阶段','2020-06-17', '2020-06-30',null, '一片林', '拖走');


