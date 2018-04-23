import pygame
import serial
import re
import sys
import glob
from projectRes.motors.motor import motorController

print("Booting MUROVISP...")








# ______________________________________________
# Text drawing functions
# ______________________________________________

# Class for printing the text on the left hand side
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 27)

    def drawText(self, screen, textString):
        textBitmap = self.font.render(textString, True, WHITE)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 20
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10

# ______________________________________________
# Extras for ease of use
# ______________________________________________
def consoleBreakLine(_breaks=1):
    for i in range(_breaks):
        print("")


# ______________________________________________
# Serial Port Connection
# ______________________________________________

def getPort(_prompt):
    availablePorts = serial_ports()
    # Check if the specified port index exists
    for i, port in enumerate(availablePorts):
        print(str(i) + ": " + port)

    consoleBreakLine()

    index = raw_input(_prompt)

    if index == '':
        consoleBreakLine(2)
        return False



    # Check if the input is an int
    try:
        index = int(index)
    except ValueError:
        raw_input('[Error]: Input not an intiger. Press enter to continue.')
        consoleBreakLine()
        getPort(_prompt)

    # Attempt to get an index of the ports list, method restarts if index does not exist
    try:
        selectedPort = availablePorts[index]
        return selectedPort
    except IndexError:
        raw_input('[Error]: Port not available, select a valid port. Press enter to continue.')
        consoleBreakLine()
        getPort(_prompt)

# Returns a list of serial ports
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

# Add a break

# __name__ is a special variable in python set when the program first runs, it returns '__main__'
# unless it is in a module
if __name__ == '__main__':
    # Puts index in 'i' and port in 'port' and then I print them out for easy selection
    consoleBreakLine()

    moterPort = getPort("Select a port for moters: ")

    #clawPort = getPort("Select a port for claw: ")



# ______________________________________________
# Serial communication variable initializations
# ______________________________________________

# Defineing serial port

if moterPort != False:
    moterArduino = serial.Serial(moterPort, 9600) # Establish the connection on a specific port
# if clawPort != False:
#     clawArduino = serial.Serial(clawPort, 9600) # Establish the connection on a specific port

# Serial packet variables
packet = ""
packet_rec = False
inbyte = ""

    

# ______________________________________________
# Color variable initializations
# ______________________________________________

BLACK    = (0, 0, 0)
WHITE    = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# ______________________________________________
# Pygame variable initializations
# ______________________________________________

# Initialize pygame
pygame.init()
   
