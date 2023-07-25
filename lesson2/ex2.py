"""
  Lesson 2: ex2.py
"""

# 1. Use string formatting with empty curly brackets {}
#    to take the argument passed into format and print a
#    sentence of your choice.

# INSERT YOUR CODE HERE

name: str = "Taka"
height: float = 215.2
feet: int = 7
inch: int = 2

print('Crazy {}\'s height is {} cm, which is about {} feet {} inches.'
      .format(name, height, feet, inch))

print()


# 2. Use string formatting with positional arguments and
#    print the sentence: "Don't Panic!"

# INSERT YOUR CODE HERE

def panic(string_1: str, string_2: str) -> str:
    print(string_1 + " " + string_2)

panic("Don't", "Panic!")

print()

panic("Panic!", "Don't")

print()

panic(string_2 = "Panic!", string_1 = "Don't")

print()


# 3. Use string formatting with named arguments and
#    print the sentence: "[name] is really [what]!" and
#    fill in the brackets with your name and "great".

# INSERT YOUR CODE HERE

def charactor(name: str, what: str) -> str:
    print(name + " is really " + what + "!")

charactor("Taka", "bastard")

print()

charactor("bastard", "Taka")

print()

charactor(what="bastard", name="Taka")

print()