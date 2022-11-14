from random import randint

tm=randint(1,100)
print("TEMPERATURE :",tm)
hm=randint(1,100)
print("HUMIDITY :",hm)
if tm not in range(5,30):
    print("CAUTION! TEMPERATURE IS NOT NORMAL!!")
else:
    print("TEMPERATURE is NORMAL")
if hm not in range(40,60):
    print("CAUTION! HUMIDITY IS NOT NORMAL!!")
else:
    print("HUMIDITY is NORMAL")
