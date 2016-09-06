# Create a program that output Celsius and Fanrenheit temperatures from 0 - 100 in 5 
  step increments table.
  
def main():
    ''' Create a table of Fanrenheit and Celsius temperature '''
    
# Set both Celsius and Fanrenheit total to zero
    cel = 0
    fan = 0
# Print out table title
    print("Fanrenheit\n (F) ")
# increments by 5 in the for loop
    for i in range(0, 101, 5):
# Calculate fanrenheit temperature
        fan = '{:5.2f}'.format(i + 32 * 9.0 / 5.0) + (' F')
# Print out fanrenheit temperature calculation
        print(fan)
# Print out table title
    print'{:>30}'.format('Celsius')
    print'{:>27}'.format('(C)')

# increments by 5 in the for loop
    for i in range(0, 101, 5):
# Calculate Celsius temperature
        cel = '{:05.2f}'.format(i - 32 * 5.0 / 9.0) + (' C')
# Print out Celsius temperature calculation 
        print'{:>30}'.format(cel)

main()
