import smtplib
import json
import certifi
from urllib2 import urlopen as ureq
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as soup


def ID(title_series):							#function to find imdbID corresponding to given tv series title
	
	myurl1="http://www.omdbapi.com/?t=%s&apikey=8deaca41"%title_series  #creating omdb url from title
	client1=ureq(myurl1)
	page=json.load(client1)
	ID=page['imdbID']
	myurl="https://www.imdb.com/title/%s/"%ID		#imdb url to be used for scraping
	return(myurl)						#to return the generated url 



def helper(List):						#function to do scraping

	status=[]
	IMDBID=[]
	for i in range(len(List)):
		status1=[]
		myurl=ID(List[i])
		uclient=ureq(myurl, cafile=certifi.where())
		page_html=uclient.read()				#reading the content from myurl
		uclient.close()
		
		page_soup=soup(page_html,"html.parser")			#using 'beautiful soup' for scraping
		
		title=page_soup.h1
		status1.append("Title of series: %s"%title.text)	#scraped title of tv series
		container=page_soup.findAll("div",{"class":"table full-width"})
		contain=container[0]	
		
	
		contain.findAll("div",{"class":"episode-widget-currentep"})

		sub=contain.findAll("div",{"class":"episode-widget-currentep"})
		if sub is None:
        		continue 
		if(sub==[]):
			final=contain.div.findAll("a")
			finals=final[0]
			number1=finals.text
		
			number=int(number1)				       #season number
			finals_date=final[number]
			date=finals_date.text
			
			date=number1		
			DATE=int(date)					       #Date of release
			if(DATE>2018):
				
				status1.append("Upcoming season: %d"%number)			#upcoming season
				status1.append("Aired in: %s"%date)				#year in which it will be released
				status1.append("\n")
			elif(DATE==2018):
				
				status1.append("Running season: %d"%number)			#running season
				status1.append("Aired in: %s"%date)				#year in which season started streaming
				status1.append("\n")
			elif(DATE<2016):
				s="The show has finished streaming all its episodes."
				status1.append(s)
				status1.append("Most recent season: %d"%number)			#last aired season
				status1.append("Aired in: %s"%date)				#year in which it was released
				status1.append("\n")		
		for i in range(len(status1)):
			elements=status1[i]
			status.append(elements)		#list named 'status' having details related to each tv series
	return status						#return list status


def mail_deliver(email, status):				#function for sending mail
	content1="\n"
	for i in range(len(status)):
		
		content1=content1+(status[i]).encode("utf-8")+"\n"   #content which will be mailed to the user
	content=content1.split()
	mail=smtplib.SMTP('smtp.gmail.com',587 )		     #smtp mail id and port number
	mail.ehlo()
	mail.starttls()
	mail.login('aman3006preet','aman9391')			     #username and password of id from which mail is being sent
	mail.sendmail('aman3006preet',email,content1)		     #(sender'mail id,receiver's mail id,content)
	mail.close()
	print("mail delivered")



	


