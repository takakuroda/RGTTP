"""
  Lesson 2: ex3.py
"""

# 1. Create a list containing three elements representing the
#    name, age, and occupation of a person.
#    Then, print the sentence using the elements with .format()

# INSERT YOUR CODE HERE

list = ["Taka", 60, "provisional associate TSE"]

print(list)

print('Bloody {0} is {1} years old and his role is {2}.'.format(*list))

print()


# 2. The dictionary should contain keys such as
#    'title', 'author', and 'publication_year'.
#    Use the .format() method with multiple positional arguments.
#    Example:
#    "The guidebook [title] by [author] was published in [publication_year]."

# INSERT YOUR CODE HERE

dict = {"title": "On the Origin of Species"
      , "author": "Charles Robert Darwin"
      , "publication_year": 1859}

print(dict)

print('The guidebook {title} by {author} was published in {publication_year}.'.format(**dict))

print()


# 3. The dictionary should hold details about a spaceship, such as
#    'name', 'type', and 'purpose'.
#    Use the .format() method with named arguments.
#    Example:
#    "The spaceship is called the [name]. It is a [type] used for [purpose]."

# INSERT YOUR CODE HERE

dict_space = {"name": "Enterprise"
      , "type": "battle ship"
      , "purpose": "conquest of galaxy"}

print(dict_space)

print('The spaceship is called {name}. It is a {type} used for {purpose}.'.format(**dict_space))

print('{0} {1} {2}'.format(*dict_space))
