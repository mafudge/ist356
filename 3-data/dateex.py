import datetime

# a string
mikes_dob = "Dec 6, 1970"
mikes_dob_date = datetime.datetime.strptime(mikes_dob, "%b %d, %Y")
four_weeks = datetime.timedelta(days=28)
four_weeks_from_dob = mikes_dob_date + four_weeks

mike_dob_dow = mikes_dob_date.strftime("%A")  # day of the week
mike_dob_dow = datetime.datetime.strftime(mikes_dob_date, "%A")  # day of week

# python datetime object
today = datetime.datetime.now()

print(f"Today is {today}")
print(f"Mike's date of birth is {mikes_dob_date}")
print(f"Four weeks from Mike's date of birth is {four_weeks_from_dob}")
print(f"Mike was born on a {mike_dob_dow}")

