// this programme will receive then send the same data to Raspberry using serial communication

String data="";
void setup() {
  Serial.begin(115200);
}

void loop() {

 if (Serial.available())
 {
  data = Serial.readStringUntil('\n');
  Serial.println(data);
  delay(10);
 }
}
