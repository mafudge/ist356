import pytest
from datetime import datetime

def parsedate_mdy(text: str) -> datetime:
    dt = datetime.strptime(text, "%m/%d/%Y")
    return dt

def formatdate_ymd(date: datetime) -> str:
    return date.strftime("%Y-%m-%d")

def test_parsedate_mdy():
    assert parsedate_mdy("12/6/1990") == datetime(1990, 12, 6)
    assert parsedate_mdy("03/06/2020") == datetime(2020, 3, 6)
    
def test_formatdate_ymd():
    assert formatdate_ymd(datetime(1990,12,6)) == "1990-12-06"
    assert formatdate_ymd(datetime(2020,3,6)) == "2020-03-06"