def get_prime_numbers(num):
    factors = list()
    divisor = 2
    num = int(input())

    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num = num / divisor
        else:
            divisor += 1
    return factors

print(get_prime_numbers(13))

    