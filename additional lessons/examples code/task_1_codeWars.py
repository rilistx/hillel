def sum_pairs(ints, s):
    num = set()
    for i in ints:
        if s - i in num:
            return [s - i, i]
        num.add(i)
    return None
