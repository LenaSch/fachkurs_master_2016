from random import randint


def guess_a_number():
    """Game to guess a number the computer randomly generated."""

    # TODO:
    # generate a random number (uniformly distributed between 0 and 100)
    number=randint(0,100)
    guessednumber=-1
    while guessednumber!=number:
        # read input from the user and validate that the input is numeric (use the function check_raw)
        test=False
        while test==False:
            guessednumber=input("guess a number between 0 and 100: ")
            try:
                guessednumber=int(guessednumber)
                test=True
            except ValueError:
                print('please enter integer value between 0 and 100')        
        # check whether the number was guessed 
        if number == guessednumber:
            print('correct number')
        # implement the functions evaluate_my_number, which checks whether the number is too high or too low
        if number < guessednumber:
            print('guessed number too high, guess again')
        if number > guessednumber:
            print('guessed number too low, guess again')
    return guessednumber
        # and print this information to the user
    # let the computer guess, therefore implement the demo_a_number function
    


def check_raw(guessednumber):
    """Gets the string, raw_input should print, checks and returns the input."""
  
    

def evaluate_my_number(guess, random_number):
    """Is the guess to high or to low? Guess again!"""


def demo_a_number():
    """The computer tries to guess the number"""
    number=randint(0,100)
    print(number)
    guessednumber=randint(0,100)  
    i = 0
    while guessednumber!=number:
        # read input from the user and validate that the input is numeric (use the function check_raw)
        i = i+1 
        print(guessednumber)
        # check whether the number was guessed 
        # implement the functions evaluate_my_number, which checks whether the number is too high or too low
        if number < guessednumber:
            print('too high')
            new_guess = randint(0,guessednumber)
        elif number > guessednumber:
            print('too low')
            new_guess = randint(guessednumber,100)
        guessednumber = new_guess
    if number == guessednumber:
        print('Anzahl: %i' % (i))
        print('richtige Zahl: %i' % (guessednumber))
        
    return guessednumber

    
#guessednumber=guess_a_number()
demo_a_number()

