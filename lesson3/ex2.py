def digit_root(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    if result > 9:
        return digit_root(result)
    else:
        return result