int temp_data=0;
void setup()
{
  pinMode(A0,INPUT);
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  pinMode(5,OUTPUT);
}

void loop()
{
  temp_data=analogRead(A0);
  Serial.println(temp_data);
  
  if(temp_data<154){
    digitalWrite(13,HIGH);
    digitalWrite(5,HIGH);
   }
  else{
    digitalWrite(13,LOW);
    digitalWrite(5,LOW);
  }
}