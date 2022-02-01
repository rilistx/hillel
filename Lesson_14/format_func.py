
print('Test sting - {players[0]}:{players[1]}:{players[2]}'.format(players=['1', '2', '3']))

s = '{:<30}'.format('left aligned')                 # 'left aligned                  '
print(s)
s = '{:>30}'.format('right aligned')                # '                 right aligned'
print(s)
s = '{:^30}'.format('centered')                     # '           centered           '
print(s)
s = '{:*^30}'.format(' centered ')                  # '********** centered **********'
print(s)

s = '{:+f}; {:+f}'.format(3.14, -3.14)              # '+3.140000; -3.140000'
print(s)
s = '{: f}; {: f}'.format(3.14, -3.14)              # ' 3.140000; -3.140000'
print(s)
s = '{:-f}; {:-f}'.format(3.14, -3.14)              # '3.140000; -3.140000'
print(s)

print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(37))

points = 19.5
total = 22
print('Correct answers: {:.2%}'.format(points / total))     # 'Correct answers: 88.64%'
