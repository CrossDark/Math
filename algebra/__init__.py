recursion = 0
output = []


def positive_integer(get):
    global output
    if get == '':
        return
    try:
        get = int(get, 16)
    except ValueError:
        pass
    try:
        get = int(get)
    except ValueError:
        output.append('这不是正整数')
        return
    if get <= 0:
        output.append('这不是正数')
        return
    return get
