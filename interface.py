import MySQLdb
import mysql.connector

def user_interface():
	email=raw_input('Email address: ')       #taking user's email address
	
	
	name = raw_input("TV Series: ")	         #taking tv series title from user
	title_list1 = name.split(",")
	title_list=[] 
		
	for i in range(len(title_list1)):
		k=title_list1[i].replace(' ','+')
		title_list.append(k)		  #creating and appending list of titles provided by user
	mydb = mysql.connector.connect( 
	host="localhost",
	user="root",
	passwd="root"
	)

	connection=MySQLdb.connect(host='localhost',user='root',passwd='root',db='inputDB')
	cursor=connection.cursor()
	mycursor = mydb.cursor()
	mycursor.execute("use inputDB")  #using database inputDB
	mydb2= mysql.connector.connect(host="localhost",user="root",passwd="root",database="inputDB")
	mycursor2 = mydb2.cursor()

	
	for k in range(len(title_list)):
		names=title_list[k]
		sql2=("insert into input_table(email,title)Values('%s','%s')"%(email,names))   #storing email address and titles in table 												        input_table
	
		
		cursor.execute(sql2)
	
	connection.commit()
	return email, title_list	#returning the data fetched from user

	


	
















		
