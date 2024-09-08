from datetime import datetime

text = input("Enter date m/d/y: ")
now = datetime.strptime(text, "%m/%d/%Y")
nowstr = now.strftime("%Y-%m-%d")
print(nowstr)
