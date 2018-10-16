

from Create_db import create_db
from interface import user_interface
from scrape1 import helper,mail_deliver

print("Creating database")
#create_db()   #initially creating database.This function should be executed only once.
		

email, title_list = user_interface()   #Taking email address and titles from user.
status = helper(title_list)		#extracting data from imdb site related to series given by user
mail_deliver(email, status)		#mailing the details to user's email id
