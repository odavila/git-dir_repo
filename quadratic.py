# Create a quadratic program
def main():
    ''' Create a quadratic program '''
# Set all totals to zero
    A_value = 0
    B_value = 0
    C_value = 0
    X_vlaue = 0
    Q_tot_value =0
    
    def quadratic():
        " Ask user to enter numbers"
# Print welcome message and ask user to enter numbers
        print("Welcome to the Program! ")
        print("Please enter the value of A, B, C, and X at the corresponding prompts")

        A_value = (int(input("What is the value of A: ")))
        B_value = (int(input("What is the value of B: ")))
        C_value = (int(input("What is the value of C: ")))
        X_value = (int(input("What is the value of X: ")))
# Calculate the value of the quadratic
        Q_tot_value = ((A_value)*((X_value)*(X_value)) + (B_value)*(X_value) + (C_value))

# Print the display of the quadratic
        message = ("{0}{1}^{2}+{3}{1}+{5}".format(A_value, 'X', '2', B_value, 'X', C_value))
        print("The following quadratic was entered: " + str(message))
# Print vaule of the quadratic
        print("The value of the quadratic is : %d" % int(Q_tot_value))
        
        
    quadratic()
if __name__ == "__main__":
    main()

