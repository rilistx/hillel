
def measure_time(value):
    from datetime import datetime
    print(value)

    def outer(function):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            res = function(*args, **kwargs)
            print(datetime.now() - start)
            return res
        return wrapper
    return outer


@measure_time('Hello')
def gen_1(param):
    lst = []
    for i in range(param):
        if i % 2 == 0:
            lst.append(i)
    return lst


@measure_time('World')
def gen_2(param):
    lst = [x for x in range(param) if x % 2 == 0]
    return lst


print(len(gen_1(10**5)))
print(len(gen_2(10**5)))

# r = measure_time(gen_1)
# print(r)
# r()
