
template = '{surname:>13} {name[0]}.{average:>10.2f}\n'
template1 = '{name:<25}{average:>10.2f}\n'

summa = 0
cnt = 0
with open('src.txt', encoding='utf-8') as src, open('dst.txt', 'w', encoding='utf-8') as dst:
    for line in src:
        lst = line.strip('\n').split()
        grad = sum([int(grad) for grad in lst[2:]]) / len(lst[2:])
        res = template.format(
            surname=lst[1],
            name=lst[0],
            average=grad
        )

        res1 = template1.format(
            name=lst[1] + ' ' + lst[0][0] + '.',
            average=grad
        )
        dst.write(res1)
        if grad < 5:
            print(res1, end='')

        summa += grad
        cnt += 1


print()
print('Class average: ', round(summa / cnt, 2))
