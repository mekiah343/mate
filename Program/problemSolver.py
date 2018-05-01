from __future__ import print_function

import math
import matplotlib

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import os


takeOffPoints = [[360.34, 353.585],[450, 1170.43]]



indexTakeOff = int(raw_input("navel 0 or renton 1?"))
airFieldStart = takeOffPoints[indexTakeOff]



#(In meters per second.)

heading = float(raw_input("Heading: "))

ascent_airSpeed = float(raw_input("Ascent air speed: "))
ascent_rate = float(raw_input("Ascent rate: "))

engineFailureTime = float(raw_input("Engine failure time: "))

desent_airSpeed = float(raw_input("Desent air speed: "))
desent_rate = float(raw_input("Desent rate: "))

wind_direction = float(raw_input("Wind direction: "))
wind_speed = float(raw_input("Wind Speed: "))


ascent_distance = ascent_airSpeed * engineFailureTime
ascent_maxAltitude = ascent_rate * engineFailureTime

desent_time = ascent_maxAltitude / desent_rate

crash_distance = desent_time * desent_airSpeed 

wind_distance = wind_speed * desent_time
wind_direction = wind_direction - 180

if indexTakeOff == 0:
	travelY = -math.cos(math.radians(heading)) * crash_distance

	travelX = math.sin(math.radians(heading)) * crash_distance

	windY = -math.cos(math.radians(wind_direction)) * wind_distance
	windX = math.sin(math.radians(wind_direction)) * wind_distance
if indexTakeOff == 1:
	travelY = -math.cos(math.radians(heading)) * crash_distance

	travelX = math.sin(math.radians(heading)) * crash_distance

	windY = -math.cos(math.radians(wind_direction)) * wind_distance
	windX = math.sin(math.radians(wind_direction)) * wind_distance


print("")

print("Desent time is " + str(desent_time))

print("Ascent distance is " + str(ascent_distance))

print("Crash distance is " + str(crash_distance))

print("Wind distance is " + str(wind_distance))


print(wind_direction)


travelX = (travelX / 500) * 44.482

travelY = (travelY / 500) * 44.482


windX = (windX / 500) * 44.482

windY = (windY / 500) * 44.482


finalX = travelX + windX
finalY = travelY + windY

travelX = airFieldStart[0] + travelX
travelY = airFieldStart[1] + travelY

finalX = airFieldStart[0] + finalX
finalY = airFieldStart[1] + finalY


# A sample image
cwd = os.getcwd()
with cbook.get_sample_data(str(cwd) + '/map.png') as image_file:
    image = plt.imread(image_file)

fig, ax = plt.subplots()
ax.imshow(image)
ax.axis('off')  # clear x- and y-axes


# And another image

w, h = 512, 512

# with cbook.get_sample_data('ct.raw.gz', asfileobj=True) as datafile:
#     s = datafile.read()
# A = np.fromstring(s, np.uint16).astype(float).reshape((w, h))
# A /= A.max()

# fig, ax = plt.subplots()
# extent = (0, 25, 0, 25)
# im = ax.imshow(A, cmap=plt.cm.hot, origin='upper', extent=extent)

# markers = [(15.9, 14.5), (16.8, 15)]
# x, y = zip(*markers)
# ax.plot(x, y, 'o')

# ax.set_title('CT density')


markers = [(travelX, travelY), airFieldStart, (finalX, finalY)]

x, y = zip(*markers)
ax.plot(x, y, 'o')

plt.show()

