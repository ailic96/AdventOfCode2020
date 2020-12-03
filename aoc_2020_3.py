# Advent of Code, Day 3
# https://adventofcode.com/2020/day/3
# Opens file and splits lines
# Inspiration found on https://www.reddit.com/r/adventofcode/comments/k5qsrk/2020_day_03_solutions/
# for this one.


def open_file(file):
    with open(file, 'r') as file:
        row = [x for x in file.read().splitlines()]
        return row

def part_one(row):
    
    # Position [0,0]
    length = len(row[0])
    # Number of trees
    counter = 0
    # x coordinate
    dx = 0
    
    # y coordinate
    for dy in range(1, len(row), 1):
        r = row[dy]
        dx = (dx + 3) % length
        if (r[dx] == '#'):
            counter += 1
    return counter


def part_two(row, horizontal, vertical):
    
    # Position [0,0]
    length = len(row[0])
    # Number of trees
    counter = 0
    # x coordinate
    dx = 0
    
    # y coordinate
    for dy in range(vertical, len(row), vertical):
        r = row[dy]
        dx = (dx + horizontal) % length
        if (r[dx] == '#'):
            counter += 1
    return counter


row = open_file('aoc_2020_day_3.txt')

tree_count = part_one(row)

print('Part one solution: ' + str(tree_count))

# Part two
slopes = [(1, 1),(3, 1),(5, 1),(7, 1),(1, 2)]


# Feeds the function with slope coordinates
product = 1
for (hor, ver) in slopes:
    product *= part_two(row, hor, ver)

print('Part two solution: ' + str(product))


