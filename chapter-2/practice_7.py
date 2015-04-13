#!/usr/bin/env python

input_param = raw_input("Please type in a string: ")

index = 0

while index < len(input_param):
    print input_param[index]
    index += 1

for item in input_param:
    print item
