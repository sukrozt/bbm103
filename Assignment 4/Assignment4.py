import sys
import os

row1, column1, row2, column2 = {}, {}, {}, {} #rows for the board which has the exact locations of ships, columns for board which shows shot ships
allalphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
               "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "Y", "Z"]
alphabet = allalphabet[:10]
indexnumbers, indexalphabet = [], []  #indexnumbers list for the row number of input, indexalphabet list for the column letter of input
output = open("Battleship.out", "w")
for a in range(10): #I created dictionary in dictionary for every row of board
    row1[a + 1] = {}
    column1[a + 1] = {}
    row2[a + 1] = {}
    column2[a + 1] = {}
carrier1, destroyer1, submarine1, destroyer2, submarine2, carrier2 = "-", "-", "-", "-", "-", "-" #they are the indicator for if ships are sank or not
patrolboat1, battleship1, patrolboat2, battleship2 = ["-", "-", "-", "-"], ["-", "-"], ["-", "-", "-", "-"], ["-", "-"]
counterS2, shipcounter2, shipcounter1, counterP14, counterP13, counterP12, counterP11, counterB12, counterB11, counterD2, counterC2, counterS1, counterB21, counterD1, counterC1, counterP24, counterP23, counterB22, counterP22, counterP21 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  #they're for all the part of a ship is shot or not
(T1, T2, T3, T4, B1, B2, T5, T6, T7, T8, B3, B4) = (False, False, False, False, False, False, False, False, False, False, False, False) #they are for multiple ships
def getinput(*p):
    global listindex, row1, row2, problematic
    problematic = []
    for k in p:
        if not os.path.exists(k):
            problematic.append(k)
    for k in p:
        openinput = open(k, "r")
        listinputfile = list(openinput.read().splitlines())
        if ".txt" in k:
            for a in range(10):
                for x in range(10):
                    newlist = listinputfile[a].split(";")
                    if k == sys.argv[1]:
                        row1[a + 1][alphabet[x]] = newlist[x]
                        column1[a + 1][alphabet[x]] = "-"
                    if k == sys.argv[2]:
                        row2[a + 1][alphabet[x]] = newlist[x]
                        column2[a + 1][alphabet[x]] = "-"
        elif ".in" in k:
            listindex = []
            for x in range(len(listinputfile)):
                listindex = (listinputfile[x].split(";"))
                listindex.remove('')
def ships(x):
    global mulships
    mulships = []                                           #this is the list of list of optional player inputs
    optional = open(x, "r")
    optionallist = list(optional.read().splitlines())
    for i in range(len(optionallist)):
        optionalelements = optionallist[i].split(";")
        ship = optionalelements[0].split(":")
        position = ship[1].split(",")
        splittedoptional = ship + position
        splittedoptional.append(optionalelements[1])
        mulships.append(splittedoptional)

