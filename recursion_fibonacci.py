def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(5))


def fibonacci(n):
    if n == 2:
        return 1
    if n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(5))

def fibonacci2(n):
    if n == 2 or n == 1:
        return 1
    else:
        return (fibonacci2(n-1) + fibonacci2(n-2))

print(fibonacci2(5))