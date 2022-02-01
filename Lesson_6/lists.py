# a = []
# print(a, type(a))
#
# a = list()
# print(a, type(a))
#
# a = list('Hello World!')
# print(a, type(a))
#
# # a = list(213412334)
# # print(a, type(a))
#
# a = list(str(213412334))
# print(a, type(a))
#
# a = [1, 5, 7, 8, 6]
# print(a, type(a))
#
# a = [2342, 'dsfsdf', 78.67, True]
# print(a, type(a))
#
# print(a[3])
#
# a = list('Hello World!')
# print(a, type(a))
#
# print(a[2: -2: 2])
# print(a[::-1])
#
# for i in range(len(a)):
#     print(a[i], end=' ')
# print()
#
# for element in a:
#     print(element, end=' ')
# print()
#
# for idx, element in enumerate(a, 10):
#     print(idx, element)
#
# a1 = [1, 2, 3, 4, 5]
# b1 = [6, 7, 8, 9, 0]
# c1 = a1 + b1
# print(c1)
#
# c2 = a1 * 4
# print(c2)
#
# c3 = [0] * 10
# print(c3)

a1 = [1, 2, 3, 4, 5]
c2 = a1 * 4

# len(lst)
print(len(c2))

# append(new_el)
print(a1)
a1.append(45)
print(a1)

# del
del a1[2]
print(a1)

# del a1
# print(a1)

# pop(idx)
x = a1.pop(1)
print(x, a1)

# count(value)
a1 = a1 * 3
print(a1.count(5))

# clear()
# a1.clear()
# print(a1)

# extend(lst)
a1 = [1, 2, 3, 4, 5]
b1 = [6, 7, 8, 9, 0]
c1 = a1 + b1        # a1 += b1
print(id(a1), a1, id(b1), b1)
# a1 += b1
# print(id(a1), a1)
print(id(c1), c1)

a1.extend(b1)
print(a1)

# index(value)
print(a1.index(5))

# insert(idx, value)
print(a1)
a1.insert(5, 99)
print(a1)

# a1[5] = 55
# print(a1)

# remove(value)
a1.remove(99)
print(a1)

print(id(a1), a1)
x1 = a1[::-1]
print(id(x1), x1)
a1.reverse()
print(id(a1), a1)

# in
print(a1)
print(5 in a1)
print(55 in a1)
