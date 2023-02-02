import sys
ackapiyi = sys.argv[1]
output = []
output = open("output.txt", "w")
allinputs = []
seats = []
rowandcoulumn = {}
categories = {}
row = {}
coulumn = {}
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
def getinput():
    global inputs
    getinput = open(ackapiyi, "r")
    thelist = list(getinput.read().splitlines())
    for i in range(len(thelist)):
        inputs = allinputs.append(thelist[i].split(" "))
def CREATECATEGORY(i):
    global categories, row, coulumn, rowandcoulumn
    totalticket = allinputs[i][2].split("x")                                #totalticket: mevcut kategorinin satır ve sütun sayısının liste hali(str)
    seatcount = int(totalticket[0]) * int(totalticket[1])                   #seatcount: oluşturulan her kategorideki toplam koltuk sayısı
    if allinputs[i][1] not in categories:
        rowandcoulumn[allinputs[i][1]] = [int(totalticket[0]), int(totalticket[1])]
        for a in range(len(allinputs[i])):
            row[allinputs[i][1]] = int(totalticket[0])
            coulumn[allinputs[i][1]] = int(totalticket[1])
        categories[allinputs[i][1]] = {}                                    #categories: oluşturulan tüm kategoriler, satış durumuyla beraber(dict)
        for x in range(int(totalticket[0])):
            for a in range(int(totalticket[1])):
                seat = alphabet[x] + str(number[a])                         #seat: harf+sayı koltuk gösterimi
                categories[allinputs[i][1]][seat] = "X"
        print(f"The category '{allinputs[i][1]}' having {seatcount} seats has been created.\n")
        output.write(f"The category '{allinputs[i][1]}' having {seatcount} seats has been created.\n")
    else:
        print(f"Warning: Cannot create the category for the second time. The stadium has already {allinputs[i][1]}.\n")
        output.write(f"Warning: Cannot create the category for the second time. The stadium has already {allinputs[i][1]}.\n")
