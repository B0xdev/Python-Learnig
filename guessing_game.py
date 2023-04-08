secret_number = 27 ####Change this number for a diffferent secret numbe####
guess_count = 0
guess_limit = 3 ####Change this nyumber for the amount of guesses you get####
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
####The code below is to make you win####
    if guess == secret_number:
        print("You Won")
        break
####The code below is to know if you got it wrong####
    if guess == guess_count == 1 or 2:
        print("Wrong number")
####The code below is to know if you lost####
if guess == guess_limit:
    print("You Lost! :(")