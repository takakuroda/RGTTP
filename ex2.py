"""
  Lesson 1: ex2.py
"""

# Here is my shopping list:
#
# 2.99 Apples
# 1.79 Milk
# 3.49 Bread
# 6.99 Chicken
# 2.49 Pasta

# 1. Make a python list of the 5 items above and print it out.

# INSERT YOUR CODE HERE

shopping_list = ["Apples", "Milk", "Bread", "Chicken", "Pasta"]
print(shopping_list)

# 2. Use python as your calculator and print out the total cost of
#    all items on shopping list.

# INSERT YOUR CODE HERE

def shopping_calculator(apples: int = 10, milk: int = 3, bread: int = 2, chicken: int = 7, pasta: int = 5) -> float:
  total_cost = 2.99*apples + 1.79*milk + 3.49*bread + 6.99*chicken + 2.49*pasta
  return print(total_cost)
shopping_calculator()

# 3. I have decided that we need 5 cartons of milk, can you recalculate
#    it and print it out again?

# INSERT YOUR CODE HERE

def shopping_calculator(apples: int = 10, milk: int = 3, bread: int = 2, chicken: int = 7, pasta: int = 5) -> float:
  total_cost = 2.99*apples + 1.79*milk + 3.49*bread + 6.99*chicken + 2.49*pasta
  return print(total_cost)
shopping_calculator(milk=5)

# 4. Print out every item of your shopping list on a new line.

# INSERT YOUR CODE HERE

apples = 10
milk = 5
bread = 2
chicken = 7
pasta = 5

print("Apples: AUD" + str(round(2.99*apples)) + ", " + "Milk: AUD" + str(1.79*milk) + ", " + "Bread: AUD" + str(3.49*bread)  + ", " + "Chicken: AUD" + str(6.99*chicken)  + ", " + "Pasta: AUD" + str(round(2.49*pasta)))


