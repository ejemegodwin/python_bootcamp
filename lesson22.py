numbers = [15, 42, 8, 99, 23]

highest = numbers[0]

for number in numbers:
    if number > highest:
        highest = number

print(highest)