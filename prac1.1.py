Name = input(" Enter Your Name : ")
Age = int(input(" Enter Your Age : "))

import datetime
currunt_year = datetime.datetime.now().year

year_100 = currunt_year + (100 - Age)

print( f"Hello {Name},You will be turn 100 into Year of {year_100}")