def SELLTICKET(i):
    global categories, row, coulumn
    seats = allinputs[i][4:]                                                #seats: mevcut müşterinin seçmiş olduğu koltuk/lar liste halinde                                                 #multipleseats: çoklu koltuk alımlarında aralıkta alınan tüm koltuklar(c1,c2)(str)
    for a in range(len(seats)):
        if len(seats[a]) > 3:
            seatssplitted = seats[a].split("-")
            therange = []
            multipleseats = []
            for x in range(int(seatssplitted[0][1]), int(seatssplitted[1]) + 1):
                therange.append(str(x))
            for x in range(len(therange)):
                multipleseats.append(seatssplitted[0][0] + therange[x])
            if (alphabet.index(multipleseats[0][0]) + 1) < row[allinputs[i][3]] and int(therange[-1]) < coulumn[allinputs[i][3]]:
                if categories[allinputs[i][3]][multipleseats[a]] == "X":
                    therange = []
                    multipleseats = []
                    for x in range(int(seatssplitted[0][1]), int(seatssplitted[1]) + 1):
                        therange.append(str(x))
                    for x in range(len(therange)):
                        multipleseats.append(seatssplitted[0][0] + therange[x])
                    if allinputs[i][2] == "full":
                        for x in range(len(therange)):
                            categories[allinputs[i][3]][multipleseats[x]] = "F"
                        print(f"Success: {allinputs[i][1]} has bought {seats[a]} at {allinputs[i][3]}\n")
                        output.write(f"Success: {allinputs[i][1]} has bought {seats[a]} at {allinputs[i][3]}\n")
                    elif allinputs[i][2] == "season":
                        for x in range(len(therange)):
                            categories[allinputs[i][3]][multipleseats[x]] = "T"
                        print(f"Success: {allinputs[i][1]} has bought {seats[a]} at {allinputs[i][3]}\n")
                        output.write(f"Success: {allinputs[i][1]} has bought {seats[a]} at {allinputs[i][3]}\n")
                    elif allinputs[i][2] == "student":
                        for x in range(len(therange)):
                            categories[allinputs[i][3]][multipleseats[x]] = "S"
                        print(f"Success: {allinputs[i][1]} has bought {seats[a]} at {allinputs[i][3]}\n")
                        output.write(f"Success: {allinputs[i][1]} has bought {seats[a]} at {allinputs[i][3]}\n")
                else:
                    if len(allinputs[i][4:]) >= 3:
                        print(f"Warning: The seat {seats[a]} cannot be sold to {allinputs[i][1]} since it was already sold!\n")
                        output.write(f"Warning: The seat {seats[a]} cannot be sold to {allinputs[i][1]} since it was already sold!\n")
                    else:
                        print(f"Warning: The seats {seats[a]} cannot be sold to {allinputs[i][1]} due some of them have already been sold!\n")
                        output.write(f"Warning: The seats {seats[a]} cannot be sold to {allinputs[i][1]} due some of them have already been sold!\n")
            elif (alphabet.index(multipleseats[0][0]) + 1) < row[allinputs[i][3]] and int(therange[-1]) >= coulumn[
                allinputs[i][3]]:
                print(f"Error: The category '{allinputs[i][3]}' has less column than the specified index {seats[a]}!\n")
                output.write(
                    f"Error: The category '{allinputs[i][3]}' has less column than the specified index {seats[a]}!\n")
            elif (alphabet.index(multipleseats[0][0]) + 1) >= row[allinputs[i][3]] and int(therange[-1]) < coulumn[
                allinputs[i][3]]:
                print(f"Error: The category '{allinputs[i][3]}' has less row than the specified index {seats[a]}!\n")
                output.write(f"Error: The category '{allinputs[i][3]}' has less row than the specified index {seats[a]}!\n")
            else:
                print(f"Error: The category '{allinputs[i][3]}' has less row and column than the specified index {seats[a]}!\n")
                output.write(f"Error: The category '{allinputs[i][3]}' has less row and column than the specified index {seats[a]}!\n")
        else:
            seatnumbers = []
            seatnumbers.append(seats[a][1:])
            if (alphabet.index(seats[0][0]) + 1) < row[allinputs[i][3]] and int(seatnumbers[0]) < coulumn[allinputs[i][3]]:
                if categories[allinputs[i][3]][seats[a]] == "X":
                    if allinputs[i][2] == "full":
                        categories[allinputs[i][3]][seats[a]] = "F"
                        print(f"Success: {allinputs[i][1]} has bought {seats[a]} at {allinputs[i][3]}\n")
                        output.write(f"Success: {allinputs[i][1]} has bought {seats[a]} at {allinputs[i][3]}\n")
                    elif allinputs[i][2] == "season":
                        categories[allinputs[i][3]][seats[a]] = "T"
                        print(f"Success: {allinputs[i][1]} has bought {seats[a]} at {allinputs[i][3]}\n")
                        output.write(f"Success: {allinputs[i][1]} has bought {seats[a]} at {allinputs[i][3]}\n")
                    elif allinputs[i][2] == "student":
                        categories[allinputs[i][3]][seats[a]] = "S"
                        print(f"Success: {allinputs[i][1]} has bought {seats[a]} at {allinputs[i][3]}\n")
                        output.write(f"Success: {allinputs[i][1]} has bought {seats[a]} at {allinputs[i][3]}\n")
                else:
                    if len(allinputs[i][4:]) >= 1:
                        print(f"Warning: The seat {allinputs[i][4]} cannot be sold to {allinputs[i][1]} since it was already sold!\n")
                        output.write(f"Warning: The seat {allinputs[i][4]} cannot be sold to {allinputs[i][1]} since it was already sold!\n")
                    else:
                        print(f"Warning: The seats {seats[a]} cannot be sold to {allinputs[i][1]} due some of them have already been sold!\n")
                        output.write(f"Warning: The seats {seats[a]} cannot be sold to {allinputs[i][1]} due some of them have already been sold!\n")
            elif (alphabet.index(seats[0][0]) + 1) < row[allinputs[i][3]] and int(seatnumbers[0]) >= coulumn[allinputs[i][3]]:
                print(f"Error: The category '{allinputs[i][3]}' has less column than the specified index {allinputs[i][4:]}!\n")
                output.write(f"Error: The category '{allinputs[i][3]}' has less column than the specified index {allinputs[i][4:]}!\n")
            elif (alphabet.index(seats[0][0]) + 1) >= row[allinputs[i][3]] and int(seatnumbers[0]) < coulumn[allinputs[i][3]]:
                print(f"Error: The category '{allinputs[i][3]}' has less row than the specified index {allinputs[i][4:]}!\n")
                output.write(f"Error: The category '{allinputs[i][3]}' has less row than the specified index {allinputs[i][4:]}!\n")
            else:
                print(f"Error: The category '{allinputs[i][3]}' has less row and column than the specified index {allinputs[i][4:]}!\n")
                output.write(f"Error: The category '{allinputs[i][3]}' has less row and column than the specified index {allinputs[i][4:]}!\n")
