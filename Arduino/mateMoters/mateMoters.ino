//Serial Initialization
int count = 0;
bool in_byte = false;
String package = "";
char message = '1';
char prev_message = '1';
String speedCharList[] = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"};
int potPin = 2;
int val = 0;
int lastpacket = 0;
int rightTrigger = 0;
int hydrolicsPin = 3;
bool hydrolicsActive = false;
int hydrolicsCooldown = 0;

//Motor speed
int bottomRightMotor = 1500;
int topRightMotor = 1500;
int topLeftMotor = 1500;
int bottomLeftMotor = 1500;

//Motor Initialization/pins
byte bottomRightMotorPin = 10;
byte topRightMotorPin = 9;
byte topLeftMotorPin = 6;
byte bottomLeftMotorPin = 5;

#include <Servo.h>
int light = 13;

Servo topRightServo;

Servo topLeftServo;

Servo bottomLeftServo;

Servo bottomRightServo;


void setup() {
//Hydrolics setup
pinMode(hydrolicsPin, OUTPUT);
digitalWrite(hydrolicsPin, LOW);

//Serial Setup
Serial.begin(9600); // set the baud rate
Serial.println("Ready"); // print "Ready" once

//Motor setup
pinMode(light, OUTPUT);
digitalWrite(light, LOW);

//Servos 
topLeftServo.attach(topLeftMotorPin);
topLeftServo.writeMicroseconds(1500);

bottomLeftServo.attach(bottomLeftMotorPin);
bottomLeftServo.writeMicroseconds(1500);

topRightServo.attach(topRightMotorPin);
topRightServo.writeMicroseconds(1500);

bottomRightServo.attach(bottomRightMotorPin);
bottomRightServo.writeMicroseconds(1500);
delay(2000);
digitalWrite(light, HIGH);
}
void loop() {
// Motor stuff
// Set signal value, which should be between 1100 and 1900
  //forward 
  //topLeftServo.writeMicroseconds(1300); 
  //delay(5000);
  //stop
  //topLeftServo.writeMicroseconds(1500); 
  //delay(1000);

  if (millis() - lastpacket > 100){
    val = analogRead(potPin);
    //Serial.println(Motor0);
    lastpacket = millis();
    count = count + 1;
  }

  if(rightTrigger == 49 and millis() - hydrolicsCooldown > 1000){
    hydrolicsActive = not hydrolicsActive;
    Serial.write(rightTrigger);
    hydrolicsCooldown = millis();
  }
  
  if (hydrolicsActive) {
    digitalWrite(hydrolicsPin, HIGH);
  } else{
    digitalWrite(hydrolicsPin, LOW);
  }


  
  if(Serial.available()){ // only send data back if data has been sent
     message = Serial.read(); // read the incoming data
     //Serial.println(message); // send the data back in a new line so that it is not all one long line
    if (message == '{') {
      in_byte = true;
      package = package + message;
    }
    else if (in_byte) {
      package = package + message;
      if (message == '}') {
        in_byte = false;
        topLeftMotor = (((package.charAt(1) - 75) * 40) + 1500);
        Serial.println(topLeftMotor);
        topRightMotor = (((package.charAt(2) - 75) * 40) + 1500);
        bottomRightMotor = (((package.charAt(3) - 75) * 40) + 1500);
        bottomLeftMotor = (((package.charAt(4) - 75) * 40) + 1500);
        rightTrigger = package.charAt(5);
        
        bottomRightServo.writeMicroseconds(bottomRightMotor); 
        bottomLeftServo.writeMicroseconds(bottomLeftMotor); 
        topLeftServo.writeMicroseconds(topLeftMotor); 
        topRightServo.writeMicroseconds(topRightMotor); 

        package = "";
      }
    }
  }
}
