from random import randint

temperature=randint(1,100)
print("TEMPERATURE is:",temperature)
humidity=randint(1,100)
print("HUMIDITY is:",humidity)
if temperature not in range(5,30):
    print("CAUTION! TEMPERATURE IS NOT NORMAL!!")
else:
    print("TEMPERATURE is NORMAL")
if humidity not in range(40,60):
    print("CAUTION! HUMIDITY IS NOT NORMAL!!")
else:
    print("HUMIDITY is NORMAL")
