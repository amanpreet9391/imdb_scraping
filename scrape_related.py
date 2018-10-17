import smtplib
import json
import certifi
from urllib2 import urlopen as ureq
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as soup


def ID(title_series):							#function to find imdbID corresponding to given tv series
	
	myurl1="http://www.omdbapi.com/?t=%s&apikey=8deaca41"%title_series     #creating omdb url from title
	client1=ureq(myurl1)
	
	page=json.load(client1)
	ID=page['imdbID']						#imdb url to be used for scraping
	myurl="https://www.imdb.com/title/%s/"%ID
	
	return(myurl)							#to return the generated url



def helper(List):							#function to do scraping

	status=[]
	IMDBID=[]
	for i in range(len(List)):
		status1=[]
		myurl=ID(List[i])
		
		uclient=ureq(myurl, cafile=certifi.where())
		page_html=uclient.read()			       #reading the content from myurl	
		uclient.close()
		
		page_soup=soup(page_html,"html.parser")		       #using 'beautiful soup' for scraping
		title=page_soup.h1
		
		status1.append("Title of series: %s"%title.text)	#scraped title of tv series
		container=page_soup.findAll("div",{"class":"table full-width"})
		contain=container[0]	
		
	
		contain.findAll("div",{"class":"episode-widget-currentep"})

		sub=contain.findAll("div",{"class":"episode-widget-currentep"})
		if(sub==[]):
		
	 
			final=contain.div.findAll("a")
			finals=final[0]
			number1=finals.text				#season number
			number=int(number1)
			
			finals_date=final[number]
			date=finals_date.text
			
			DATE=int(date)					#Date of release
			if(DATE>2018):
				
				status1.append("Upcoming season: %d"%number)		#upcoming season
				status1.append("Aired in: %s"%date)			#year in which it will be released
			elif(DATE==2018):
				
				status1.append("Running seson: %d"%number)		#running season
				status1.append("Aired in: %s"%date)			#year in which season started streaming
			elif(DATE<2017):
				s="The show has finished streaming all its episodes."
					
				status1.append(s)
				
				status1.append("Most recent season: %d"%number)		#last aired season
				status1.append("Aired in: %s"%date)			#year in which it was released
		else:
			subs=sub[0]
			subs.findAll("div",{"class":"episode-widget-airdate"})
			dd=subs.findAll("div",{"class":"episode-widget-airdate"})
			dds=dd[0]
			dds.text
			
			ddttitle=subs.findAll("div",{"class":"episode-widget-title"})
			ddttitles=ddttitle[0]
			title=ddttitles.a
			title.text
			status1=contain.h4
			
			status1.append(dds.text)
			status1.append(title.text)
			
		for i in range(len(status1)):
				
				elements=status1[i]				   #list named 'status' having details related to each tv series
				status.append(elements)				   #return list status
							   
	return status


def mail_deliver(email, status):						#function for sending mail
	content1="\n"
	for i in range(len(status)):
		
		content1=content1+(status[i]).encode("utf-8")+"\n"		 #content which will be mailed to the user
	
	content=content1.split()
	
	mail=smtplib.SMTP('smtp.gmail.com',587 )				#smtp mail id and port number
	mail.ehlo()
	mail.starttls()
	sender_email=raw_input("Sender's email address: ")	     #to get username and password of id from which mail is being sent
	sender_password=raw_input("Password: ")
			     
	mail.login(sender_email,sender_password)	
	mail.sendmail(sender_email,email,content1)       #(sender'mail id,receiver's mail id,content)
	
	mail.sendmail(sender_email,email,content1)
	mail.close()
	print("mail delivered")
	



