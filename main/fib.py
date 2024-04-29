def fib(n):
    if not isinstance(n, int) or n < 0:
        return None
    if n == 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

