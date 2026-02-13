def plus(a: int, b: int) -> int:
    return a + b


a = int(input())
b = int(input())

action = input()

if action == "+":
    print(plus(a, b))