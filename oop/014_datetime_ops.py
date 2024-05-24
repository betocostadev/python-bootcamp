# Python - Introduction to Object Oriented Programming in Python
# Making some operations using datetime.

from datetime import datetime, timedelta

print("\n======== Python - Introduction to Object Oriented Programming in Python ========\n")
print("Dealing with timedelta")

options = """
============== Car Washer - Options ==============
Please, select the size of your car:
1 - Small
2 - Medium
3 - Large
"""
car_size = ''

while car_size not in ['1', '2', '3']:
    car_size = input(options)  # small, medium, large
    if car_size not in ['1', '2', '3']:
        print("Invalid option. Please, try again.")

if car_size == '1':
    car_size = 'small'
elif car_size == '2':
    car_size = 'medium'
else:
    car_size = 'large'

time_car_small = 30
time_car_medium = 45
time_car_large = 60
# actual_time = datetime.now(datetime.now().astimezone().tzinfo)

actual_time = datetime.now()

if car_size == 'small':
    estimated_time = actual_time + timedelta(minutes=time_car_small)
elif car_size == 'medium':
    estimated_time = actual_time + timedelta(minutes=time_car_medium)
else:
    estimated_time = actual_time + timedelta(minutes=time_car_large)

print("\n============== Car Washer - Status ==============")
print(f"Car received at: {actual_time}. Car size: {car_size}")
print(f"Estimated time to finish: {estimated_time}")
# The code above is a simple car washer that receives a car and estimates the time to finish
# the washing based on the size of the car.
# The code uses the datetime module to get the current time and timedelta to add the time to finish the washing.
