"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f"Number of primes = {number_of_primes}. Should have been an integer greater than 0.")
    list = []
    i = 2
    list.append(i)
    while len(list) < number_of_primes:
        prime = True
        i = i + 1
        for j in range (2,i):
            if i % j == 0:
                prime = False
                break
        if prime == True:
            list.append(i)
    return list
