import beautiful_date as bd

today = bd.BeautifulDate.fromisoformat('2026-09-08')
# add 2 months to the date (multiply on the left: BeautifulTimedelta only defines __rmul__)
today = today + 2 * bd.months

print(today)