from datetime import datetime

line = "August 3, 2020"

date_format = "%B %d, %Y"  

date_string = '12-25-2018'
format = "%Y-%m-d"

try:
    datetime.strptime(line, date_format)
    pass
except ValueError:
  print("This is the incorrect date string format. It should be YYYY-MM-DD")