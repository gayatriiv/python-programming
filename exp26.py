def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def list_primes(limit):
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes

# Get user input for the limit
limit = int(input("Enter a limit to find all prime numbers up to: "))
prime_numbers = list_primes(limit)

print("Prime numbers up to", limit, "are:", prime_numbers)

