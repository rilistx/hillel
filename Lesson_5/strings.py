#
# """
#
#  chr()
#  ord()
#
# """
#
# # 0x26bd
# print(chr(0x26bd))
# print('\u26bd')     # \u - 2b   \U - 4b
# print(chr(9917))
#
# print(ord('⚽'))
# print(hex(ord('⚽')))
#
# wave = '~'
# boat = '\U0001f6a3'
# seagull = '\u033c'
# fish = '\U0001f41f'
# penguin = '\U0001f427'
# wale = '\U0001f40b'
# octopus = '\U0001f419'
#
# seagull_row = wave * 11 + seagull + wave * 15 + '\n'
# row = wave * 10 + boat + wave * 15 + '\n'
# fish_row = wave * 4 + fish + wave * 21 + '\n'
# wale_row = wave * 10 + wale + wave * 15 + '\n'
# penguin_row = wave * 7 + penguin + wave * 18 + '\n'
# octopus_row = wave * 17 + octopus + wave * 8 + '\n'
#
# sea = seagull_row + row + fish_row + wale_row + penguin_row + octopus_row
# print(sea)
#
# print('\u2764')
#
# print('Hello ' * 5)
#
# # n1 = input('enter a num1: ')
# # n2 = input('enter a num2: ')
# # print(int(n1) + int(n2))
#
# s = 'Process finished with exit code 0'
#
#
#
# #  0  1  2  3  4
# #  H  E  L  L  O         ==> HELLO
# # -5 -4 -3 -2 -1
#
# print(s[0])
# print(s[-1])
#
# # s[0] = '7'        ERROR
# # print(s[35])
# # print(s[-55])
# # str[start: stop: step]
# print(s[8: 16: 2])
# print(s[8:])
# print(s[: 16])
# print(s[::2])
# print(s[8: 34572347845])
# print(s[::-1])
# print('12345'[::-1])
#
# for i in range(0, len(s), 2):
#     print(s[i], end='')
# print()
#
# print(s[::2])
#
# for symbol in s:
#     print(symbol, end=' ')
# print()
#
# for i in range(len(s)):
#     print(s[i], end=' ')
# print()


s = 'Process finished with exit code 0'

# len(str)
print(len(s))

# find(sub, start, end)
# rfind(sub, start, end)
idx = s.find('i')
print(idx)
idx = s.find('i', idx + 1)
print(idx)
idx = s.find('i', idx + 1)
print(idx)
idx = s.find('i', idx + 1)
print(idx)
idx = s.find('i', idx + 1)
print(idx)

print(s.find('finished'))

# replace(old, new, count)
print(s.replace('i', 'I', 2))
print(s.replace('finished', 'finished'.upper()))

# count(str)
print(s.count('i'))
print(s.count('finished'))

s = 'prOceSs fINished wITh eXit cOde 0'
# capitalize()
print(s.capitalize())

# upper()
# lower()
print(s.upper())
print(s.lower())

# title()
print(s.title())

# strip(str)
s = '3333333             Hello     World!    3333333'
print("'" + s + "'")
print("'" + s.strip('3').strip().upper() + "'")

s = 'prOceSs       fINiiiished        wITh         eXit                         cOde 0'
# split()
# join()
lst = s.lower().split('i')
print(lst)
s = ' '.join(lst)
print(s)
