s = "Hello, world!"
print('s = ' + s)
print(type(s))

s = 'He"llo, wor"ld!'
print('s = ' + s)
print("*************************")


s = """Hello, world!"""
print('s = ' + s)
print("*************************")

s = '''Hel
lo, wor
ld!'''
print('s = ' + s)
print("*************************")

s = 'Hello, \' "world!'
print('s = ' + s)
print("*************************")

s = 'Hello, \n world!'
print('s = ' + s)
print("*************************")


# Сырые строки
s = 'Hello, \\ "world!'
print('s = ' + s)
print("*************************")

s = r'Hello, \n world!'
print('s = ' + s)
print("*************************")

# индексы и слайсы (срезы)

email = "user@yandex.ru"
print(email[1])
print("*************************")
print(email[-2])
print("*************************")
print(email[0:5])
print("*************************")
print(email[:5])
print("*************************")
print(email[:5:2])
print("*************************")
# развернуть строку
print(email[::-1])
print("*************************")
# сделать первую букву заглавной
print(email.title())
print("*************************")
# проверить, что окончание соответствует
print(email.endswith('@yandex.ru'))
print("*************************")

# разделить строку на значение до и после указанного символа
print(email.split("@"))
print("*************************")



# Форматирование
a = "Hello"
b = "world"

print(a + b)
print("*************************")

print(a + ", " + b + "!")
print("*************************")

print("{a}, {b}!".format(a=a, b=b))
print("*************************")

print(f'{a}, {b}!')
print("*************************")

print(f'{a}, {b.upper()}!')
print("*************************")

print(f'{a=}, {b=}!')
print("*************************")

print("%s, %s!" % (a,b))
print("*************************")

s ="12345"
n = 12345
assert s == str(n)
assert int(s) == n

