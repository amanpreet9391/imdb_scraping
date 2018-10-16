## scraping_imdb
### This is a project for Hacker Camp 2019 by Innovaccer - SDE-Platform
Please find the problem statement [here](http://innovaccer.com/media/hackercamp/SDE-Intern-Assignment.pdf).
### Things to be implemented as per the problem statement
* Creating Database.
* Fetching data from the user.
  *  email address
  * title of tv series
* Web scraping
* Sending mail
 
 All the scripts to perform these tasks are already imported in main script i.e.`python main.py`
### Prerequisites
 All the scipts that I have created were tested successfully on macOS & other Linux based OSes with Python 2.7.10 and MySql installed on the system.
#### 1. Creating Database
To create databse,script involved `python Create_db.py`. In this database named inputDB will be created.This database include a table named input_table to store email address and title of tv series given by user.
#### 2. User input
For storing user inputs database is used.`python interface.py`will store values provided by user.
![user_input](https://user-images.githubusercontent.com/25201552/47012676-65387880-d162-11e8-81f2-75c367255b90.png)
![database](https://user-images.githubusercontent.com/25201552/47012776-bc3e4d80-d162-11e8-8ef4-e5f97bfa7b2f.jpg)
#### 3.Web Scraping
We have to find the imdbID corresponding to the title of tv series provided by user.To find imdbID we use omdb(database of imdb).Using the api key of omdb i.i.`http://www.omdbapi.com/?t=title_of_series&apikey=8deaca41`we get the details about tv series in form of a json script.Then find imdbID from that script.After getting the imdbID we will be able to get the url corresponding to series at imdb.Url looks like `https://www.imdb.com/title/imdbID/`This url is further used for web scraping. We are going to use Python as our scraping language, together with a simple and powerful library, BeautifulSoup.
![scrape](https://user-images.githubusercontent.com/25201552/47013290-4c30c700-d164-11e8-92c6-fd66083dac49.jpg)
#### 4.Email
 For emailing we have used SMTP library.Function mail_deliver from script `python scrape1.py` is responsible for mailing the datails of tv series to email id provided by user.
 ![email](https://user-images.githubusercontent.com/25201552/47013530-1e984d80-d165-11e8-9d06-0874bff513c5.png)
