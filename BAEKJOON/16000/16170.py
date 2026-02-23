from datetime import datetime, timezone

utc_now = datetime.now(timezone.utc)
print(utc_now.year)
print(utc_now.month)
print(utc_now.day)