age = 23
name = 'Кирилл'

# Добавление переменных с помошью .format
print('My name is  {0}.'.format(name))
print('{0}у {1} года.'.format(name, age))
print('{0:_^11}'.format('hello'))

a = 5
print(a)
a += 1
print(a)

# Добавление переменных с помошью %s
print('Переменая а равна %s' % a)

s = 'тут я напишу \
всё что я хочу'
print(s)
