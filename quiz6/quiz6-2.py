import sys
a = int(sys.argv[1])
stars = [print("%50s" % (f'{"*"*(x * 2 - 1)}').center(50)) for x in range(1, a + 1)]
[print("%50s" % (f'{"*"*(x * 2 - 1)}').center(50)) for x in range(a-1, 0, -1)]

#Şükriye Öztürk 2210356110