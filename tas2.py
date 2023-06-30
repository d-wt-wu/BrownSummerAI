import math as cal
import random as rd

result_1 = cal.pow(2, 4)
print(result_1)

result_2 = cal.sqrt(16)
print(result_2)

result_3 = rd.randint(0, 100)
print(result_3)

names = ["A", 'B', 'C', 'D', 'E']
print(names)

rd.shuffle(names)
print(names)

result_4 = rd.choice(names)
print(result_4)