from datetime import datetime

today = datetime.now()
year = today.year
next_year = year + 1
new_year = "1-1-"+str(next_year)+"-0:00:00" #new year in string
new_year_date = datetime.strptime(new_year, "%m-%d-%Y-%H:%M:%S") # converting new year in date format
time_remaining = new_year_date - today
print(new_year_date)
print(time_remaining)