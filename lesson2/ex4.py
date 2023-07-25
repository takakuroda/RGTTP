"""
  Lesson 2: ex4.py
"""

# 1. Print the formatted keys and values of the dictionary.
#    versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

# INSERT YOUR CODE HERE

versions = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

print(versions)

print("RHOSP " + ('{Stein}'.format(**versions)) + " is based on " + ('{0}'.format(*versions)))
print("RHOSP " + ('{Train}'.format(**versions)) + " is based on " + ('{1}'.format(*versions)))
print("RHOSP " + ('{Wallaby}'.format(**versions)) + " is based on " + ('{2}'.format(*versions)))


#(k1, v1), (k2, v2), (k3, v3) = versions.items()

#print(k1)
#print(v1)
#print(k2)
#print(v2)
#print(k3)
#print(v3)

#print(str(v1) + " is based on " + k1)
#print(str(v2) + " is based on " + k2)
#print(str(v3) + " is based on " + k3)

print()


# 2. Print {} around the version numbers.

# INSERT YOUR CODE HERE

print("RHOSP {" + ('{Stein}'.format(**versions)) + "} is based on " + ('{0}'.format(*versions)))
print("RHOSP {" + ('{Train}'.format(**versions)) + "} is based on " + ('{1}'.format(*versions)))
print("RHOSP {" + ('{Wallaby}'.format(**versions)) + "} is based on " + ('{2}'.format(*versions)))

print()


# 3. Print numbers in decimal, byte and hexadecimal form.

# INSERT YOUR CODE HERE
