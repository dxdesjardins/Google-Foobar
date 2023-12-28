T = [[0, 1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30, 31], [32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47], [48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63]]

def CalcLoc(src):
	x = src % 8 
	y = int((src - (src % 8)) / 8)
	return [x, y]

def PossibleMoves(x, y):
	moves = [[x - 2, y + 1], [x - 2, y - 1], [x + 2, y + 1], [x + 2, y - 1], [x + 1, y - 2], [x - 1, y - 2], [x + 1, y + 2], [x - 1, y + 2]]
	result = []
	for move in moves:
		inbounds = True	
		for ele in move:
			if ele < 0 or ele > 7:
				inbounds = False
		if inbounds:
			result.append(move)
	return result

def solution(src, dest):
	source = CalcLoc(src)
	destination = CalcLoc(dest)
	#print(source)
	#print(destination)
	previousLs = [source]
	currentLs = [source]
	moves = 0
	if src == dest:
		return 0
	while True:
		moves = moves + 1	
		newLs = []
		for currentL in currentLs:
			possibleLs = PossibleMoves(currentL[0], currentL[1])
			used = False
			for possibleL in possibleLs:
				for previousL in previousLs:
					if previousL == possibleL:
						used = True
				if not used:
					newLs.append(possibleL)
		currentLs = newLs
		for currentL in currentLs:
			if currentL == destination:
				return moves
		#print(currentLs)	
		for currentL in currentLs:
			previousLs.append(currentL)
		if moves > 100:
			#print("Houston, we have a problem.")
			#print(previousLs)
			break
