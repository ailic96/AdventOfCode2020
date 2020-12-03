<<<<<<< HEAD
# Advent of code day one
# https://adventofcode.com/2020/day/1


def file_to_list(input_file):
    elements = []
    for row in input_file:
        elements.append(int(row))
    
    return elements 

file = open('puzzle_input.txt', 'r')

elements = file_to_list(file)

result = []
sum = 2020

for i in range(0, len(elements) - 1):
        for j in range(i + 1, len(elements)):
            if elements[i] + elements[j] == sum:
                result = elements[i] * elements[j]
                print('Pair: (' + str(elements[i]) + ', ' + str(elements[j])  + ')')
=======
# Advent of code, day one

def file_to_list(input_file):
    elements = []
    for row in input_file:
        elements.append(int(row))
    
    return elements 

file = open('puzzle_input.txt', 'r')

elements = file_to_list(file)

result = []
sum = 2020

for i in range(0, len(elements) - 1):
        for j in range(i + 1, len(elements)):
            if elements[i] + elements[j] == sum:
                result = elements[i] * elements[j]
                print('Pair: (' + str(elements[i]) + ', ' + str(elements[j])  + ')')
>>>>>>> 794ac7b22149c4254d41c6589682c969ad1b16d6
print(result)