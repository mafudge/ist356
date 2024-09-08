from datetime import datetime

def parsedate_mdy(text: str) -> datetime:
    dt = datetime.strptime(text, "%m/%d/%Y")
    return dt

def formatdate_ymd(date: datetime) -> str:
    return date.strftime("%Y-%m-%d")



text = input("Enter date m/d/y: ")
date = parsedate_mdy(text)
date_str = formatdate_ymd(date)
print(date_str)
