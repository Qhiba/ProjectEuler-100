"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

problem link: https://projecteuler.net/problem=1
solver: Akbar H. Harahap
"""

#region Brute Force Method
def brute_force(below_num):
    sum_of_multiples = 0
    for i in range(below_num):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i
    
    return sum_of_multiples


def brute_force_shortened(below_num):
    return sum([i for i in range (below_num) if i % 3 == 0 or i % 5 == 0])
#endregion


#region Using Arithmetic Series Formula.
# Where "d" is the common difference value.
# "n" means it will sum until targetet n-th number.
# last_term is the last number of the series, it is the targeted n-th number.
# first_term is the first number of the series, the default is 1.
def sum_of_series(d, n=None, last_term=None, first_term = 1):
    if n is None and last_term is None:
        raise TypeError("sum_of_series() missing a required argument: ")
    elif n is not None and last_term is None:
        last_term = first_term + (n - 1) * d
    elif n is None and last_term is not None:

        # Even If the last_term is known, it still need to be verified by divide it by "d" to the nearest integer and multiple it by "d".
        # This is required so that last_term could be use for both the known last_term or last_term is below a number.
        last_term = (last_term // d) * d
        n = 1 + (last_term - first_term) // d
    
    total_sum = (n * (first_term + last_term)) // 2

    return total_sum

# This method is specialy to series of number that is the multiples of common difference value or "d"
# "target" is the targeted number, it can be use for limiting the sum before "target" or be the last term of the series.
def sum_of_series_multiples(d, target):
    # "term" is the number inside the series, usually it is the middle number of the series.
    # To find it, we need to divide "target" by "d" to the nearest integer.
    term = target // d

    # The basic form of series that consist of number that is multiples of "d" is where d = 1, series = 1, 2, 3, 4, 5,..., term.
    # From this form we can be sure that if the "d" is other than 1, let's say d = 3, the series will be 1 * 3, 2 * 3, 3 * 3, ..., term * 3 => 3, 6, 9, ..., 3*term.
    # We can simplify this to 3 * (1, 2, 3, ..., term);
    # using the previous sum_of_series() total_sum, where the first_term = 1, last_term = term, and n = 1 + (last_term - first_term) // d, we will get.
    total_sum = d * (term * (term + 1)) // 2

    return total_sum
#endregion


def main():
    below_num = 1000
    sum_with_brute_force = brute_force(below_num)
    sum_with_brute_force_shortened = brute_force_shortened(below_num)
    
    print(f"Using brute_force method the sum of all multples of 3 or 5 below {str(below_num)} is \t\t= {str(sum_with_brute_force)}")
    print(f"Using brute_force_shortened method the sum of all multples of 3 or 5 below {str(below_num)} is \t= {str(sum_with_brute_force_shortened)}")

    # Don't forget to substract target parameter by one if you searching total sum below target number on the last_term parameter.
    print(f"Using Arithmetic Series Formula method the sum of all multples of 3 or 5 below {str(below_num)} is \t= {str(sum_of_series(3, last_term=below_num-1, first_term=3) + sum_of_series(5, last_term=below_num-1, first_term=5) - sum_of_series(15, last_term=below_num-1, first_term=15))}")

    # Don't forget to substract target parameter by one if you searching total sum below target number on the target parameter.
    print(f"Using Arithmetic Series Formula method for 'multiples of' number series the sum of all multples of 3 or 5 below {str(below_num)} is = {str(sum_of_series_multiples(3, below_num-1) + sum_of_series_multiples(5, below_num-1) - sum_of_series_multiples(15, below_num-1))}")

if __name__ == "__main__":
    main()