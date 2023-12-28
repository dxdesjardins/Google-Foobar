forward = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
reverse = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]

def solution(inputStr):
    outputStr = list(inputStr)
    i = 0
    for chr in outputStr:
        j = 0
        for alph in forward:
            if alph == chr:
                outputStr[i] = reverse[j]
            j += 1
        i += 1
    return "".join(outputStr)

#print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))