def CANCELTICKET(i):
    global categories, row, coulumn
    if (alphabet.index(allinputs[i][2][0])+1) <= row[allinputs[i][1]] and int(allinputs[i][2][1:]) <= coulumn[allinputs[i][1]]:
        if categories[allinputs[i][1]][allinputs[i][2]] == "X":
            print(f"Error: The seat {allinputs[i][2]} at '{allinputs[i][1]}' has already been free! Nothing to cancel\n")
            output.write(f"Error: The seat {allinputs[i][2]} at '{allinputs[i][1]}' has already been free! Nothing to cancel\n")
        else:
            categories[allinputs[i][1]][allinputs[i][2]] = "X"
            print(f"Success: The seat {allinputs[i][2]} at '{allinputs[i][1]}' has been canceled and now ready to sell again\n")
            output.write(f"Success: The seat {allinputs[i][2]} at '{allinputs[i][1]}' has been canceled and now ready to sell again\n")
    elif (alphabet.index(allinputs[i][2][0])+1) > row[allinputs[i][1]] and int(allinputs[i][2][1:]) <= coulumn[allinputs[i][1]]:
        print(f"Error: The category '{allinputs[i][1]}' has less row than the specified index {allinputs[i][2]}!\n")
        output.write(f"Error: The category '{allinputs[i][1]}' has less row than the specified index {allinputs[i][2]}!\n")
    elif (alphabet.index(allinputs[i][2][0])+1) <= row[allinputs[i][1]] and int(allinputs[i][2][1:]) > coulumn[allinputs[i][1]]:
        print(f"Error: The category '{allinputs[i][1]}' has less column than the specified index {allinputs[i][2]}!\n")
        output.write(f"Error: The category '{allinputs[i][1]}' has less column than the specified index {allinputs[i][2]}!\n")
    else:
        print(f"Error: The category '{allinputs[i][1]}' has less column and row than the specified index {allinputs[i][2]}!\n")
        output.write(f"Error: The category '{allinputs[i][1]}' has less column and row than the specified index {allinputs[i][2]}!\n")
def BALANCE(i):
    global categories
    result = 0
    summation = []
    sumofstudent = 0
    sumoffull = 0
    sumofseason = 0
    for x in categories[allinputs[i][1]].values():
        if "S" in x:
            summation.append(10)
            sumofstudent = sumofstudent + 1
        elif "F" in x:
            summation.append(20)
            sumoffull = sumoffull + 1
        elif "T" in x:
            summation.append(250)
            sumofseason = sumofseason + 1
    for a in range(len(summation)):
        result = summation[a] + result
    print("-" * 41, "\n")
    output.write("-" * 41)
    output.write("\n")
    print(f"Sum of students = {sumofstudent}, Sum of full pay = {sumoffull}, Sum of season ticket = {sumofseason}, and Revenues = {result} Dollars\n")
    output.write(f"Sum of students = {sumofstudent}, Sum of full pay = {sumoffull}, Sum of season ticket = {sumofseason}, and Revenues = {result} Dollars\n")
def SHOWCATEGORY(i):
    global categories, rowandcoulumn
    seats = list(categories[allinputs[i][1]].keys())
    seats.reverse()
    print(f"Printing category layout of {allinputs[i][1]}\n\n")
    output.write(f"Printing category layout of {allinputs[i][1]}\n\n")
    for b in range(64+rowandcoulumn[allinputs[i][1]][1], 64, -1):
        print(chr(b), end=" ")
        output.write(chr(b)+" ")
        for a in range(rowandcoulumn[allinputs[i][1]][0]):
            print(categories[allinputs[i][1]][chr(b)+str(a)], end="  ")
            output.write(f"{categories[allinputs[i][1]][chr(b)+str(a)]}"+"  ")
        print()
        output.write("\n")
    for a in range(rowandcoulumn[allinputs[i][1]][1]):
        thelast = []
        thelast.append(a)
        print(str(a).rjust(3," "), end="")
        output.write(str(a).rjust(3," "))
    print()
    print(f"\ncategory report of '{allinputs[i][1]}'\n")
    output.write(f"\ncategory report of '{allinputs[i][1]}'\n")
def getoutput():
    for i in range(len(allinputs)):
        if allinputs[i][0] == "CREATECATEGORY":
            CREATECATEGORY(i)
        elif allinputs[i][0] == "SELLTICKET":
            SELLTICKET(i)
        elif allinputs[i][0] == "CANCELTICKET":
            CANCELTICKET(i)
        elif allinputs[i][0] == "BALANCE":
            BALANCE(i)
        elif allinputs[i][0] == "SHOWCATEGORY":
            SHOWCATEGORY(i)
getinput()
getoutput()

#Şükriye Öztürk 2210356110
