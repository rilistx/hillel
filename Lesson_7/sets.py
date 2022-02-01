# {4, 6, 8, }

# s = {}
s = set()
print(s, type(s))

s = set('Hello World!')
print(s, type(s), len(s))

s1 = {1, 2, 3}
s2 = {3, 1, 2, 3, 2}
print(s1, s2, s1 == s2)

for element in s1:
    print(element)

print(2 not in s2)

s2.add(5)
print(s2)

# remove()
# discard()
s1.remove(2)
print(s1)
s2.discard(8)
print(s2)

# pop()
x = s2.pop()
print(x, s2)

s1 = {5, 8, 6, 3, 7, 4, 2}
s2 = {9, 8, 3, 6, 1, 0, 5}

# A | B     A.union(B)    A.update(B)   A |= B
print(s1 | s2)

# A & B     A.intersection(B)   A.intersection_update(B)   A &= B
print(s1 & s2)

# A - B     A.difference(B)     A.difference_update(B)      A -= B
print(s1 - s2)

# A ^ B     A.symmetric(B)      A.symmetric_update(B)       A ^= B
print(s1 ^ s2)
print(s1 - s2 | s2 - s1)

# A.isdisjoin(B)
print(s1.isdisjoint(s2))

s0 = frozenset('Hello World!')
print(s0, type(s0))
