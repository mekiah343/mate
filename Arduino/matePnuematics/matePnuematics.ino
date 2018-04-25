int switchPin = 8;
char message = '0';
int hydrolicsCooldown = 0;
bool hydrolicsActive = false;

void setup() {
  // Pin Setup
  pinMode(switchPin, OUTPUT);
  digitalWrite(switchPin, LOW);

  // Serial Setup
  Serial.begin(9600); // set the baud rate
  //Serial.println("Ready"); // print "Ready" once
  
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    message = Serial.read();
    if (message == '1') {
      digitalWrite(switchPin, HIGH);
    } else {
      digitalWrite(switchPin, LOW);
    }
  }

// Why 49? Because 49 is the ascii code for the character '1'
// Python sends 1 when the motors are active and 0 when they are not
// and because message is the type 'int' the char is converted to ascii

}

  