def play1(i):
    try:
        global indexnumbers, indexalphabet, listindex, submarine2, destroyer2, carrier2, patrolboat2, battleship2, counterC2, counterS2, counterD2, counterB21, counterB22, counterP21, counterP22, counterP23, counterP24, shipcounter2, T1, T2, T3, T4, B1, B2
        if len(listindex[i]) < 3:
            raise IndexError
        listindex = listindex[i].split(",")
        indexnumbers = int(listindex[0])
        indexalphabet = listindex[1]
        if indexalphabet == '':
            raise IndexError
        if len(listindex) > 2 or indexalphabet not in allalphabet:
            raise ValueError
        getoutput(f"")
        getoutput(f"\n\nPlayer1's Move\n\n")
        getoutput(f"Round : {i+1}\t\t\t\t\tGrid Size: 10x10\n\n")
        board()
        getoutput("")
        getoutput(f"\nEnter your move: {indexnumbers},{indexalphabet}")
        assert int(indexnumbers) in range(1, 11)
        assert indexalphabet in alphabet
        assert column2[int(indexnumbers)][indexalphabet[0]] == '-'
        ships("OptionalPlayer2.txt")
        if row2[int(indexnumbers)][indexalphabet[0]] == '':
            column2[int(indexnumbers)][indexalphabet[0]] = "O"
        elif row2[int(indexnumbers)][indexalphabet[0]] == 'C':
            column2[int(indexnumbers)][indexalphabet[0]] = "X"
            counterC2 += 1
            if counterC2 == 5:
                carrier2 = "X"
                shipcounter2 += 1
        elif row2[int(indexnumbers)][indexalphabet[0]] == 'D':
            column2[int(indexnumbers)][indexalphabet[0]] = "X"
            counterD2 += 1
            if counterD2 == 3:
                destroyer2 = "X"
                shipcounter2 += 1
        elif row2[int(indexnumbers)][indexalphabet[0]] == 'S':
            column2[int(indexnumbers)][indexalphabet[0]] = "X"
            counterS2 += 1
            if counterS2 == 3:
                submarine2 = "X"
                shipcounter2 += 1
        elif row2[int(indexnumbers)][indexalphabet[0]] == 'P':
            column2[int(indexnumbers)][indexalphabet[0]] = "X"
            if not T1:
                if mulships[2][4] == "right":
                    for a in range(alphabet.index(mulships[2][3]), alphabet.index(mulships[2][3]) + 2):
                        if column2[int(mulships[2][2])][alphabet[a]] == "X":
                            counterP21 += 1
                        else:
                            counterP21 = 0
                        if counterP21 == 2:
                            counterP21 = 0
                            patrolboat2.insert(0, "X")
                            T1 = True
                            shipcounter2 += 1
                            patrolboat2.pop()
                elif mulships[2][4] == "down":
                    for a in range(int(mulships[2][2]), int(mulships[2][2]) + 2):
                        if column2[a][(mulships[2][3])] == "X":
                            counterP21 += 1
                        else:
                            counterP21 = 0
                        if counterP21 == 2:
                            counterP21 = 0
                            patrolboat2.insert(0, "X")
                            T1 = True
                            shipcounter2 += 1
                            patrolboat2.pop()
            if not T2:
                if mulships[3][4] == "right":
                    for a in range(alphabet.index(mulships[3][3]), alphabet.index(mulships[3][3]) + 2):
                        if column2[int(mulships[3][2])][alphabet[a]] == "X":
                            counterP22 += 1
                        else:
                            counterP22 = 0
                        if counterP22 == 2:
                            counterP22 = 0
                            patrolboat2.insert(0, "X")
                            T2 = True
                            shipcounter2 += 1
                            patrolboat2.pop()
                elif mulships[3][4] == "down":
                    for a in range(int(mulships[3][2]), int(mulships[3][2]) + 2):
                        if column2[a][(mulships[3][3])] == "X":
                            counterP22 += 1
                        else:
                            counterP22 = 0
                        if counterP22 == 2:
                            counterP22 = 0
                            patrolboat2.insert(0, "X")
                            T2 = True
                            shipcounter2 += 1
                            patrolboat2.pop()
            if not T3:
                if mulships[4][4] == "right":
                    for a in range(alphabet.index(mulships[4][3]), alphabet.index(mulships[4][3]) + 2):
                        if column2[int(mulships[4][2])][alphabet[a]] == "X":
                            counterP23 += 1
                        else:
                            counterP23 = 0
                        if counterP23 == 2:
                            counterP23 = 0
                            patrolboat2.insert(0, "X")
                            T3 = True
                            shipcounter2 += 1
                            patrolboat2.pop()
                elif mulships[4][4] == "down":
                    for a in range(int(mulships[4][2]), int(mulships[4][2]) + 2):
                        if column2[a][(mulships[4][3])] == "X":
                            counterP23 += 1
                        else:
                            counterP23 = 0
                        if counterP23 == 2:
                            counterP23 = 0
                            patrolboat2.insert(0, "X")
                            T3 = True
                            shipcounter2 += 1
                            patrolboat2.pop()
            if not T4:
                if mulships[5][4] == "right":
                    for a in range(alphabet.index(mulships[5][3]), alphabet.index(mulships[5][3]) + 2):
                        if column2[int(mulships[5][2])][alphabet[a]] == "X":
                            counterP24 += 1
                        else:
                            counterP24 = 0
                        if counterP24 == 2:
                            counterP24 = 0
                            patrolboat2.insert(0, "X")
                            T4 = True
                            shipcounter2 += 1
                            patrolboat2.pop()
                elif mulships[5][4] == "down":
                    for a in range(int(mulships[5][2]), int(mulships[5][2]) + 2):
                        if column2[a][(mulships[5][3])] == "X":
                            counterP24 += 1
                        else:
                            counterP24 = 0
                        if counterP24 == 2:
                            counterP24 = 0
                            patrolboat2.insert(0, "X")
                            T4 = True
                            shipcounter2 += 1
                            patrolboat2.pop()
        elif row2[int(indexnumbers)][indexalphabet[0]] == 'B':
            column2[int(indexnumbers)][indexalphabet[0]] = "X"
            if not B1:
                if mulships[0][4] == "right":
                    for a in range(alphabet.index(mulships[0][3]), alphabet.index(mulships[0][3]) + 4):
                        if column2[int(mulships[0][2])][alphabet[a]] == "X":
                            counterB21 += 1
                        else:
                            counterB21 = 0
                        if counterB21 == 4:
                            counterB21 = 0
                            battleship2.insert(0, "X")
                            B1 = True
                            shipcounter2 += 1
                            battleship2.pop()
                elif mulships[0][4] == "down":
                    for a in range(int(mulships[0][2]), int(mulships[0][2]) + 4):
                        if column2[a][mulships[0][3]] == "X":
                            counterB21 += 1
                        else:
                            counterB21 = 0
                        if counterB21 == 4:
                            counterB21 = 0
                            battleship2.insert(0, "X")
                            B1 = True
                            shipcounter2 += 1
                            battleship2.pop()
            if not B2:
                if mulships[1][4] == "right":
                    for a in range(alphabet.index(mulships[1][3]), alphabet.index(mulships[1][3]) + 4):
                        if column2[int(mulships[1][2])][alphabet[a]] == "X":
                            counterB22 += 1
                        else:
                            counterB22 = 0
                        if counterB22 == 4:
                            counterB22 = 0
                            battleship2.insert(0, "X")
                            B2 = True
                            shipcounter2 += 1
                            battleship2.pop()
                elif mulships[1][4] == "down":
                    for a in range(int(mulships[1][2]), int(mulships[1][2]) + 4):
                        if column2[a][mulships[1][3]] == "X":
                            counterB22 += 1
                        else:
                            counterB22 = 0
                        if counterB22 == 4:
                            counterB22 = 0
                            battleship2.insert(0, "X")
                            B2 = True
                            shipcounter2 += 1
                            battleship2.pop()
    except AssertionError:
        getoutput("\n\nAssertionError: Invalid Operation.")
    except ValueError:
        if listindex[1] not in allalphabet:
            getoutput("\n\nValueError: the second value should be alphabetic.\n")
        elif len(listindex) > 2:
            getoutput("\n\nValueError: positions should separate from each other with ';' .\n")
        else:
            getoutput("\n\nValueError: the first value should be numeric.\n")
    except IndexError:
        if indexnumbers == '' and indexalphabet == '':
            getoutput("\n\nIndexError: movement should be written with a number and a letter.\n")
        elif indexnumbers == '':
            getoutput("\n\nIndexError: first element of movement should be a number.\n")
        elif indexalphabet == '':
            getoutput("\n\nIndexError: second element of movement should be a letter.\n")
    except:
        getoutput(f"\n\nkaBOOM: run for your life!\n")

