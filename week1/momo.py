momo_code = input("Please enter your momo code: ")

balance = 9000

if momo_code != "*170#":
    print("Sorry Wrong MoMo Code!!!")
else:
    menu = """
    1). Transfer Money
    2). MomoPay & Pay Bill
    3). Airtime & Bundles
    4). Allow Cash Out
    5). Financial Service
    6). My Wallet
    """
    print(menu)

    option = input('Enter your option here: ')

    if option == '1':

        menu = """
        1). Momo User
        2). Non Momo User
        """
        print(menu)
        option = input('Enter your option here: ')

        if option == '1':
            number1 = input('Enter receipient number: ')
            number2 = input('Enter receipient number again: ')

            if number1 != number2:
                print("Number don't match. Try Again.")
            elif len(number1) == 0:
                print('Number not provided')
            elif len(number1) != 10:
                print('Invalid number')
            else:
                amount = input('Enter amount to send ..')
                print(f"Amount of {amount} sent to {number1}")
        elif option == '2':
            print('Not implemented')
        else:
            print('Wrong Value chosen!!!')

    elif option == '2':
        print('Not implemented')
    elif option == '3':
        print('Not implemented')
    elif option == '4':
        print('Not implemented')
    elif option == '5':
        print('Not implemented')
    elif option == '6':
        print('Not implemented')
    else:
        print('Wrong Value chosen!!!')    

    


    


