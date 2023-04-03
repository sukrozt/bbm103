
import sys

try:
    BasketTwo = 2 * int(sys.argv[1])
    BasketThree = 3 * int(sys.argv[2])
    FreeThrow = int(sys.argv[3])
    TotalPoints = BasketTwo + BasketThree + FreeThrow
    print(TotalPoints)
except:
    pass

def healthStatus(height,mass):
    BMIvalue = mass / (height **2)
    if BMIvalue >= 30:
        return "obese"
    elif 24.9 <= BMIvalue < 30: 
        return "overweight"
    elif 18.5 <= BMIvalue < 24.9:
        return "healthy"
    else:
        return "underweight"


#Şükriye Öztürk 2210356110