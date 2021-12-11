"""AoC sonar sweep solution in python
https://adventofcode.com/2021/day/1"""

# Part 1
filename = '../input/day01.txt'
prev_reading = 99999 # Just to force the first difference to be negative
increase = 0

with open(filename) as file_object:
    for str_reading in file_object:
        difference = int(str_reading) - prev_reading
        if difference > 0:
           increase += 1
        prev_reading = int(str_reading)

print(increase)

# Part 2
filename = '../input/day01.txt'
prev_triplet = 99999 # Just to force the first difference to be negative
increase = 0
i = 0

with open(filename) as file_object:
   list_readings = file_object.readlines()

for i in range(len(list_readings)-2):
    triplet = int(list_readings[0+i])+int(list_readings[1+i])+int(list_readings[2+i])
    print(triplet, end=" : ")
    difference = triplet - prev_triplet
    print(difference > 0)
    if difference > 0:
        increase += 1 
    prev_triplet = triplet

print(increase)