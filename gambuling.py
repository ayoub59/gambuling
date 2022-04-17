
# the steps for making the algo
import random
import time
# the greatings
def intro_banner():
    s = "Welcome to the Game!"
    print(s)
def game_over():
    s = "Game Over. Bye!"
    print(s)

# main function
def main():
    intro_banner()
    playername = input('Player Name >> ')
    money = 100
    print("Welcome to the game, " + playername + ". Your starting amount is " + str(money) + ' DH.')
    time.sleep(0.5)


    keepplaying = True
    # validate the bet
    while keepplaying:
        # place the bet
        bet = input("how much are you willing to bet >> ")
        time.sleep(0.5)

        isbetnotvalid = int(bet) > money or int(bet) < -1
        while isbetnotvalid:
            print("Please enter a valid bet.")
            time.sleep(0.5)
            bet = input("Place fix your bet >> ")
            time.sleep(0.5)
            isbetnotvalid = int(bet) > money or int(bet) < -1
        bet = int(bet)
        # getting the player_number and confugiring it
        player_number = input("ok, now what is your bet >> ")
        time.sleep(0.5)
        player_number = int(player_number)
        # validating the player's bet
        if player_number > 9:
            print("that's too hight, bet another number")
            player_number = input("ok, now what is your bet >>")
            time.sleep(0.5)

        elif player_number < 1:
            print("that's too low, bet another number")
            player_number = input("ok, now what is your bet >> ")
            time.sleep(0.5)

        else:
            print("good luck bozo")
            time.sleep(0.5)

        # the magic_number
        magic_number = random.randint(0, 9)
        
        print("Your card is " + str(player_number) + ". the random card is " + str(magic_number) + ".")
        time.sleep(0.5)


        if player_number == magic_number:
            # if you hit
            print("Damn you won!!, you are so lucky.")
            time.sleep(0.5)

            money = money + bet * 2
            print("you have " + str(bet) + " DH!")
            time.sleep(0.5)

        # it you mise
        else:
            print("pc wins! You lose " + str(bet) + " DH!")
            time.sleep(0.5)

            money = money - bet
        if money < 0:
            print("brock, You're out of money!")
            time.sleep(0.5)

            game_over()
            keepplaying = False
        else: 
            print("Your money is now " + str(money) + " DH.")
            time.sleep(0.5)

            ask = input("Do you want to keep playing? [y/N] >> ")
            time.sleep(0.5)

            if ask == 'y' or ask == 'Y':
                keepplaying = True
            else:
                print("You're leaving with " + str(money) + " DH. comme again, Bye.")
                time.sleep(0.5)

                game_over()
                keepplaying = False
main()