#include <Servo.h>

  
//Global variables-----------------------------------------------------------------------------------------
int servoPosition = 0;    // The servoPosition variable will be used to set the position of the servo
byte DTMFread;            // The DTMFread variable will be used to interpret the output of the DTMF module.
const int STQ = 3;        // Attach DTMF Module STQ Pin to Arduino Digital Pin 3
 const int Q4 = 4;        // Attach DTMF Module Q4  Pin to Arduino Digital Pin 4
 const int Q3 = 5;        // Attach DTMF Module Q3  Pin to Arduino Digital Pin 5

Servo SG5010;             // The SG5010 variable provides Servo functionality
 const int Q2 = 6;        // Attach DTMF Module Q2  Pin to Arduino Digital Pin 6
 const int Q1 = 7;        // Attach DTMF Module Q1  Pin to Arduino Digital Pin 7
int code[]={2,3,1,5};
int C_indx=0;

/*=========================================================================================================
setup() : will setup the Servo, and prepare the Arduino to receive the MT8700 DTMF module's output.
========================================================================================================== */
void setup() {
   
  
  SG5010.attach(9);             // The Servo signal cable will be attached to Arduino Digital Pin 9
  SG5010.write(servoPosition);  // Set the servo position to zero.

  //Setup the INPUT pins on the Arduino
  pinMode(STQ, INPUT);
  pinMode(Q4, INPUT);
  pinMode(Q3, INPUT);
  pinMode(Q2, INPUT);
  pinMode(Q1, INPUT);
  Serial.begin(9600);
}

/*=========================================================================================================
loop() : Arduino will interpret the DTMF module output and position the Servo accordingly
========================================================================================================== */
void loop() { 
    if(Serial.available()>0)
    char letter = Serial.read();
   if(digitalRead(STQ)==HIGH){  
if (DTMF_Detect() == code[C_indx]) {       //When a DTMF tone is detected, STQ will read HIGH for the duration of the tone.
    C_indx = C_indx+1;
    Serial.println("GOT NUMBER");
    } else { 
      C_indx=0;
      Serial.println("BAD NUMBER");
    }
    if (C_indx == 4)  {
    Serial.println("yeet");
    servoPosition = 1500;
    SG5010.write(servoPosition);
    delay(5000);
    C_indx = 0; }
   while (digitalRead(STQ)==HIGH){
   delay(10);}
   }
  
          //Set the servo's position according to the "servoPosition" variable.

}

int DTMF_Detect(){

   DTMFread=0;

    if(digitalRead(Q1)==HIGH){      //If Q1 reads HIGH, then add 1 to the DTMFread variable
      DTMFread=DTMFread+1;
    }
    if(digitalRead(Q2)==HIGH){      //If Q2 reads HIGH, then add 2 to the DTMFread variable
      DTMFread=DTMFread+2;
    }
    if(digitalRead(Q3)==HIGH){      //If Q3 reads HIGH, then add 4 to the DTMFread variable
      DTMFread=DTMFread+4;
    }
    if(digitalRead(Q4)==HIGH){      //If Q4 reads HIGH, then add 8 to the DTMFread variable
      DTMFread=DTMFread+8;
    }
    return DTMFread;
}
