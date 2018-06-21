# Find the highest value of velocity that is not in a cabel area / squigily line
from math import pi

seaWaterDensity = 1025 # kg/m^3

turbineDiameter =  float(raw_input("Diameter of turbines: "))
turbineRadius = turbineDiameter / 2
turbineArea = (turbineRadius * turbineRadius) * pi

efficiencyValue = float(raw_input("Efficiency Value (Decimal): "))

turbineCount = float(raw_input("Number of turbines: "))

turbineCount = turbineCount / 2

velocityKnots = float(raw_input("Velocity in knots: "))

# Cube it
velocitySquared = velocityKnots * velocityKnots * velocityKnots

# Knots into meters per second
velocityMPS = velocitySquared * 0.514444

solution = turbineCount * (seaWaterDensity * turbineArea * velocityMPS * efficiencyValue)

print(solution)
