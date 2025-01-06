# Importing all app imports
from ostra_config import *

# Main Window Functions
def calculate_cml(weight,activityfactor):
    bmr=weight*24.2
    cml=bmr*activityfactor
    cmlrounded= round(cml, 1)    
    return cmlrounded

# Main Window Variables
todays_date_str = dt.date.today().strftime("%d-%m-%Y") #this is a string
todays_date_obj = dt.date.today() #this is an object

# Main Window Lists / Dictionaries
