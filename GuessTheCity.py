import random


def game():
    city_list = ["ahmedabad", "surat", "vadodara", "rajkot", "bhavnagar", "gandhinagar", ]
    score = 0

    while city_list:
        city = random.choice(city_list).lower()
        city_list.remove(city)
        guess_list = []
        attempt = 7

        print("\n\n~=~=~=~=~=~=~> Welcome to 'Guess the City' Game...! <~=~=~=~=~=~=~")

        print(f"\nThe City has {len(city)} letter.")
        print(showWord(city, guess_list))

        while attempt > 0:
            guess = input("\nGuess the Letter or Full City Name : ").lower()

            if len(guess) == 1:
                if guess in guess_list:
                    print(f"\nYou Already Guessed the Letter '{guess}'.")
                else:
                    guess_list.append(guess)
                    if guess in city:
                        print(f"\nGood Job...! The Letter '{guess}' is in the City Word.")
                    else:
                        print(f"\nSorry, '{guess}' is NOT in the City Word.")
                attempt -= 1
                print(f"Attempt Left : {attempt}\n")

            elif len(guess) == len(city):
                if guess == city:
                    score += 5
                    print(f"Good...! You Guessed the City Correctly - '{city}'. \nNow Your Score is {score}")
                    break
                else:
                    attempt -= 1
                    print(f"\nSorry, '{guess}' is NOT in the City Word. \nAttempt Left : {attempt}")

            else:
                print("Invalid Input. Please Guess a Single Letter or Full City Name.")

            word = showWord(city, guess_list)
            print(word)

            if '_' not in word:
                score += 5
                print(f"Good...! You Guessed the City Correctly - '{city}'. \nNow Your Score is {score}")
                break

        if attempt == 0:
            print(f"Game Over...! The city was '{city}'.", sep="")


def showWord(word, guess_letter):
    show_word = ''
    for letter in word:
        if letter in guess_letter:
            show_word += letter
        else:
            show_word += ' _ '
    return show_word


game()