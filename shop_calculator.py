# A python program which will keep adding a stream of numbers ibputed by the user. The adding stops as soon as user presses q key on the keyboard

sum = 0
while(True):
    userInput = input("Enter the price or press q to quit: \n")
    if (userInput != 'q'):
        sum += int(userInput)
        print(f"Order total so far:{sum}")
    else:
        print(f"Your Bill total is {sum} . Thanks for shopping with us")
        break
