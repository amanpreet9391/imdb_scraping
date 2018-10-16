

from Create_db import create_db
from interface import user_interface
#from scrape1 import helper,mail_deliver
from scrape1 import helper,mail_deliver

print("Creating database")
create_db()


email, title_list = user_interface()
status = helper(title_list)
mail_deliver(email, status)
