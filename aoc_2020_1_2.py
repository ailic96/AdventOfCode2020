<<<<<<< HEAD
# Advent of code day one
# https://adventofcode.com/2020/day/1

import re
def file_to_list(input_file):
    elements = []
    for row in input_file:
        elements.append(int(row))
    
    return elements

file = open('puzzle_input.txt', 'r')

elements = file_to_list(file)

result = []
sum = 2020

for i in range(0, len(elements) - 2):
    for j in range(i + 1, len(elements) - 1):
        for k in range(j + 1, len(elements)):
            if elements[i] + elements[j] + elements[k] == sum:
                result = elements[i] * elements[j] * elements[k]
                print('Pair: (' + str(elements[i]) + ', ' + str(elements[i])  + ', ' + str(elements[k]) + ')')
=======
# Advent of code, day one, task two

def file_to_list(input_file):
    elements = []
    for row in input_file:
        elements.append(int(row))
    
    return elements

file = open('puzzle_input.txt', 'r')

elements = file_to_list(file)

result = []
sum = 2020

for i in range(0, len(elements) - 2):
    for j in range(i + 1, len(elements) - 1):
        for k in range(j + 1, len(elements)):
            if elements[i] + elements[j] + elements[k] == sum:
                result = elements[i] * elements[j] * elements[k]
                print('Pair: (' + str(elements[i]) + ', ' + str(elements[i])  + ', ' + str(elements[k]) + ')')
>>>>>>> 794ac7b22149c4254d41c6589682c969ad1b16d6
print(result)