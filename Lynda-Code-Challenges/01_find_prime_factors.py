factors = []
divisor = 2
num = int(input())

while divisor <= num:
    if (num % divisor) == 0:
        factors.append(divisor)
        num = num / divisor
    else:
        divisor += 1

print(factors)