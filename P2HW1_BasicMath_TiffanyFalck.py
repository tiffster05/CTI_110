
def main():
    #INPUT
    #Ask user for 1st number & store input
    num1 = int(input('What is your first number?'))

    #Ask user for @nd number & store input
    num2 = int(input('What is your second number?'))


    #PROCESS
    #Add num1 & num2 & store sum
    mathsum = num1 + num2
    #Multiply num1 & num2 & store result
    result = num1 * num2


    #OUTPUT
    #Display num1, num2, sum & result
    print('Users first number: ', num1)
    print('Users second number: ', num2)
    print('Sum of numbers: ', mathsum)
    print('Result of numbers: ', result)

main()
