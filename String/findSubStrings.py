inputStr = "abcd"
def findSubStrs(input):
    for i in range(len(input)):
        for j in range(i,len(input)):
            print input[i: j+1]

findSubStrs(inputStr)