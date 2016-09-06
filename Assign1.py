# Create a small python3 program that convert temperature
def main():
    '''Ask the user to input a number in Fahrenheit 
    and convert it to Celsius and print both on the screen '''

# Set Celsius count to zero
cel = 0

# Welcome user to temperature convert program
print("\nWelcome to the temperature convert program")

# Ask the user to enter a temperature in fahenheit
fan = float(input("Please enter a temperature in Fahrenheit: "))

# Convert Fahrenheit temperate to celsius
cel = round((fan - 32) * 5 / 9, 1)

# Display the temperature in both Fahrenheit and Celsius
print("The temperature in Celsius is : {}".format(cel))
print("The temperature in Fahrenheit is : {}".format(fan))


main()
