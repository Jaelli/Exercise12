import random

your_numbers = []
for i in range(0, 6):
    number = int(input("Enter a number: "))
    your_numbers.append(number)

lotto_numbers = []
for i in range(0, 6):
    number = random.randint(1, 50)
    while number in lotto_numbers:
        number = random.randint(1, 50)
    lotto_numbers.append(number)
    print(lotto_numbers)

print()

lotto_numbers.sort()

print("Tonight's lotto results are: \n" + str(lotto_numbers))

print()

your_numbers.sort()
print("Your numbers: \n" + str(your_numbers))

count = 0
for number in your_numbers:
    if number in lotto_numbers:
        count += 1

if count == 1:
    print("You had " + str(count) + " matching number")
else:
    print("You had " + str(count) + " matching numbers")
