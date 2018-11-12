# 201358937 Tonge_Brandon-CA02.py
# October 2018
# This program will calculate the distance travelled, the
# horizonal distance, the vertical distance and the battery drain
# of a robot when the user inputs an angle and a travel time.

print("This program will calculate the distance travelled, the\n\
horizonal distance, the vertical distance and the battery drain\n\
of a robot when the user inputs an angle and a travel time.")
print()

# Define variables and libraries that are going to be used
import math
speed = 1.5

# Explain and accept inputs from the user
angle_degree = float(input("Please enter an angle in degrees: "))
travel_time = float(input("Please enter a travel time in seconds: "))

# Input conversions
angle_radian = math.radians(angle_degree)

# Calculations for the program
distance = speed * travel_time
horizontal = distance * math.sin(angle_radian)
vertical = distance * math.cos(angle_radian)
battery_estimate = travel_time * 2.7

# User Outputs
print()
print("The distance travelled is: {0:.2f}".format(distance), "Meters")
print("The horizontal distance is: {0:.2f}".format(horizontal), "Meters")
print("The vertical distance is {0:.2f}".format(vertical), "Meters")
print("Estimated battery usage: {0:.2f}".format(battery_estimate))

# TEST
# print()
# print("The robot will move at:" , str(speed) , "Meters a second")
# print("The distance travelled is: {0:.2f}" .format(distance) ,"Meters")
# print("The angle in degrees is: {0:.2f}" .format(angle_degree))
# print("The angle converted to radians is: {0:.2f}" .format(angle_radian))
# print("The horizontal distance is: {0:.2f}" .format(horizontal) , "Meters")
# print("The vertical distance is {0:.2f}" .format(vertical) , "Meters")
# print("Estimated battery usage: {0:.2f}" .format(battery_estimate))
