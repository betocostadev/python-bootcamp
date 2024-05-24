# Python - Introduction to Object Oriented Programming in Python
# Dealing with dates and times in Python is easy with the datetime module.
# The datetime module provides classes for manipulating dates and times.
# The datetime module provides the following classes:
# date: A class that represents a date.
# time: A class that represents a time.
# datetime: A class that represents a date and time.
# timedelta: A class that represents a duration, or the difference between two dates or times.
# timezone: A class that represents a time zone.

from datetime import date, time, datetime, timedelta, timezone

print("======== Python - Introduction to Object Oriented Programming in Python ========")
print("=== Dates and Times ===")

# Creating a date object
# The date class is used to represent a date.
# The date class takes three arguments: year, month, and day.
# The following example shows how to create a date object.

print("\n=== Creating a date object ===\n")

today = date.today()
print(f"Today is: {today}")
date_of_this_code = date(2024, 5, 23)
print(f"The date this code was written: {date_of_this_code}")

# Timedelta between two dates
# The timedelta class is used to represent a duration, or the difference between two dates or times.
# The following example shows how to calculate the difference between two dates.

print("\n=== Timedelta between two dates above ===\n")

difference = today - date_of_this_code
print(f"Diference in days: {difference.days}")

print("\n=== Creating a datetime object ===\n")
datetime_now = datetime.now()
datetime_code = datetime(2024, 5, 23, 15, 30, 0)

print(f"Date Time now: {datetime_now}")
print(f"Date Time this code was written: {datetime_code}")
print(f"Diference in time: {datetime_now - datetime_code}")
# Below we are using timedelta to subtract 2 hours and 2 days from the current time.
print(f"Subtracting 2 hours and 2 days using timedelta: {datetime_now - timedelta(hours=2, days=2)}")

date_birthday = datetime(1986, 4, 1, 18, 0, 0)
days_since_birthday = datetime_now - date_birthday
months_since_birthday = days_since_birthday.days // 30
years_since_birthday = months_since_birthday // 12

print("""
===== Life Stats =====
Days since my birthday: {day}
Months since my birthday: {month}
Years since my birthday: {year}
+++++++++++++++++++++++
""".format(day=days_since_birthday, month=months_since_birthday, year=years_since_birthday))


# Creating a time object
# The time class is used to represent a time.
# The time class takes three arguments: hour, minute, and second.

print("\n=== Creating a time object ===\n")

time_now = time(16, 14, 0)
print(f"Time now: {time_now}")

# Creating a timezone object
# The timezone class is used to represent a time zone.
# The timezone class takes two arguments: offset and name.
# The offset is the difference between the local time and UTC time.
# The name is the name of the time zone.
print("\n=== Creating a timezone object ===\n")

utc = timezone.utc
utc_time = datetime.now(utc)
print(f"UTC timezone: {utc}")
print(f"UTC time: {utc_time}")

gmt = timezone(timedelta(hours=1), "GMT")
gmt_time = datetime.now(gmt)
print(f"GMT timezone: {gmt}")
print(f"GMT time: {gmt_time}")

sp_timezone = timezone(timedelta(hours=-3), "America/Sao_Paulo")
sp_time = datetime.now(sp_timezone)
print(f"America/Sao_Paulo timezone: {sp_timezone}")
print(f"America/Sao_Paulo time: {sp_time}")


print("\n=== More examples using timedelta ===\n")
date1 = datetime(2024, 5, 23, 12, 0, 0)
print(f"Date 1: {date1}")
date = date1 + timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5)
print(f"Date changed for next week and 3 hours more: {date}")
