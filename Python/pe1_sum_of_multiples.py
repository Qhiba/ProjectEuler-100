"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

problem link: https://projecteuler.net/problem=1
solver: Akbar H. Harahap
"""

# Brute Force
def sum_of_multiples_of_3_or_5(sum_until):
    sum = 0
    for i in range(sum_until):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    
    return sum

def main():
    sum_until = 1000
    sum = sum_of_multiples_of_3_or_5(sum_until)

    
    print("Total sum of all multiples of 3 or 5 below " + str(sum_until) + " is = " + str(sum))

if __name__ == "__main__":
    main()