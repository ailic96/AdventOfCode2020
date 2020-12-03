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
    
    if (password[minimum-1] == letter and password[maximum-1] != letter):
        pass_counter += 1
        print('Found one!')
    elif(password[minimum-1] != letter and password[maximum-1] == letter):
        pass_counter += 1
        print('Found one!')
    else:
        print('Invalid password')

print('Number of correct passwords: ' + str(pass_counter))



        
=======
# Advent of code day two

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
    
    if (password[minimum-1] == letter and password[maximum-1] != letter):
        pass_counter += 1
        print('Found one!')
    elif(password[minimum-1] != letter and password[maximum-1] == letter):
        pass_counter += 1
        print('Found one!')
    else:
        print('Invalid password')

print('Number of correct passwords: ' + str(pass_counter))



        
>>>>>>> 794ac7b22149c4254d41c6589682c969ad1b16d6
