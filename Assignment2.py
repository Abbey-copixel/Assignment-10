from random import randint
#list generation
list_numbers = list()
for i in range(0,10):
    list_numbers.append(randint(1,10))
while True:
    guess = input("Please enter a number:\t or\t Type \"q\" to quit:\t")
    if guess == "q":
        break
    else:
        try:
            guess = int(guess)
            if guess in list_numbers:
                print("Congratulations! You have guessed the number!")
            else:
                print("Please try again!")
        except:
            print("Please type a number!")
    
