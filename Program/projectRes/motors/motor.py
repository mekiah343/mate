from __future__ import division

class motorController:
	def __init__(self , states, joystickOffset):
		# Defining the offset of the joysticks
		self.joystickOffset = joystickOffset
		
		# Default states
		self.states = [
			{
				"joystick1xStates":{
					1:0,
					0:0,
					-1:0
				},
	    		"joystick1yStates":{
	    			1:0,
					0:0,
					-1:0
	    		},
	        	"joystick2xStates":{
	        		1:0,
					0:0,
					-1:0
	        	},
	        	"joystick2yStates":{
					1:0,
					0:0,
					-1:0
	        	}
        	}
        ]
        # Imported states
		self.states = states

		# Active Axis
		self.joystick1Xon = 0
		self.joystick1Yon = 0
		self.joystick2Xon = 0
		self.joystick2Yon = 0

		# Axis Force
		self.joystick1Xtorque = 0
		self.joystick1Ytorque = 0
		self.joystick2Xtorque = 0
		self.joystick2Ytorque = 0

		# Moter output
		self.moterOutput = 0
		
	# Called every frame
	def update(self, joystick1X, joystick1Y, joystick2X, joystick2Y):
		
		self.joystick1Xon = self.safeDivide((joystick1X + self.joystickOffset), abs(joystick1X + self.joystickOffset))
		self.joystick1Yon = self.safeDivide((joystick1Y + self.joystickOffset), abs(joystick1Y + self.joystickOffset))
		self.joystick2Xon = self.safeDivide((joystick2X + self.joystickOffset), abs(joystick2X + self.joystickOffset))
		self.joystick2Yon = self.safeDivide((joystick2Y + self.joystickOffset), abs(joystick2Y + self.joystickOffset))

		self.joystick1Xtorque = abs(joystick1X)
		self.joystick1Ytorque = abs(joystick1Y)
		self.joystick2Xtorque = abs(joystick2X)
		self.joystick2Ytorque = abs(joystick2Y)
		
		

		self.moterOutput = (self.joystick1Xtorque * self.states[0]["joystick1xStates"][self.joystick1Xon]) + (self.joystick1Ytorque * self.states[0]["joystick1yStates"][self.joystick1Yon]) + (self.joystick2Xtorque * self.states[0]["joystick2xStates"][self.joystick2Xon]) + (self.joystick2Ytorque * self.states[0]["joystick2yStates"][self.joystick2Yon])

		if (self.moterOutput > 1):
			self.moterOutput = 1

		if (self.moterOutput < -1):
			self.moterOutput = -1




	def safeDivide(self,x,y):
	    try:
	        return x/y
	    except ZeroDivisionError:
	        return 0




