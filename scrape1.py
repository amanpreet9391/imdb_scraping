import smtplib
import json
import certifi
from urllib2 import urlopen as ureq
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as soup


def ID(x):	
	words=x
	myurl1="http://www.omdbapi.com/?t=%s&apikey=8deaca41"%words
	client1=ureq(myurl1)
	print(myurl1)
	page=json.load(client1)
	ID=page['imdbID']
	myurl="https://www.imdb.com/title/%s/"%ID
	print(myurl)
	return(myurl)



def helper(List):

	status=[]
	IMDBID=[]
	for i in range(len(List)):
		status1=[]
		myurl=ID(List[i])
		#myurl=str(myurl1)
		#status(myurl1)
		uclient=ureq(myurl, cafile=certifi.where())
		page_html=uclient.read()
		uclient.close()
		
		page_soup=soup(page_html,"html.parser")
		title=page_soup.h1
		print(title.text)
		status1.append("Title of series: %s"%title.text)
		container=page_soup.findAll("div",{"class":"table full-width"})
		contain=container[0]	
		#status(contain)
	
		contain.findAll("div",{"class":"episode-widget-currentep"})

		sub=contain.findAll("div",{"class":"episode-widget-currentep"})
		if(sub==[]):
		
	 
			final=contain.div.findAll("a")
			finals=final[0]
			number1=finals.text
			number=int(number1)
			#status.append("Most recent season: %d"%number)
			finals_date=final[number]
			date=finals_date.text
			#status.append("Aired in: %s"%date)
			DATE=int(date)
			if(DATE>2018):
				print("Upcoming season: %d"%number)
				print("Aired in: %s"%date)
				status1.append("Upcoming season: %d"%number)
				status1.append("Aired in: %s"%date)
			elif(DATE==2018):
				#print("Next Episode: %d"%number)
				print("Running Season %d"%number)
				status1.append("Running seson: %d"%number)
				status1.append("Aired in: %s"%date)
			elif(DATE<2017):
				s="The show has finished streaming all its episodes."
				print(s)	
				status1.append(s)
				print("Most recent season:%d"%number)
				print("Aired in: %s"%date)
				status1.append("Most recent season: %d"%number)
				status1.append("Aired in: %s"%date)
		else:
			subs=sub[0]
			subs.findAll("div",{"class":"episode-widget-airdate"})
			dd=subs.findAll("div",{"class":"episode-widget-airdate"})
			dds=dd[0]
			dds.text
			#status.append(dds.text)
			ddttitle=subs.findAll("div",{"class":"episode-widget-title"})
			ddttitles=ddttitle[0]
			title=ddttitles.a
			title.text
			status1=contain.h4
			#status1.append(status2.text)
			status1.append(dds.text)
			status1.append(title.text)
			print(status1.text)
			print(dds.text)
	
			print(title.text)
			#print(status)
	
		for i in range(len(status1)):
				#print(status1[i])
				elements=status1[i]
				status.append(elements)


	for j in range(len(status)):
		print(status[j])
	return status
#content1=[]

def mail_deliver(email, status):
	content1="\n"
	for i in range(len(status)):
		print(type(status[i]))
		content1=content1+(status[i]).encode("utf-8")+"\n"
	print("&&&&&&&&&&&&&&&&")
	print(content1)
	content=content1.split()
	print(content)
	mail=smtplib.SMTP('smtp.gmail.com',587 )
	mail.ehlo()
	mail.starttls()
	mail.login('aman3006preet','aman9391')
	mail.sendmail('aman3006preet',email,content1)
	mail.close()
	



	


