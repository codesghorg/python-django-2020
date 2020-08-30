#print('show anything here')

# bv = True or False
# bv2 = True or True

# c1 = False or False

# d1 = True and False

# n1 = not True

# n2 = not False

# combined = True or False and not False

# # print(combined)

# v = 3 <= 3

# if v:
#     print('It is true')
# else:
#     print('It is false')


name = 'Kofi'

balance = 3009

message = 'Hello '+name+' Please enter how much you want to withdraw: '

amt = input(message)

# print(type(amt))

amt = float(amt)

# print(type(amt))

if amt > balance:
    print('You don not have enough money to withdraw '+ str(amt) )
else:
    print('You have withdrawn '+ str(amt))
    print('Now your new balance is '+ str(balance - amt))
