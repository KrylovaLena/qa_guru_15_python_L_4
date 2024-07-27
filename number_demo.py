from decimal import Decimal
a = 123
a = a + 456
print('a = ' + str(a))
print(type(a))

b = 0.1 + 0.2
print('b = ' + str(b))


import math

print(math.pi)


import random
#  добавить константу random.seed, чтобы сгенерированные данные не менялись от теста к тесту
random.seed("another word")
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

# округрение первого числа до количества знаков после запятой, равной второму числу
print(round(1.3445566, 2))

