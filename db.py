# install python : https://www.python.org/downloads/
# install xampp : https://www.apachefriends.org/download.html
# open cmd :-> install -> pip install pymysql

import pymysql as mq

#	Server Name -> localhost
#	Username ->		root
#	Password ->		''


myobj = mq.connect(host="localhost",user="root",password="")

cursorobj=myobj.cursor()

try:
	db="create database school"
	cursorobj.execute(db)
	print("database created ")

except mq.Error as e:
	print(f"database error..{e}")

finally:
	myobj.close()

