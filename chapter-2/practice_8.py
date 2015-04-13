#!/usr/bin/env python

# fixed list
fixed_list = [1, 2, 3, 4, 5]

while_result = 0

fixed_index = 0

while fixed_index < len(fixed_list):
    while_result += fixed_list[fixed_index]
    fixed_index += 1

print while_result

for_result = 0

for item in fixed_list:
    for_result += item

print for_result

# input list
input_list = [0, 0, 0, 0, 0]

index = 0

while index < 5:
    input_list[index] = int(raw_input("Please input a number: "))
    index += 1

print "The input list is: " + repr(input_list)

index = 0

result = 0

while index < len(input_list):
    result += input_list[index]
    index += 1

print result
