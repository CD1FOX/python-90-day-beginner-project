def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % 2 == 0:
            return False
    return True

print(is_prime(4))
print(is_prime(90))
print(is_prime(102))