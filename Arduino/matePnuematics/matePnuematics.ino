int switchPin = 9;
String message = "";
int hydrolicsCooldown = 0;
bool hydrolicsActive = false;

void setup() {
  // Pin Setup
  pinMode(switchPin, OUTPUT);
  digitalWrite(switchPin, LOW);

  // Serial Setup
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" once
  
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    message = Serial.read();
    Serial.println(message); // print "Ready" once
  }

  if(message == 49 and millis() - hydrolicsCooldown > 1000){
    hydrolicsActive = not hydrolicsActive;
    Serial.write(rightTrigger);
    hydrolicsCooldown = millis();
  }
}

if (hydrolicsActive) {
    digitalWrite(switchPin, HIGH);
  } else{
    digitalWrite(switchPin, LOW);
  }
