d = {}
print(d, type(d))
d = {0: 'zero', 1: 'one', 2: 'two'}
print(d, type(d))
d = dict()
print(d, type(d))
d = dict(
    [
        (0, 'zero'),
        (1, 'one'),
        (2, 'two')
    ]
)
print(d, type(d))
print(d[2])

d = dict(
    one=1,
    two=2,
    zero=0
)
print(d, type(d))

print(d['one'])

d['one'] = 3
print(d)
d['four'] = 4
print(d)

d[6] = [3, 4, 5, 6]
print(d)
print(d[6][1])
d['d'] = {'name': 'Ivan', 'surname': 'Ivanov'}
print(d)
print(d['d']['surname'])

# len(dict)
print(len(d))

# clear()
# d.clear()
# print(d)

# get(key, def_value)
print(d.get('zero1', -1))

# keys()
print(d.keys())

# values()
print(d.values())

# items()
print(d.items())

# pop(key, def_value)
print(d.pop('d1', None))

# popitems()
print(d.popitem())

# update(dict)
x = {'a': 1, 'b': 5, 'two': 55}
d.update(x)
print(d)

# fromkeys(list)
d1 = dict.fromkeys([1, 3, 5, 6, 8])
print(d1)

a, b = 4, 6
for key, value in d.items():
    print(key, value)

for key in d.keys():
    print(key, d[key])
