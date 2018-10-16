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
