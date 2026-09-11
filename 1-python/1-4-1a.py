from datetime import datetime
import beautiful_date as bd

today = bd.BeautifulDate.fromisoformat('2026-09-08')

six_months_from_today = today + 6 * bd.months

print(today)
print(six_months_from_today)

# Parse this date into a BeautifulDate object Jan 14, 2024
parsed = datetime.strptime("Jan 14, 2024", "%b %d, %Y").date()
parsed_date = bd.BeautifulDate(parsed.year, parsed.month, parsed.day)

print(parsed_date)