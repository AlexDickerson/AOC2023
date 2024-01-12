import os

numDict = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9',
           '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9' }

#n = number of lines, k = number of keys in numDict, l = number of characters in line
#O(n*k*l), n and k being static => O(n)
def main(filePath: str) -> int:
    sum = 0
    for l in open(filePath).readlines(): sum += ParseLine(l) #O(n)
    return sum

def ParseLine(characters: str) -> int:
    digits = ["-1"] * len(characters)
    
    index1 = index2 = -1

    for num in numDict.keys(): #O(k)
        try:
            index = characters.index(num) #O(l)
            lastindex = characters.rfind(num) #O(l)
            digits[index] = digits[lastindex] = numDict[num]

            if(index < index1 or index1 == -1): index1 = index
            if(index > index2): index2 = index

            if(lastindex < index1 or index1 == -1): index1 = lastindex
            if(lastindex > index2): index2 = lastindex
        except: pass
    
    return int(digits[index1] + digits[index2])

print(main(os.path.join(os.path.dirname(__file__), "input.txt")))