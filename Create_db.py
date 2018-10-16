import MySQLdb
import mysql.connector

def create_db():
	#email=raw_input('Email address: ')
	#name = raw_input("Enter")
	#title_list = name.split(",")
	#num1=raw_input('Number of fav tv series')
	#num=int(num1)
	#list=[]
	#for i in range(num):
		#name=raw_input('tv series name: ')
		#list.append(name)	
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="root"
	)





	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE inputDB2")

	connection=MySQLdb.connect(host='localhost',user='root',passwd='root',db='inputDB2')
	cursor=connection.cursor()

	mydb2= mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="root",
	  database="inputDB2"
	)
	mycursor2 = mydb2.cursor()

	mycursor2.execute("CREATE TABLE input_table2 (email VARCHAR(255), title VARCHAR(255))")
		#mydb3= mysql.connector.connect(
		  #host="localhost",
		  #user="root",
		  #passwd="root",
		  #database="mydatabase"
		#)
		#mycursor3= mydb2.cursor()

		#mycursor3.execute("CREATE TABLE seriestitle_status (title VARCHAR(255), status VARCHAR(255))")
	#for k in range(len(title_list)):
	#names=title_list[k]
	#sql2=("insert into email_seriestitle(email,title)Values('%s','%s')"%(email,names))
	
		#sql1=("insert into titlestatus2(title,status)Values('%s','%s')"%(names,status))
		#cursor.execute(sql2)
	#cursor.execute(sql1)
	#connection.commit()

