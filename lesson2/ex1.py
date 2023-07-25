"""
  Lesson 2: ex1.py
"""

# 1. Create a format string to display the name and age of a person.

# INSERT YOUR CODE HERE

name: str = "Taka"
age: int = 60

print(f'Bloody {name} is {age} years old.')

print('Bloody {} is {} years old.'.format(name, age))

print('Bloody {0} is {1} years old.'.format(name, age))

print('Bloody {1} is {0} years old.'.format(name, age))

print('Bloody {0} is {0} years old.'.format(name, age))

print('Bloody {1} is {1} years old.'.format(name, age))

print()


# 2. Print version with it's corresponding upstream codename,
#    and use padding aligned format to left, centre and right.

# INSERT YOUR CODE HERE

rhosp: int = 17
upstream: str = "Wallaby"

print(f'{("RHOSP " + str(rhosp) + " is based on " + upstream + "."):>50}')
print(f'{("RHOSP " + str(rhosp) + " is based on " + upstream + "."):^50}')
print(f'{("RHOSP " + str(rhosp) + " is based on " + upstream + "."):<50}')

print()

print(f'{("RHOSP " + str(rhosp) + " is based on " + upstream + "."):#>50}')
print(f'{("RHOSP " + str(rhosp) + " is based on " + upstream + "."):#^50}')
print(f'{("RHOSP " + str(rhosp) + " is based on " + upstream + "."):#<50}')

print()


# 3. Show different representations of an integer.

# INSERT YOUR CODE HERE

num:int = 987654321

print(bin(num))

print(oct(num))

print(hex(num))

print(type(bin(num)))

print(type(oct(num)))

print(type(hex(num)))

print()


# 4. Format a floating-point number with fixed precision.

# INSERT YOUR CODE HERE

float_num: float = 9876.54321

print(f'without formatting:   {float_num}')

print(f'decimal places 4:     {float_num:.4f}')

print(f'significant digits 6: {float_num:.6g}')

print()