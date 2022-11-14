from random import randint

temp=randint(1,100)
print("TEMPERATURE is:",temp)
humi=randint(1,100)
print("HUMIDITY is:",humi)
if temp not in range(5,30):
    print("CAUTION! TEMPERATURE IS NOT NORMAL!!")
else:
    print("TEMPERATURE is NORMAL")
if humi not in range(40,60):
    print("CAUTION! HUMIDITY IS NOT NORMAL!!")
else:
    print("HUMIDITY is NORMAL")
