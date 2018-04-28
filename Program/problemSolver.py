import math

# (In meters per second.)

heading = raw_input("Heading: ")

ascent_airSpeed = raw_input("Ascent air speed: ")
ascent_rate = raw_input("Ascent rate: ")

engineFailureTime = raw_input("Engine failure time: ")

desent_airSpeed = raw_input("Desent air speed: ")
desent_rate = raw_input("Desent rate: ")

wind_direction = raw_input("Wind direction: ")
wind_speed = raw_input("Wind Speed: ")


ascent_distance = ascent_airSpeed * engineFailureTime
ascent_maxAltitude = ascent_rate * engineFailureTime

desent_time = ascent_maxAltitude / desent_rate

crash_distance = desent_time * desent_airSpeed 

wind_distance = wind_speed * desent_time

print("")

print("Ascent distance is " + ascent_distance)

print("Crash distance is " + ascent_distance)

print("Wind distance is " + ascent_distance)

