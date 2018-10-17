# Summer Intern Hiring Challenge
### This is a project for *Hacker Camp 2019 by Innovaccer* for the profile of SDE-Platform(Intern)
## Problem Statement
Create a script which takes email address and favourite TV Series as the input from the user and responds back with the date of latest airing. The user will be entering his/her email address with the name of TV Series he/she wants information of. Multiple names can be entered separated by new line.
The system shall be sending appropriate responses/information to the entered email address.
Please find the detailed problem statement [here](http://innovaccer.com/media/hackercamp/SDE-Intern-Assignment.pdf).

## Input
Email address: abc.123@xyz.com
TV Series: Game of Thrones, Suits, friends, black mirror, Gotham

```
Email address: jagritipopli97@gmail.com
TV Series: game of thrones, suits, friends
```
## Implementation(steps)
* Creating database
* Input data from the user
  * email address
  * title of tv series
* Web Scraping
* Sending desired information via mail
 
All the scripts to perform these tasks are already imported in main script i.e.`python main.py`
## Prerequisites
All the scipts created were tested successfully Linux based OSes with Python 2.7.10 and MySQL installed on the system.
#### 1. Creating Database
Script `python Create_db.py` creates the required database, which will store the input values from the user(email address and Title of TV Series). Single run of this script is required.
#### 2. User input
Script `python interface.py` will be then used to store values provided by user in the database.
![user_input](https://user-images.githubusercontent.com/25201552/47012676-65387880-d162-11e8-81f2-75c367255b90.png)
![database](https://user-images.githubusercontent.com/25201552/47012776-bc3e4d80-d162-11e8-8ef4-e5f97bfa7b2f.jpg)
#### 3. Web Scraping
We need to find the 'imdbID' corresponding to the title of tv series provided by user. To find 'imdbID' we use omdb(database of imdb). Using the api key of omdb i.e. `http://www.omdbapi.com/?t=title_of_series&apikey=8deaca41` we get the details about tv series in form of a json script. After getting the imdbID from the script, we will be able to get the url corresponding to series at imdb. Url will look something like `https://www.imdb.com/title/imdbID/`. 
This url is further used for web-scraping. We are going to use Python as our scraping language, together with a simple and powerful library, BeautifulSoup.
![scrape](https://user-images.githubusercontent.com/25201552/47013290-4c30c700-d164-11e8-92c6-fd66083dac49.jpg)
#### 4. Email
Finally, to mail the desired information, SMTP library is used. 
Secure SMTP library lets you communicate with any secure SMTP server. 
It defines an SMTP client session object which can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
Here are the details of the parameters which are used while sending the email:
* host
* port
* local host_name

An SMTP object has an instance method called sendmail, which is typically used to do the work of mailing a message. It takes three parameters −

* The sender − A string with the address of the sender.

* The receivers − A list of strings, one for each recipient.

* The message − A message as a string formatted as specified in the various RFCs.