# Set the width and height of the screen [width,height]
size = [900, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mekiah's Underwater Remotely Operated Vehicle Independent Software Project")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
textPrint = TextPrint()
DISPLAY_WIDTH = 500 # screen width in pixels
DISPLAY_HEIGHT = 700 # screen height in pixels
DW_HALF = DISPLAY_WIDTH / 2
DH_HALF = DISPLAY_HEIGHT / 2

# ______________________________________________
# Moter object initializations
# ______________________________________________
#   + First parameter is the control scheme
#   + Second parameter is the offset of the joystick when they are at rest.


topLeftMotor = motorController(
    [        
        {
            "joystick1xStates":{
                1:-1,
                0:0,
                -1:1
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
                1:-1,
                0:0,
                -1:1
            }
        }
    ],
    -0.00390625
)

topRightMotor = motorController(
    [        
        {
            "joystick1xStates":{
                1:1,
                0:0,
                -1:-1
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
                1:-1,
                0:0,
                -1:1
            }
        }
    ],
    -0.00390625
)

bottomLeftMotor = motorController(
    [        
        {
            "joystick1xStates":{
                1:0,
                0:0,
                -1:0
            },
            "joystick1yStates":{
                1:1,
                0:0,
                -1:-1
            },
            "joystick2xStates":{
                1:-1,
                0:0,
                -1:1
            },
            "joystick2yStates":{
                1:0,
                0:0,
                -1:0
            }
        }
    ],
    -0.00390625
)

bottomRightMotor = motorController(
    [        
        {
            "joystick1xStates":{
                1:0,
                0:0,
                -1:0
            },
            "joystick1yStates":{
                1:1,
                0:0,
                -1:-1
            },
            "joystick2xStates":{
                1:1,
                0:0,
                -1:-1
            },
            "joystick2yStates":{
                1:0,
                0:0,
                -1:0
            }
        }
    ],
    -0.00390625
)

print topLeftMotor.states

motor0 = 0
motor1 = 0
motor2 = 0
motor3 = 0


# ______________________________________________
# Moter controller packet variable initializations
# ______________________________________________

# * K is stationary
# * A is full reverse
# * U is full forward
# Can only send 1 char at a time, must send analog joystick speeds as different chars.
activeMotorCharList = ["V","W","X","Y"]
speedCharList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"]
messageToArduino = ""

# ______________________________________________
# Robot sensor/other parts variable initializations
# ______________________________________________
pot = 0

# ______________________________________________
# Moter variables initializations
# ______________________________________________

motorVisualOffsetX = 200
motorVisualOffsetY = -225
joystickVisualOffsetX = 0
joystickVisualOffsetY = 0

while done == False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        #if event.type == pygame.JOYBUTTONDOWN:
            #print("Joystick button pressed.")
        #if event.type == pygame.JOYBUTTONUP:
            #print("Joystick button released.")
            
 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    # textPrint.drawText(screen, "Number of joysticks: {}".format(joystick_count) )
    # textPrint.indent()
    
    # For each joystick:
    textPrint.drawText(screen, "Joystick Thrust:")
    textPrint.indent()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        name = joystick.get_name()
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()


    pygame.draw.circle(screen, (255,255,255), (DW_HALF + motorVisualOffsetX, DH_HALF + motorVisualOffsetY), 100, 0)    # EVENT PROCESSING STEP
    

    # ______________________________________________
    # Moter updating and serial communication
    # ______________________________________________


    # Axis 1 = L joystick horizontal, Axis 2 = L joystick vertical, Axis 2 is some conbination of all axis, Axis 3 = R joystick horizonal, Axis 4 = R joystick vertical
    topLeftMotor.update(joystick.get_axis(0), joystick.get_axis(1), joystick.get_axis(3), joystick.get_axis(4))
    
    topRightMotor.update(joystick.get_axis(0), joystick.get_axis(1), joystick.get_axis(3), joystick.get_axis(4))

    bottomLeftMotor.update(joystick.get_axis(0), joystick.get_axis(1), joystick.get_axis(3), joystick.get_axis(4))

    bottomRightMotor.update(joystick.get_axis(0), joystick.get_axis(1), joystick.get_axis(3), joystick.get_axis(4))


    topLeftMoterByte = str(speedCharList[int(round((topLeftMotor.moterOutput + 0.004) * 10)) + 10])

    topRightMotorByte = str(speedCharList[int(round((topRightMotor.moterOutput + 0.004) * 10)) + 10])

    bottomLeftMotorByte = str(speedCharList[int(round((bottomLeftMotor.moterOutput + 0.004) * 10)) + 10])

    bottomRightMotorByte = str(speedCharList[int(round((bottomRightMotor.moterOutput + 0.004) * 10)) + 10])

    button = str(joystick.get_button(7))
    
    
    # Compiling the moter speeds into one packet for the arduino
    messageToMoterArduino = "{" + topLeftMoterByte + topRightMotorByte + bottomLeftMotorByte + bottomRightMotorByte + button + "}"
    print(messageToMoterArduino)
    moterArduino.write(messageToMoterArduino) #message to arduino

    # if clawPort != False:
    #     messageToClawArduino = button
    #     clawArduino.write(messageToClawArduino)

    
    pygame.draw.circle(screen, (255,255,255), (DW_HALF + joystickVisualOffsetX + int(round((joystick.get_axis(0) * 30))), DH_HALF + joystickVisualOffsetY + int(round(joystick.get_axis(1) * 30))), 20, 0)    # EVENT PROCESSING STEP



    textPrint.indent()
    for i in range( axes ):
        axis = joystick.get_axis( i )
        textPrint.drawText(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
    textPrint.unindent()

    buttons = joystick.get_numbuttons()
    textPrint.unindent()
    textPrint.drawText(screen, "Number of buttons: {}".format(buttons) )
    textPrint.indent()
    
    
    for i in range( buttons ):
        button = joystick.get_button( i )
        textPrint.drawText(screen, "Button {:>2} value: {}".format(i,button) )
    textPrint.unindent()
   
    if moterPort != False:
        if moterArduino.in_waiting > 0:
            pot = moterArduino.readline()

    # print(pot)
    textPrint.drawText(screen, "Diagnostics:")
    textPrint.indent()
    textPrint.drawText(screen, "Potentiometer 1: " + re.sub('\W+','', str(pot)))
        

    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(75)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
moterArduino.close()
pygame.quit ()
