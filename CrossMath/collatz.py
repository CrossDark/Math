recursion = 0


class EndError(Exception):
    pass


def calculate(num: int):
    """

    :rtype: int
    """
    global recursion
    recursion += 1
    if num == 1:
        print(1)
        print('总共' + str(recursion) + '次')
        raise EndError()
    if num % 2 == 0:
        print(num)
        calculate(int(num / 2))
    else:
        print(num)
        calculate(int(num * 3 + 1))


def determine(get):
    if get == '':
        return
    try:
        get = int(get, 16)
    except ValueError:
        pass
    try:
        get = int(get)
    except ValueError:
        print('这不是正整数')
        return
    if get <= 0:
        print('这不是正数')
        return
    return get

    
if __name__ == '__main__':
    while True:
        try:
            recursion = 0
            calculate(determine(input('输入正整数')))
        except TypeError:
            pass
        except OverflowError:
            print('数太大')
            pass
        except EndError:
            pass
