import time
#calculate the when a player wins, looses, or a tie
#main function
time.sleep(1)
print('\nReady?')
print('1. New game')
print('2. Game history')
print('3. Player record')
print('4. Exit')

time.sleep(1)
user_input = int(input('\nChoose a number: '))

if user_input == 1:
new_game()
elif user_input == 2:
game_history()
elif user_input == 3:
player_record()


    def NewGame():
    #get our players for the game
    players = ReturnPlayersDetails()

    # print out scoreboard
    my_scoreboard(score_board)

    print(f"Thank you for joining {player_one} and {player_two}")
    print(f"{player_one} sign will be - X")
    print(f"{player_two} sign will be - O")

    # get our signed dictionaries
    sign_dictionary = []
    for i in range(9):
    sign_dictionary.append(' ')

    # print the details of the signed dictionary
    print_board(sign_dictionary)

    for i in range(9):
    if i % 2 == 0:
    index = take_input(players.p1)
    sign_dictionary[index] = 'X'
    else:
    index = take_input(players.p2)
    sign_dictionary[index] = 'O'

    calculate_result(players.p1, players.p2)


    # note 
    # this function should return the player object
    # eg players = {player_one: 0, player_two: 0}
    def ReturnPlayersDetails(): players
    player_one = input("Enter player one name: ")
    player_two = input("Enter player two name: ")

    ValidatePlayerName(player_one)
    ValidatePlyaerName(player_two)

    #create and return a players object
    players = {p1: player_one, p2: player_two}
    return players

    def ValidatePlayerName(player_name):
    while True:
    #add logic to validate player usernames here
    #username is between 3 - 12 characters
    if len(player_name) < 3 or > 12:
    return False

    #sample code for first character in string to match a particular standard
    arr = list(player_name)
    special_char = ['&', '#', '$', '!', '?', '"', '(', ')', '.']

    # get the first character using the array index
    first_char = arr[0]

    #here we will write our validation to check that the first letter of
    #name is not a numnber
    if first_char.isnumeric():
    return False
    min_length = 9
    def user_password():
    password = input("Enter password: ")
    character_count = 0
    alphabet_count = 0

    for i in range(len(password)):
    #check if any special character or alphabet is present in a given string or not
    if password[i] in special_characters:
    character_count += 1
    if password[i] in alphabetic_characters:
    alphabet_count += 1
    if character_count > 3 or alphabet_count > 5:
    print("Validation failed")
    elif (len(password) < 9 or len(password) > 12):
    print("Validation failed")
    else:
    print("Created password successfully")
    user_password()

    #lets leverage on regular expression to validate the special char thing
    #make sure you import regex 
    #import re
    #NOTE we still need to figure out the regex for this validation
    #(bool(re.search(`/[^abc]+/g`, first_char)))


    #this function should return the sign dictionary after printing 
    def print_board(sign_dictionary)

    board = f""" 
    {sign_dictionary[0]} | {sign_dictionary[1]} | {sign_dictionary[2]}
    ---------
    {sign_dictionary[3]} | {sign_dictionary[4]} | {sign_dictionary[5]}
    ---------
    {sign_dictionary[6]} | {sign_dictionary[7]} |{sign_dictionary[8]} """

    print(board)

    def take_input(player_name):
        while True:
            x = int(input(f"{player_name}: "))
            x -= 1
            if 0 <= x < 10:
                if x in index_list:
                print("This spot is blocked")
                continue
            index_list.append(x)
            return x
            print("Please enter a number between 1-9")


    #calculates the final score for the players
    def calculate_result(player_one, player_two):
    if sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'X' or sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'X' or sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'X' or sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'X' or sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'X' or sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'X' or sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'X' or sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'X' :
    print(f"Congratulations {player_one}. You won!")
    quit("Thank you both for playing")
    elif sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'O' or sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'O' or sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'O' or sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'O' or sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'O' or sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'O' or sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'O' or sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'O' :
    print(f"Congatulations{player_two}. You won")
    quit("Thank you both for playing")
    else {
    print("This is a TIE, nobody won. Play again?")
    }
