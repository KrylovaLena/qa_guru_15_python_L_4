# Списки
l = [1, 2, 3, 'a', 'c', [4, 5, 6]]
print(l[0])
print(l[-1])
print(l[-1][0])
print(l[::-1])

l.append('new_element')
print(l)
l.extend(['elementt', 'another3'])
print(l)
print(len(l))


l[0] = 200
print(l)

# Множества

s1 = {1, 2, 3, 4}
s2 = {1, 2, 5, 5}
print(s1)
print(s2)

# пересечение двух множеств
p = s1.intersection(s2)
print(p)
p = s1 - s2
print(p)