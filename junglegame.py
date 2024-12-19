print('Welcome to Jungle Game')
choice1=input('enter choice 1 for left and 2 for right')
if choice1=='1':
    print('now you have further two options where to go')
    print('again press 1 to go further left ')
    print(' press 2 to go right')
choice2=input('enter choice from 1 or 2')
if choice2=='1':
    print('oops!you fell in a pit,Gameover')
elif choice2=='2':
    print('ohno!you are eaten by an animal,Again Gameover')
else:
    print('Invalid choice')
    
choice3=input(' again enter choice 1 for left and 2 for right')
if choice3=='1':
    print('now you have further two options to go')
    print('press 1 for left')
    print( 'press 2 for right')
choice4=input('enter choice 1 for left and 2 for right')
if choice4=='1':
    print('Gameover!')
elif choice4=='2':
    print('help! you win')
else:
    print('Gameover!')