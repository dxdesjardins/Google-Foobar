def PossibleMoves(map, loc):
    move1 = [loc[0] + 1, loc[1]]
    move2 = [loc[0] - 1, loc[1]]
    move3 = [loc[0], loc[1] + 1]
    move4 = [loc[0], loc[1] - 1]
    moves = [move1, move2, move3, move4]
    possibleMoves = []
    for move in moves:
        if move[0] >= 0 and move[0] < len(map[0]) and move[1] >= 0 and move[1] < len(map):
            if map[move[1]][move[0]] == 0:
                possibleMoves.append(move)
    return possibleMoves

def IsAtFinish(map, loc):
    if loc[0] == len(map[0]) - 1 and loc[1] == len(map) - 1:
        return True
    else:
        return False

class Area:
    def __init__(self, prevLocs):
        self.prevLocs = prevLocs[:]
    def CanMoveToLoc(self, newLoc):
        hasBeen = False
        for prevLoc in self.prevLocs:
            if newLoc == prevLoc:
                hasBeen = True
        if hasBeen:
            return False
        else:
            return True
    def appendPrevLoc(self, loc):
        self.prevLocs.append(loc)

def DistToFinish(map):
    area = Area([[0,0]])
    locsToCheck = [[0,0]]
    nextLocsToCheck = []
    distance = 1
    solved = False
    while len(locsToCheck) > 0:
        for location in locsToCheck:
            for possibleMove in PossibleMoves(map, location):
                if area.CanMoveToLoc(possibleMove):
                    nextLocsToCheck.append(possibleMove)
                    area.prevLocs.append(possibleMove)
        distance += 1
        for nextLoc in nextLocsToCheck:
            if IsAtFinish(map, nextLoc):
                solved = True
                break
        if solved:
            break
        locsToCheck = nextLocsToCheck[:]
        del nextLocsToCheck[:]
    if solved:
        return distance
    else:
        return None

def solution(map):
    shortestDists = []
    dist = DistToFinish(map)
    if dist is not None:
        shortestDists.append(dist)
    y = 0
    for i in map:
        x = 0
        for j in i:
            if j == 1:
                map[y][x] = 0
                dist = DistToFinish(map)
                if dist is not None:
                    shortestDists.append(dist)
                map[y][x] = 1
            x += 1
        y += 1
    answerDist = shortestDists[0]
    for shortestDist in shortestDists:
        if shortestDist < answerDist:
            answerDist = shortestDist
    return answerDist
