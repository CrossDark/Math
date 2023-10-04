from algebra import output, recursion, positive_integer


class EndError(Exception):
    pass


def calculate(num: int):
    """

    :rtype: int
    """
    global recursion
    global output
    recursion += 1
    if num == 1:
        output.append(1)
        output.append('总共' + str(recursion) + '次')
        raise EndError()
    if num % 2 == 0:
        output.append(num)
        calculate(int(num / 2))
    else:
        output.append(num)
        calculate(int(num * 3 + 1))


def main(get):
    global recursion
    try:
        del output[0: -1]
        del output[-1]
    except IndexError:
        pass
    try:
        recursion = 0
        calculate(positive_integer(get))
    except TypeError:
        pass
    except OverflowError:
        output.append('数太大')
        pass
    except EndError:
        pass
    else:
        pass
    finally:
        pass
    return output


def collatz(got):
    def inside():
        while True:
            get = main(got(False, '输入正整数'))
            for iter_ in get:
                got(True, iter_)
    return inside


@collatz
def display(mode: bool, data: str):
    if not mode:
        return input(data)
    elif mode:
        print(data)

    
if __name__ == '__main__':
    display()
