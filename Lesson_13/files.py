import os

print(os.sep)

# .
# ..

# \n
# \r

# Win       \r\n
# linux     \n
# MacOs     \r


# open(file_name, mode, encoding)

"""
    r           read            default
    w           write
    x           exclusive
    a           append
        ------------------------------------
    t           text            default
    b           binary
        ------------------------------------
    +           mix (read/write)
"""

file = open('test.txt', 'a', encoding='utf-8')
file.write('Привет Мир!')
file.write('\n')

if not file.closed:
    file.close()
