def myfunc(*args):
    out = []
    for num in args:
        if num % 2 == 0:
            out.append(num)
    return out

def myfunc2(*args):
    return [x for x in args if x % 2 == 0]