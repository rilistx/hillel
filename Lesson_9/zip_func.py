# zip(*collection)
name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]

name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]

dict_res = dict(zip(name_hero, name_real))
list_res = list(zip(name_hero, name_real))
print(dict_res)
print(list_res)

# rev_dict_res = list(zip(*dict_res))
# print(rev_dict_res)
#
# rev_list_res = list(zip(*list_res))
# print(rev_list_res)
#
# a, b = ([', '.join(x)] for x in rev_list_res)
#
# print(a, b)
