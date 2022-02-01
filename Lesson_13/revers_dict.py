from pprint import pprint

d = {
    'apple': ['malum', 'pomum', 'popula', 'one', 'two'],
    'fruit': ['baca', 'bacca', 'popum', 'test', 'one'],
    'punishment': ['malum', 'multa', 'test', 'two', 'one']
}

d1 = {}
for key, value in d.items():
    for element in value:
        if element not in d1:
            d1[element] = []

        d1[element].append(key)

pprint(d1)
