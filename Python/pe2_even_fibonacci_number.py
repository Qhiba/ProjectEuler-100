"""
##Even Fibonacci Number
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

problem link: https://projecteuler.net/problem=2
solver: Akbar H. Harahap
"""
#region Brute Force to find even Fibonacci numbers
def brute_force_fibonacci_even(limit):
    fibonacci_numbers = fibonacci(limit)
    fibonacci_even = []
    for i in range(len(fibonacci_numbers)):
        if fibonacci_numbers[i] % 2 == 0:
            fibonacci_even.append(fibonacci_numbers[i])
    
    return fibonacci_even
#endregion

# Populate fibonacci numbers until it reach or found "limit" number.
def fibonacci(limit):
    fibonacci_numbers = []
    i = 0
    while len(fibonacci_numbers) == 0 or fibonacci_numbers[-1] <= limit:
        if i == 0:
            fibonacci_numbers.append(1)
        elif i == 1:
            fibonacci_numbers.append(2)
        else:
            next_number = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
            fibonacci_numbers.append(next_number)
        i += 1

    return fibonacci_numbers



def main():
    limit = 4000000
    #print(fibonacci(limit))
    print(sum(brute_force_fibonacci_even(limit)))


if __name__ == "__main__":
    main()