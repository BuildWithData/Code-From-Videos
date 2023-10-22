

def append(number, ls=[]):
    ls.append(number)
    return ls


def pythonic_append(number, ls=None):
    if ls is None:
        ls = []
    ls.append(number)
    return ls
