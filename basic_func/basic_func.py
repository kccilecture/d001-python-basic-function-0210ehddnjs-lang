def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def power(base, pow):
    return base**pow


def square(base):
    return base*base


def greet(이름="낯선자", 나이=20):
    if 나이 >= 50:
        인사말 = "안녕하십니까"
    elif 나이 <= 10:
        인사말 = "안녕"
    else:
        인사말 = "안녕하신가"
    return f"{인사말} {이름}!"