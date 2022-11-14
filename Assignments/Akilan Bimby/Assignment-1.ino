int temp_data=0;
void setup()
{
  pinMode(A1,INPUT);
  Serial.begin(9600);
  pinMode(11,OUTPUT);
  pinMode(7,OUTPUT);
}

void loop()
{
  temp_data=analogRead(A1);
  Serial.println(temp_data);
  
  if(temp_data<154){
    digitalWrite(11,HIGH);
    digitalWrite(7,HIGH);
   }
  else{
    digitalWrite(11,LOW);
    digitalWrite(7,LOW);
  }
}