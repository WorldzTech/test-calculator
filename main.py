def plus(a: int, b: int) -> int:
    return a + b

def minus(a: int, b: int) -> int:
    return a - b

def division(a: int, b: int) -> int:
    return a/b

a = int(input())
b = int(input())

action = input()

if action == "+":
    print(plus(a, b))

if action == "-":
    print(minus(a, b))

if action == "/":
    print(division(a, b))