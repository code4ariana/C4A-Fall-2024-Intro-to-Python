"""
This is a simple calculator using functions
"""
# Function Definition
def menu():
    print("Python Calculator")
    print("-----------------")
    print("Select the following menu options:\n")
    print("1. Addition\n")
    print("2. Subtraction\n")
    print("3. Product\n")
    print("4. Float Division\n")
    print("5. Integer Division\n")
    print("6. Exponent\n")
    print("7. Remainder\n")
    print("-----------------")
    
    
def addition(number1, number2):
    # Add 2 numbers
    total = number1 + number2
    return total

def subtract(number1, number2):
    
    # Subtract 2 numbers
    subtract = number1 - number2
    
    return subtract

def product(number1, number2):
    
    # Product 2 numbers
    product = number1 * number2
    return product

def division(number1, number2):
    
    # Divide 2 numbers with float division
    div = number1 / number2
   
    return div

def IntDivision(number1, number2):

    # Divide 2 numbers with integer division
    Idiv = number1 // number2
    
    return Idiv

def exponent(number1, number2):
    
    # Exponent
    exponent = number1 ** number2
    
    return exponent

def remainder(number1, number2):
    
    # Modulus
    mod = number1 % number2
  
    return mod

def main():
    # Call menu function
    menu()
    menu_selection = int(input("Enter your choice: "))
    number1 = float(input("Enter 1st number: "))
    number2 = float(input("Enter 2nd number: "))
    
    if menu_selection == 1:
        print("Total 2 numbers is: ", addition(number1, number2)) # Call/invoke addition function
    elif menu_selection == 2:
        print("Subtraction of 2 numbers is: ", subtract(number1, number2))
    elif menu_selection == 3:
        print("Product of 2 numbers is: ", product(number1, number2))
    elif menu_selection == 4:
        print("Division of 2 numbers is: ", division(number1, number2))
    elif menu_selection == 5:
        print("Division of 2 numbers is: ", IntDivision(number1, number2))
    elif menu_selection == 6:
        print("Exponent of 2 numbers is: ", exponent(number1, number2))
    elif menu_selection == 7:
        print("Remainder of 2 numbers is: ", remainder(number1, number2))
    else:
        print("We don't have the menu option you've selected, select only the available options")
        

# Call main function
main()





