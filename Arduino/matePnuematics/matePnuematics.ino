int clawPin = 8;
int airPin = 7;
char message = '0';
bool in_byte = true;
String package = "";
char clawByte = '0';
char airByte = '0';


void setup() {
  Serial.begin(9600); // set the baud rate
  // Pin Setup
  pinMode(clawPin, OUTPUT);
  digitalWrite(clawPin, LOW);

  pinMode(airPin, OUTPUT);
  digitalWrite(airPin, LOW);

  // Serial Setup
  //Serial.println("Ready"); // print "Ready" once

}

void loop() {
  // put your main code here, to run repeatedly:
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
        clawByte = package.charAt(1);
        airByte = package.charAt(2);
        package = "";
      }

    if (clawByte == '1') {
      digitalWrite(clawPin, HIGH);
    } else {
      digitalWrite(clawPin, LOW);
    }

    if (airByte == '1') {
      digitalWrite(airPin, HIGH);
    } else {
      digitalWrite(airPin, LOW);
    }

  }
 }
}
