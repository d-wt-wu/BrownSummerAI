# David Wu
# From module import some_item

from math import pow
from math import sqrt
from random import randint
from random import shuffle
from random import choice

result_1 = pow(2, 4)
print(result_1)

result_2 = sqrt(16)
print(result_2)

result_3 = randint(0, 100)
print(result_3)

names = ["A", 'B', 'C', 'D', 'E']
print(names)

shuffle(names)
print(names)

result_4 = choice(names)
print(result_4)