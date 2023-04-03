import sys
number = int(sys.argv[1]) ** int(sys.argv[2])
try:
    numberdigit = [int(x) for x in str(number)]                              #bu birinci sonuç
    if len(numberdigit) > 1:
        c = sum(numberdigit)                     #a burada üslü sayının rakamları toplamı                                    #bu ikinci sonuç
        a = [int(x) for x in str(c)]             #burada ise üslünün rakamları toplamının rakamlarının list hali
        for i in range(len(a)):
            b = sum(a)                           #üçüncü sonuç
            break
        print((sys.argv[1])+"^"+(sys.argv[2])+" = "+str(number)+" = "+str(numberdigit)+" = "+str(c)+" = "+str(c)+" = "+str(b))
    else:
        print((sys.argv[1])+"^"+(sys.argv[2])+" = "+str(number))
except:
    print("You cannot enter a negative number.")

#Şükriye Öztürk 2210356110