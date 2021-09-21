#advent of Code 2020 day 2

import re

test_string = "2-5 z: zzztvz"

def giveBoundsAsList(textfileLine):
  findNumerals = re.findall(r'\d+', textfileLine)
  return list(map(int,findNumerals))

print(giveBoundsAsList(test_string))


with open('AdventOfCode2020Day2input.txt', 'r') as f:
  lines = f.readlines()


print(len(lines))
print(lines[0])

f.close()
'''
def passwordIsValid(line):
  passwordSplit = line.split(": ", 1)


  
  lower = line[0] #this doesn't work because it doesn't account for two-digit numbers. 
  upper = line[2]
  

pwSplit = lines[1].split(": ", 1)
inputValidation = pwSplit[0].split()
passwordInclEscape = pwSplit[1].split("\\n", 1)
password = passwordInclEscape[0].split("\\",0)
bounds = inputValidation[0].split("-")
lowerBound = int(bounds[0])
upperBound = int(bounds[1])
validationLetter = inputValidation[1]

print(inputValidation)
print(passwordInclEscape)
print(password)
print(bounds)
print(lowerBound)
print(upperBound)
print(validationLetter)

pwStr = "2-5 z: zzztvz"
numerals = int(filter(pwStr.isDigit, str1))

'''