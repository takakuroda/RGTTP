"""
  Lesson 1: ex3.py
"""

# 1. Print out your favourite food 42 times using * operator.

# INSERT YOUR CODE HERE

print("natto" * 42)

# 2. Insert space between each output and print it out again.

# INSERT YOUR CODE HERE

print(("natto" + " ") * 42)

# 3. Save your favourite food into a variable and print it out 42 times

# INSERT YOUR CODE HERE

my_favourite_food = "natto"
print((my_favourite_food + " ") * 42)

# 4. My favourite food is "sushi", save it into a variable and using
#    fast swapping operation change it with your variable.
#    Now your favourite food should be "sushi" and mine will be yours.#

# INSERT YOUR CODE HERE

def fast_swap(robins_favourite_food: str = "sushi", takas_favourite_food: str = "wasabi"):
  print("Robin: " + robins_favourite_food)
  print("Taka: " + takas_favourite_food)
  robins_favourite_food, takas_favourite_food = takas_favourite_food, robins_favourite_food
  print("Robin: " + robins_favourite_food)
  print("Taka: " + takas_favourite_food)

fast_swap()




# 5. Why following function does not work?

robins_favourite_food: str = "sushi"
takas_favourite_food: str = "wasabi"
def fast_swap():
  print("Robin: " + robins_favourite_food)
  print("Taka: " + takas_favourite_food)
  robins_favourite_food, takas_favourite_food = takas_favourite_food, robins_favourite_food
  print("Robin: " + robins_favourite_food)
  print("Taka: " + takas_favourite_food)

fast_swap()