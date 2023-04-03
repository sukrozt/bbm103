import sys
inputfile = open(sys.argv[1], "r")
listinputfile = list(inputfile.read().splitlines())
outputfile = open(sys.argv[2], "w")
result = 0
for a in range(len(listinputfile)):
    listinputfile.sort()
    if (listinputfile[a][5]) == "0":
        result = result+1
        outputfile.write(f"Message\t{result}\n")
    outputfile.write(listinputfile[a]+"\n")

#Şükriye Öztürk 2210356110
