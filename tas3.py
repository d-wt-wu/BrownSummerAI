from math import pow as power
from math import sqrt as square
from random import randint as randomintegers
from random import shuffle as shuffles
from random import choice as choices

result_1 = power(2, 4)
print(result_1)

result_2 = square(16)
print(result_2)

result_3 = randomintegers(0, 100)
print(result_3)

names = ["A", 'B', 'C', 'D', 'E']
print(names)

shuffles(names)
print(names)

result_4 = choices(names)
print(result_4)