from dateutils import parsedate_mdy, formatdate_ymd

text = input("Enter date m/d/y: ")
date = parsedate_mdy(text)
date_str = formatdate_ymd(date)
print(date_str)
