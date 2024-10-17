uInput = input('User 01: Enter Head or Tail: ')
guess = input('User 01: Enter Head or Tail: ')

if uInput == 'Head' and guess == 'Head':
    print('Head is the correct guess')
elif uInput == 'Head' and guess != 'Head':
    print('Sorry, it is a head')
elif uInput == 'Tail' and guess == 'Tail':
    print('Tail is the correct guess')
elif uInput == 'Tail' and guess != 'Tail':
    print('Sorry, it is a tail')




