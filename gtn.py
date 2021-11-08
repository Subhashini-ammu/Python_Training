def check(a, b, c):
    num = [a, b, c]

    if check_int(a) and check_int(b) and check_int(c):
        return max(num)
    elif check_float(a) and check_float(b) and check_float(c):
        return max(num)
    elif check_float(a) and check_float(b) and check_int(c):
        return max(num)
    elif check_float(a) and check_int(b) and check_int(c):
        return max(num)
    elif check_int(a) and check_float(b) and check_float(c):
        return max(num)
    elif check_int(a) and check_int(b) and check_float(c):
        return max(num)
    elif check_int(a) and check_float(b) and check_int(c):
        return max(num)
    elif check_float(a) and check_int(b) and check_float(c):
        return max(num)
    else:
        return "error"


def check_int(x):
    if type(x) == int:
        return True
    else:
        return False


def check_float(x):
    if type(x) == float:
        return True
    else:
        return False
