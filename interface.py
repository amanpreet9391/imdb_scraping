import MySQLdb
import mysql.connector

def user_interface():
	email=raw_input('Email address: ')
	status="+"
	#num1=raw_input('Number of fav tv series')
	#num=int(num1)
	#List=[]
	#for i in range(num):
	#	name=raw_input('tv series name: ')
	#	List.append(name)	

	name = raw_input("Enter")
	title_list1 = name.split(",")
	title_list=[]
	#for i in title_list:
		#if ' ' in i:		
			#k = i.replace(' ','+')
			#print(k)
			#title_list.append(k)
			#title_list.remove(i)
	#print(title_list)	
	for i in range(len(title_list1)):
		k=title_list1[i].replace(' ','+')
		title_list.append(k)
		print(title_list)
	print(title_list)
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="root"
	)

	connection=MySQLdb.connect(host='localhost',user='root',passwd='root',db='inputDB2')
	cursor=connection.cursor()
	mycursor = mydb.cursor()
	mycursor.execute("use inputDB2")
	mydb2= mysql.connector.connect(host="localhost",user="root",passwd="root",database="inputDB2")
	mycursor2 = mydb2.cursor()

	#mycursor2.execute("CREATE TABLE email_title (email VARCHAR(255), title VARCHAR(255))")
	

	#mycursor3.execute("CREATE TABLE titlestatus (title VARCHAR(255), status VARCHAR(255))")
	for k in range(len(title_list)):
		names=title_list[k]
		sql2=("insert into input_table2(email,title)Values('%s','%s')"%(email,names))
	
		
		cursor.execute(sql2)
	
	connection.commit()
	return email, title_list

	


	
















		
