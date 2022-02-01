# map(func_ref, collection)

# def fahrenheit(temperature):
#     return round(((float(9)/5)*temperature + 32), 2)


# def celsius(temperature):
#     return round((float(5)/9)*(temperature-32), 2)


# lst = []
temperatures = (36.5, 37, 37.5, 38, 39)
# for t in temperatures:
#     lst.append(fahrenheit(t))
# print(lst)


# F = map(fahrenheit, temperatures)
# print(F)
# C = map(celsius, F)
# print(list(C))

F1 = list(map(lambda t: round(((float(9) / 5) * t + 32), 2), temperatures))
print(F1)
C1 = list(map(lambda t: round((float(5) / 9) * (t - 32), 2), F1))
print(C1)
