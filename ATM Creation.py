print('Welcome to welbere bank.')
print('Please put your card in.')
card = int(input('Put in your pin number: '))
if card == (1234):
    print('1 = withdraw money')
    print('2 = check balance')
    print('3 = both')
    option = int(input('please pick one of the above: 1 2 or 3: '))
    if (option == 1):
        money=int(input('How much would you like to withdraw: '))
        print('please take your cash (and coins)')
    if(option == 2):
        balance = print('Your balance is 678,456')
    if (option == 3):
        print('Your balance is 678,456')
        money=int(input('How much would you like to withdraw: '))
        print('please take your cash (and coins)')
else:
    print('pin incorrect')
