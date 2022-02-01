even = 0
odd = 0

min_val = 0
max_val = 0

i = 0
while i < 10:
    num = int(input('Please enter a number: '))

    if not num % 2:
        odd += 1
    else:
        even += 1

    if i == 0:
        min_val = max_val = num

    i += 1

print(odd)
print(even)
