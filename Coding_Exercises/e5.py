import random

lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

new_number = random.randint(lower_bound, upper_bound)
print(new_number)