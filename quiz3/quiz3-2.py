import sys
lucky_numbers = list(sys.argv[1:])
lucky_numbers = lucky_numbers[0].split(",")
a = 2
try:
    for i in range(1, 10, a):
        lucky_numbers.remove(lucky_numbers[i])
        a += 1
except:
    print(*lucky_numbers)
print(*lucky_numbers)
#Şükriye Öztürk 2210356110