# create a program that print out prime numbers
def main():
    ''' Show prime numbers '''
# Create an empty number list
num_list = []

# Create a for loop that runs thru numbers from 0 to 101
for number in range(0, 101):
    # Check each number to see if it is a prime number
    if number % 2 == 1:
        # Adds only the prime numbers to the empty number list
        num_list.append(number)
        # Prints out the list of prime numbers
        print(number, "is a Prime number")


if __name__ == "__main__":
    main()