def play2(i):
    try:
        global indexnumbers, indexalphabet, listindex, destroyer1, submarine1, carrier1, battleship1, patrolboat1, counterS1, counterD1, counterC1, counterB11,counterB12, counterP11, counterP12, counterP13, counterP14, shipcounter1, T5, T6, T7, T8, B3, B4
        if len(listindex[i]) < 3:
            raise IndexError
        listindex = listindex[i].split(",")
        indexnumbers = int(listindex[0])
        indexalphabet = listindex[1]
        if indexalphabet == '':
            raise IndexError
        if len(listindex) > 2 or indexalphabet not in allalphabet:
            raise ValueError
        assert int(indexnumbers) in range(1, 11)
        assert indexalphabet in alphabet
        getoutput(f"")
        getoutput(f"\n\nPlayer2's Move\n\n")
        getoutput(f"Round : {i+1}\t\t\t\t\tGrid Size: 10x10\n\n")
        assert column1[int(indexnumbers)][indexalphabet[0]] == '-'
        board()
        getoutput("")
        getoutput(f"\nEnter your move: {indexnumbers},{indexalphabet}")
        ships("OptionalPlayer1.txt")
        if row1[int(indexnumbers)][indexalphabet[0]] == '':
            column1[int(indexnumbers)][indexalphabet[0]] = "O"
        elif row1[int(indexnumbers)][indexalphabet[0]] == 'C':
            column1[int(indexnumbers)][indexalphabet[0]] = "X"
            counterC1 += 1
            if counterC1 == 5:
                carrier1 = "X"
                shipcounter1 += 1
        elif row1[int(indexnumbers)][indexalphabet[0]] == 'D':
            column1[int(indexnumbers)][indexalphabet[0]] = "X"
            counterD1 += 1
            if counterD1 == 3:
                destroyer1 = "X"
                shipcounter1 += 1
        elif row1[int(indexnumbers)][indexalphabet[0]] == 'S':
            column1[int(indexnumbers)][indexalphabet[0]] = "X"
            counterS1 += 1
            if counterS1 == 3:
                submarine1 = "X"
                shipcounter1 += 1
        elif row1[int(indexnumbers)][indexalphabet[0]] == 'P':
            column1[int(indexnumbers)][indexalphabet[0]] = "X"
            if not T5:
                if mulships[2][4] == "right":
                    for a in range(alphabet.index(mulships[2][3]), alphabet.index(mulships[2][3]) + 2):
                        if column1[int(mulships[2][2])][alphabet[a]] == "X":
                            counterP11 += 1
                        else:
                            counterP11 = 0
                        if counterP11 == 2:
                            counterP11 = 0
                            patrolboat1.insert(0, "X")
                            T5 = True
                            shipcounter1 += 1
                            patrolboat1.pop()
                elif mulships[2][4] == "down":
                    for a in range(int(mulships[2][2]), int(mulships[2][2]) + 2):
                        if column1[a][(mulships[2][3])] == "X":
                            counterP11 += 1
                        else:
                            counterP11 = 0
                        if counterP11 == 2:
                            counterP11 = 0
                            patrolboat1.insert(0, "X")
                            T5 = True
                            shipcounter1 += 1
                            patrolboat1.pop()
            if not T6:
                if mulships[3][4] == "right":
                    for a in range(alphabet.index(mulships[3][3]), alphabet.index(mulships[3][3]) + 2):
                        if column1[int(mulships[3][2])][alphabet[a]] == "X":
                            counterP12 += 1
                        else:
                            counterP12 = 0
                        if counterP12 == 2:
                            counterP12 = 0
                            patrolboat1.insert(0, "X")
                            T6 = True
                            shipcounter1 += 1
                            patrolboat1.pop()
                elif mulships[3][4] == "down":
                    for a in range(int(mulships[3][2]), int(mulships[3][2]) + 2):
                        if column1[a][(mulships[3][3])] == "X":
                            counterP12 += 1
                        else:
                            counterP12 = 0
                        if counterP12 == 2:
                            counterP12 = 0
                            patrolboat1.insert(0, "X")
                            T6 = True
                            shipcounter1 += 1
                            patrolboat1.pop()
            if not T7:
                if mulships[4][4] == "right":
                    for a in range(alphabet.index(mulships[4][3]), alphabet.index(mulships[4][3]) + 2):
                        if column1[int(mulships[4][2])][alphabet[a]] == "X":
                            counterP13 += 1
                        else:
                            counterP13 = 0
                        if counterP13 == 2:
                            counterP13 = 0
                            patrolboat1.insert(0, "X")
                            T7 = True
                            shipcounter1 += 1
                            patrolboat1.pop()
                elif mulships[4][4] == "down":
                    for a in range(int(mulships[4][2]), int(mulships[4][2]) + 2):
                        if column1[a][(mulships[4][3])] == "X":

                            counterP13 += 1
                        else:
                            counterP13 = 0
                        if counterP13 == 2:
                            counterP13 = 0
                            patrolboat1.insert(0, "X")
                            T7 = True
                            shipcounter1 += 1
                            patrolboat1.pop()
            if not T8:
                if mulships[5][4] == "right":
                    for a in range(alphabet.index(mulships[5][3]), alphabet.index(mulships[5][3]) + 2):
                        if column1[int(mulships[5][2])][alphabet[a]] == "X":
                            counterP14 += 1
                        else:
                            counterP14 = 0
                        if counterP14 == 2:
                            counterP14 = 0
                            patrolboat1.insert(0, "X")
                            T8 = True
                            shipcounter1 += 1
                            patrolboat1.pop()
                elif mulships[5][4] == "down":
                    for a in range(int(mulships[5][2]), int(mulships[5][2]) + 2):
                        if column1[a][(mulships[5][3])] == "X":
                            counterP14 += 1
                        else:
                            counterP14 = 0
                        if counterP14 == 2:
                            counterP14 = 0
                            patrolboat1.insert(0, "X")
                            T8 = True
                            shipcounter1 += 1
                            patrolboat1.pop()
        elif row1[int(indexnumbers)][indexalphabet[0]] == 'B':
            column1[int(indexnumbers)][indexalphabet[0]] = "X"
            if not B3:
                if mulships[0][4] == "right":
                    for a in range(alphabet.index(mulships[0][3]), alphabet.index(mulships[0][3]) + 4):
                        if column1[int(mulships[0][2])][alphabet[a]] == "X":
                            counterB11 += 1
                        else:
                            counterB11 = 0
                        if counterB11 == 4:
                            counterB11 = 0
                            battleship1.insert(0, "X")
                            B3 = True
                            shipcounter1 += 1
                            battleship1.pop()
                elif mulships[0][4] == "down":
                    for a in range(int(mulships[0][2]), int(mulships[0][2]) + 4):
                        if column1[a][mulships[0][3]] == "X":
                            counterB11 += 1
                        else:
                            counterB11 = 0
                        if counterB11 == 4:
                            counterB11 = 0
                            battleship1.insert(0, "X")
                            B3 = True
                            shipcounter1 += 1
                            battleship2.pop()
            if not B4:
                if mulships[1][4] == "right":
                    for a in range(alphabet.index(mulships[1][3]), alphabet.index(mulships[1][3]) + 4):
                        if column1[int(mulships[1][2])][alphabet[a]] == "X":
                            counterB12 += 1
                        else:
                            counterB12 = 0
                        if counterB12 == 4:
                            counterB12 = 0
                            battleship1.insert(0, "X")
                            B4 = True
                            shipcounter1 += 1
                            battleship1.pop()
                elif mulships[1][4] == "down":
                    for a in range(int(mulships[1][2]), int(mulships[1][2]) + 4):
                        if column1[a][mulships[1][3]] == "X":
                            counterB12 += 1
                        else:
                            counterB12 = 0
                        if counterB12 == 4:
                            counterB12 = 0
                            battleship1.insert(0, "X")
                            B4 = True
                            shipcounter1 += 1
                            battleship1.pop()
    except AssertionError:
        getoutput(f"\n\nEnter your move: {indexnumbers},{indexalphabet}")
        getoutput("\n\nAssertionError: Invalid Operation.")
    except ValueError:
        if indexalphabet not in allalphabet:
            getoutput("\n\nValueError: the second value should be alphabetic.\n")
        elif len(listindex) > 2:
            getoutput("\n\nValueError: positions should separate from each other with ';' .\n")
        else:
            getoutput("\n\nValueError: the first value should be numeric.\n")
    except IndexError:
        if indexnumbers == '' and indexalphabet == '':
            getoutput("\n\nIndexError: movement should be written with a number and a letter.\n")
        elif indexnumbers == '':
            getoutput("\n\nIndexError: first element of movement should be a number.\n")
        elif indexalphabet == '':
            getoutput("\n\nIndexError: second element of movement should be a letter.\n")
    except:
        getoutput(f"\n\nkaBOOM: run for your life!\n")

