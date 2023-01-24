# Defining Variables
invalids = 0
valids = 0

# Defining the validate function 
def validate(ballot: str, number):
    if len(ballot) != number:
        return False
    ballot = sorted(list((ballot)))
    for c,v in enumerate(ballot):
        if int(v) != c + 1:
            return False
    return True

# Defining the preferences check function 
def findWinner(arr, i):
    if i == 0:
        return sum(arr)
    else:
        return arr.count(i)

# Asking User To Specify Which File They Would Like To Open
userFile = input("Please specify which Voting File you would like to use? Input either,'test_1.txt', 'test_2.txt', 'test_3.txt' or 'test_4.txt'." '\n')

# Opening and reading the file that the user selected
with open(userFile) as sourceFile:
    readFile = [a.strip("\n") for a in sourceFile.readlines()]


# Seeing how many candidates there are and extracting out the names of all the candidates
    numOfCandidates = int(readFile[0])
    nameOfCandidates = readFile[1: numOfCandidates +1]
    names = readFile[1: numOfCandidates +1]


# Verifying how many ballots there are and if they are valid or spoilt
    ballots = readFile[numOfCandidates + 1:]
    validBallots = [x for x in ballots if validate(x, numOfCandidates)]
    valids = len(validBallots)
    invalids = len(ballots) - valids
                
#Getting preferences arrays
tally = [[] for x in range(numOfCandidates)]
for ballot in validBallots:
    for c,v in enumerate(ballot):
        tally[c].append(int(v))
tallyTotal = tally

# Loop to find the winner based of least number of points and the most preferences
i = 0
found = False
winner = None

while not found:
    points = [findWinner(arr, i) for arr in tally]
    if i == 0: 
        pWinner = min(points)
    else:
        pWinner = max(points)
    if points.count(pWinner) == 1:
        found = True
        winner = names[points.index(pWinner)] 
    else: 
        still_in = [i for i in range(len(tally)) if points[i] == pWinner] 
        tally = [tally[i] for i in still_in] 
        names = [names[i] for i in still_in] 
    i += 1 
    if i > numOfCandidates: 
        found = True
        winner = "draw"

# Printing out everything, including the total number of candidates and the total number of candidates, the number of spoilt and valid ballots and the outcome of the election
print('\n' + "The " + str(numOfCandidates) + " total number of candidates for this election are:" + '\n')

for candidatesName in nameOfCandidates:
    print(" " + candidatesName)

print( '\n' + "There were", valids, "valid ballots and", invalids, "spoilt ballots." + '\n')

for candidatesName, valves in zip(nameOfCandidates, tallyTotal):
    print(" " + candidatesName, "got", sum(valves), "points")

if winner == "draw":
    print('\n' + "This election resulted in a draw, therefore a re-election must be called.")
else:
    print('\n' + "The winner of this election is", winner + ".")
