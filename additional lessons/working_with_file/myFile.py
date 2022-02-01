mid_grade = 0
mid_count = 0

print("   ### Студенты, чей бал ниже 5 ### ")
print("--------------------------------------")

with open("src.txt", encoding='utf-8') as src_file, open("drc.txt", 'w', encoding='utf-8') as drc_file:
    lineFile = ""
    myFile = src_file.readlines()

    for i in myFile:
        suma = 0
        count = 0
        lineFile = i.split()

        for i in range(2, len(lineFile)):
            suma += int(lineFile[i])
            count += 1

        res = round(suma / count, 2)
        mid_grade += res
        mid_count += 1
        lineFile = [lineFile[1], lineFile[0][0] + '.', str(res)]
        newFile = f'{lineFile[0]} {lineFile[1]} ' \
                  f'{(25 - (len(lineFile[0]) + len(lineFile[1]) + len(lineFile[2]))) * " "} {lineFile[2]}'
        if res > 5:
            print(f'{lineFile[0]} {lineFile[1]} '
                  f'{(26 - (len(lineFile[0]) + len(lineFile[1]))) * " "} | '
                  f'{(6 - len(lineFile[2])) * " "} {lineFile[2]}')

        drc_file.write(newFile + '\n')


print("--------------------------------------")
print(f"Средний бал всей группы:     |    {round(mid_grade / mid_count, 2)}")
