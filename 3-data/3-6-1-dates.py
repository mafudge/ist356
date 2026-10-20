
import datetime



# today's date
today = datetime.date.today()

# add 30 days to today
today_plus_30 = today + datetime.timedelta(days=30)

# print today and today_plus_30
print("Today's date:", today)
print("Date after 30 days:", today_plus_30)

date_string = datetime.datetime.strftime(today, "%A, %B, %w %Y")
print("Today's date in string format:", date_string)


my_birthday = "Dec 6, 1970"
my_birthday2 = "1970-12-06"

my_birthday = datetime.datetime.strptime(my_birthday, "%b %d, %Y")
born_on = datetime.datetime.strftime(my_birthday, "%A")
print("I was born on a", born_on)    