def board():
    getoutput(f"Player1's Hidden Board\t\tPlayer2's Hidden Board\n")
    getoutput(" ")
    for a in alphabet:
        getoutput("")
        getoutput(str(a).rjust(2, " "))
    getoutput("\t\t")
    getoutput(" ")
    for a in alphabet:
        getoutput("")
        getoutput(str(a).rjust(2, " "))
    for a in range(10):
        getoutput("\n")
        getoutput(str(a + 1).ljust(2, " "))
        for x in range(10):
            getoutput(f"{column1[a + 1][alphabet[x]]} ")
        getoutput("\t\t")
        getoutput(str(a + 1).ljust(2, " "))
        for x in range(10):
            getoutput(f"{column2[a + 1][alphabet[x]]} ")
    getoutput(f"\n\nCarrier\t\t{carrier1}\t\t\t\tCarrier\t\t{carrier2}\nBattleship\t{battleship1[0]} {battleship1[1]}\t\t\t\tBattleship\t{battleship2[0]} {battleship2[1]}\nDestroyer\t{destroyer1}\t\t\t\tDestroyer\t{destroyer2}\nSubmarine\t{submarine1}\t\t\t\tSubmarine\t{submarine2}\nPatrol Boat\t{patrolboat1[0]} {patrolboat1[1]} {patrolboat1[2]} {patrolboat1[3]}\t\t\tPatrol Boat\t{patrolboat2[0]} {patrolboat2[1]} {patrolboat2[2]} {patrolboat2[3]}\n")

