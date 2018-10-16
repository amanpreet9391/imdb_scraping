import MySQLdb
import mysql.connector

def create_db():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="root"
	)
	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE input_DB")  #creating database inputDB

	connection=MySQLdb.connect(host='localhost',user='root',passwd='root',db='input_DB') 
	cursor=connection.cursor()

	mydb2= mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="root",
	  database="input_DB"
	)
	mycursor2 = mydb2.cursor()

	mycursor2.execute("CREATE TABLE input_datatable (email VARCHAR(255), title VARCHAR(255))")#creating table input_table for storing email 													and title of series given by user.
		
