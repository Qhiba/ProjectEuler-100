def search_factor(number):
    factors = []

    value = 0
    denominator = 2
    while not value == 1:
        value = number / denominator
        if not value % 1 == 0:
            denominator += 1
            continue

        if denominator not in factors:
            factors.append(denominator)
        
        number = value
        denominator += 1
    return factors

def searh_largest_prime(number_list):
    largest_num = 0
    for i in number_list:
        # 0 and 1 are not prime
        if i < 2:
            return False

        # check for factors from 2 to the square root of the i
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                return False

        # if no factors found, the number is prime
        if largest_num < i:
            largest_num = i
    
    return largest_num

def main():
    number = 600851475143
    number_factors = search_factor(number)
    print(searh_largest_prime(number_factors))
    return

if __name__ == "__main__":
    main()