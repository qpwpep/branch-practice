def fibo(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

if __name__ == '__main__':
    print(fibo(4))
