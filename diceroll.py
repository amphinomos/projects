import random

def addToRange(numList):
    '''called with the number inputed by user and returns the range+1'''
    return [i + 1 for i in numList] 

def convToDict(seq):
    '''also called with number inputed by user and
    intializes a tracking dictionary {1:0,2:0,n:0} '''
    tempDict = {}
    for i,item in enumerate(seq):
	    tempDict.update({i+1:item})
    for key,value in tempDict.items():
	    tempDict[key] = 0
    return tempDict

def counter(numSeq,rolls):
    '''params: dictionary and the number of rolls'''
    i = 1
    while i < rolls+1:
        a = random.randint(1,max(numSeq.keys()))
        for value in numSeq.keys():
            if a == value:
                numSeq[value] += 1
        i += 1
    return numSeq

def printResult(finalSeq):
    finalSeq = sorted(finalSeq.items(),key=lambda x: x[1], reverse=True)
    #returns a list with tuples
    numOnce = []
    numTwice = []
    numMultiple = []
    for i in finalSeq:
        #loop through list
        if i[1] == 2:
            numTwice.append(i[0])
        elif i[1] == 1:
            numOnce.append(i[0])
        elif  i[1]!= 1 and i[1]!= 2 and i[1] != 0:
            print i[0]," appeared",i[1]," times."
    if len(numTwice)>0:
        print ",".join([str(item) for item in numTwice]), "appeared twice."
    if len(numOnce)>0:
        print ",".join([str(item) for item in numOnce]), "appeared once."
    


print "Welcome to dice roll!"
print "-" * 20

while True:
    while True:
        numofSides = raw_input("Please choose number of sides on your dice: \n")
        try :
            if int(numofSides):
                numofSides = int(numofSides)
                break
        except ValueError:
            print ("Thought that was a number? Try again!\n")

    while True:
        numofRolls = raw_input("Please choose number of dice rolls: \n")
        print "\n"
        try :
            if int(numofSides):
                numofRolls = int(numofRolls)
                break
        except ValueError:
            print ("Thought that was a number? Try again!\n")
                
    numofSides = range(numofSides)
    numofSides = addToRange(numofSides)
    numofSides = convToDict(numofSides)
    numofSides = counter(numofSides,numofRolls)
    printResult(numofSides)

    keepPlay = raw_input("Play again? Y/N\n")
    if keepPlay.lower().startswith("n"):
        print "Thanks for playing! Press any key to quit.\n"
        raw_input()
        break



