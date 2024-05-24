# Python - Introduction to Object Oriented Programming in Python
# Making some operations using datetime.

from datetime import datetime, timedelta

print("======== Python - Introduction to Object Oriented Programming in Python ========")
print("=== Dates and Times ===")

car_size = 'small'  # small, medium, large
time_car_small = 30
time_car_medium = 45
time_car_large = 60
# actual_time = datetime.now(datetime.now().astimezone().tzinfo)

print("\n=== Car Washer - 30 for small, 45 for medium, 60 minutes for large ===\n")
actual_time = datetime.now()
print(actual_time)

if car_size == 'small':
    estimated_time = actual_time + timedelta(minutes=time_car_small)
    print(f"Car received at: {actual_time}, estimated time to finish: {estimated_time}")
elif car_size == 'medium':
    estimated_time = actual_time + timedelta(minutes=time_car_medium)
    print(f"Car received at: {actual_time}, estimated time to finish: {estimated_time}")
else:
    estimated_time = actual_time + timedelta(minutes=time_car_large)
    print(f"Car received at: {actual_time}, estimated time to finish: {estimated_time}")

# The code above is a simple car washer that receives a car and estimates the time to finish
# the washing based on the size of the car.
# The code uses the datetime module to get the current time and timedelta to add the time to finish the washing.
