# Mate project documentation
----

## Python

----
### Main


---

### `Class` moterController

----

#### `Void` moterController.__init__(self, states, joystickOffset)
Called by defualt on object instantiation. The joystick offset is the default value of the joystick torque when stationary. The variable "states" is for defineing what joystick follow what controls. It looks like this.

topLeftMotor = motorController(
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
},
-0.00390625
)

----

#### `Float` moterController.safeDivide()
Division that catches the error `ZeroDivisionError` thrown when dividing by zero and returns 0.

----

#### `Void` moterController.update(self, joystick1X, joystick1Y, joystick2X, joystick2Y)
Updates the motors according to the joystick data passed.

----

## Arduino documentation
