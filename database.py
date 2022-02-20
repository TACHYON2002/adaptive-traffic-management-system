import mysql.connector
mdb = mysql.connector.connect(host='localhost', user='root', passwd="1234")
mc = mdb.cursor()

mc.execute('CREATE DATABASE IF NOT EXISTS speedtracker;')
mc.execute('use speedtracker;')
mc.execute("create table if not exists speedtracker( Date date(), time time(),road_name varchar(25)")




