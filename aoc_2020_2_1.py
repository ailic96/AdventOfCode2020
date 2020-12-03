<<<<<<< HEAD
# Advent of code day two
# https://adventofcode.com/2020/day/2

import re

file = open('aoc_2020_day_2.txt', 'r')

pass_counter = 0

for row in file:
    regex = re.search('(\d{1,2})-(\d{1,2})\s(\w):\s(\w*)', row)

    if regex:
        minimum = int(regex.group(1))
        maximum = int(regex.group(2))
        letter = regex.group(3)
        password = regex.group(4)

    #print(minimum, maximum, letter, password)
    
    letter_count = password.count(letter)
    
    if (letter_count >= minimum and letter_count <= maximum):
        pass_counter += 1

print('Number of correct passwords: ' + str(pass_counter))



        
=======
import re

# Advent of code day two

file = open('aoc_2020_day_2.txt', 'r')

pass_counter = 0

for row in file:
    regex = re.search('(\d{1,2})-(\d{1,2})\s(\w):\s(\w*)', row)

    if regex:
        minimum = int(regex.group(1))
        maximum = int(regex.group(2))
        letter = regex.group(3)
        password = regex.group(4)

    #print(minimum, maximum, letter, password)
    
    letter_count = password.count(letter)
    
    if (letter_count >= minimum and letter_count <= maximum):
        pass_counter += 1

print('Number of correct passwords: ' + str(pass_counter))



        
>>>>>>> 794ac7b22149c4254d41c6589682c969ad1b16d6
