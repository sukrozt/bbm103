import sys
import os
try:
    operands = []
    comps = []
    openoperands = open(sys.argv[1], "r")
    opencomparisondata = open(sys.argv[2], "r")
    operand = list(openoperands.read().splitlines())
    comparisondata = list(opencomparisondata.read().splitlines())
    def roundy(x):
        if float(x) - int(float(x)) >= 0.5:
            return int(float(x)) + 1
        else:
            return int(float(x))
    for i in range(len(operand)):
        try:
            comps.append(comparisondata[i].split(" "))
            operands.append(operand[i].split(" "))
            div = roundy(operands[i][0])
            divmod = roundy(operands[i][1])
            rangeof = list(range(roundy(operands[i][2]), roundy(operands[i][3])+1))
            print("-" * 12)
            myresults = []
            for x in rangeof:
                if x % div == 0 and x % divmod != 0:
                    myresults.append(x)
            print("My results:\t\t",*myresults)
            print("Results to compare:\t", *comps[i])
            [str(myresults) for i in range(len(myresults))]
            assert len(myresults) == len(comps[i])
        except AssertionError:
            print("AssertionError: results don’t match.")
        except ZeroDivisionError:
            print("ZeroDivisionError: You can’t divide by 0.\nGiven input: ",*operands[i])
        except ValueError:
            print("-" * 12)
            print("ValueError: only numeric input is accepted.\nGiven input: ",*operands[i])
        except IndexError:
            print("-" * 12)
            print("IndexError: number of operands less than expected.\nGiven input:",*operands[i])
        except:
            print("-" * 12)
            print("kaBOOM: run for your life!")
        else:
            print("Goool!!!")
except IndexError:
    if len(sys.argv) > 2:
            print("IndexError: there is no comparison data to compare.")
    else:
        print("IndexError: number of input files less than expected.")
except IOError:
    if os.path.exists(f'{os.path.abspath(os.getcwd())}/{sys.argv[1]}') == False and os.path.exists(f'{os.path.abspath(os.getcwd())}/{sys.argv[1]}') == False:
        probleminput = f"{sys.argv[1]} and {sys.argv[2]}"
    elif os.path.exists(f'{os.path.abspath(os.getcwd())}/{sys.argv[1]}') == False:
        probleminput = f"{sys.argv[1]}"
    else:
        probleminput = f"{sys.argv[2]}"
    finalmessage = f"IOError: cannot open {probleminput}"
    print(finalmessage)
finally:
    print("\n˜ Game Over ˜")

#Şükriye Öztürk 2210356110
