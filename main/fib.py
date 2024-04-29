# Числа Фибоначчи — числовой ряд, при котором каждое последующее число равно сумме двух предыдущих

# Получить число Фибоначчи по его номеру
def fib(n):
    if not isinstance(n, int) or n < 0:
        return None
    elif n == 0:
        return None
    elif n == 1:
        return 0
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b if n >= 2 else 1