def getoutput(a):
    output.write(a)
    print(a, end="")

getoutput("Battle of Ships Game")
try:
    getinput(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    for i in range(len(listindex)):
        if shipcounter1 != 9 and shipcounter2 != 9:
            getinput(sys.argv[3])
            play1(i)
        if shipcounter1 != 9 and shipcounter2 != 9:
            getinput(sys.argv[4])
            play2(i)
        elif shipcounter1 == 8 and shipcounter2 == 9:
                play1(i)
        elif shipcounter2 == 8 and shipcounter1 == 9:
                play2(i)
        else:
            break
except IOError:
    getoutput(f"\n\nIOError: input file(s) {' '.join(str(x) for x in problematic)} "
              f"is/are not reachable.\n\n")
except:
    getoutput("\n\nkaBOOM: run for your life!\n\n")
else:
    if shipcounter2 == 9 and shipcounter1 == 9:
        getoutput("\n\nIt is a Draw!\n\nFinal Information\n\n")
    else:
        if shipcounter2 > shipcounter1:
            getoutput("\n\nPlayer1 Wins!\n\nFinal Information\n\n")
        elif shipcounter2 < shipcounter1:
            getoutput("\n\nPlayer2 Wins!\n\nFinal Information\n\n")
    getoutput(f"Player1’s Board\t\t\t\tPlayer2’s Board\n")
    getoutput(" ")
    for a in alphabet:
        getoutput("")
        getoutput(str(a).rjust(2, " "))
    getoutput("\t\t")
    getoutput(" ")
    for a in alphabet:
        getoutput("")
        getoutput(str(a).rjust(2, " "))
    for a in range(10):
        getoutput("\n")
        getoutput(str(a + 1).ljust(2, " "))
        for x in range(10):
            if row1[a + 1][alphabet[x]] != '' and column1[a + 1][alphabet[x]] == "-":
                getoutput(f"{row1[a + 1][alphabet[x]]} ")
            else:
                getoutput(f"{column1[a + 1][alphabet[x]]} ")
        getoutput("\t\t")
        getoutput(str(a + 1).ljust(2, " "))
        for x in range(10):
            if row2[a + 1][alphabet[x]] != '' and column2[a + 1][alphabet[x]] == "-":
                getoutput(f"{row2[a + 1][alphabet[x]]} ")
            else:
                getoutput(f"{column2[a + 1][alphabet[x]]} ")
    getoutput("")
    getoutput(f"\n\nCarrier\t\t{carrier1}\t\t\t\tCarrier\t\t{carrier2}\nBattleship\t{battleship1[0]} {battleship1[1]}\t\t\t\tBattleship\t{battleship2[0]} {battleship2[1]}\nDestroyer\t{destroyer1}\t\t\t\tDestroyer\t{destroyer2}\nSubmarine\t{submarine1}\t\t\t\tSubmarine\t{submarine2}\nPatrol Boat\t{patrolboat1[0]} {patrolboat1[1]} {patrolboat1[2]} {patrolboat1[3]}\t\t\tPatrol Boat\t{patrolboat2[0]} {patrolboat2[1]} {patrolboat2[2]} {patrolboat2[3]}\n")