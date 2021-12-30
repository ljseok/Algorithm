import random
import numpy as np

mylist = ["apple", "banana", "cherry"]
x = np.array((2,3,21,312,31,31,3123,131))

print(x)
print(mylist)

random.shuffle(mylist)
random.shuffle(x)

print(x)
print(mylist)
