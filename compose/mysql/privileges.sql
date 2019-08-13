use mysql;
select host, user from user;
-- 将docker_mysql数据库的权限授权给创建的docker用户，密码为123456：
-- 如果用户docker不存在，则创建用户docker
CREATE USER 'haha'@'%' identified WITH mysql_native_password by '123';
GRANT all ON *.* to haha@'%' WITH GRANT OPTION;
-- mysql新设置用户或权限后需要刷新系统权限否则可能会出现拒绝访问：
flush privileges;