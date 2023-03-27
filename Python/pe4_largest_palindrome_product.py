def find_palindrome():
    max_palindrom = 0
    max_i = 0
    max_j = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j

            if str(product) == str(product)[::-1]:
                if product > max_palindrom:
                    max_palindrom = product
                    max_i = i
                    max_j = j

    return max_palindrom, max_i, max_j

def main():
    palindrom, a, b = find_palindrome()
    print(f"The largest Palindrom product made from 3-digit number is {palindrom}, the product came from multiplying {a} and {b}.")
    return

if __name__ == "__main__":
    main()