secret_number=15
print("i am thinking of a number between 1 and 20. ")
print("van you guess what is it ?")
guess=0
while secret_number!=guess:
    guess=int(input("enter your guess: "))
    if guess==secret_number:
        print("congratulation! your guess is absolutely right.")
    elif(guess<secret_number):
        print("too small ! try a lerger num")

    else:
        print("too big try a smaller number")   


