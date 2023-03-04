import random

# specify the number of random digits to generate
num_of_digits = 46

# generate a list of unique random digits
random_digits = random.sample(range(90), num_of_digits)

# print the list of random digits
print(random_digits)
