import sys
a = int(sys.argv[1])
i = 1
def dec(a):
    if a == 1:
        print("%50s"%(f'{"*"}').center(50))
    else:
        print("%50s"%(f'{"*" * (a * 2 - 1)}').center(50))
        return dec(a - 1)
def inc(a):
    global i
    if a == i:
        pass
    else:
        print("%50s"%(f'{"*" * (i * 2 - 1)}').center(50))
        i += 1
        return inc(a)
inc(a)
dec(a)

#Şükriye Öztürk 2210356110
