import time

print("Welcome to Tic-Tac-Toe game, are you excited to be here?")

while True:
    time.sleep(1)
    print('\nReady?')
    print('1. New game')
    print('2. Game history')
    print('3. Player record')
    print('4. Exit')

    time.sleep(1)
    user_input = int(input('\nChoose a number: '))

    Instructions = ['\n The game is played on a grid that is 3 squares by 3 squares. You are X, your friend is O. Players take turns putting their marks in empty squares.The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.When all 9 squares are full, the game is over.']

    sign_dictionary = []
    for i in range(9):
        sign_dictionary.append(' ')

    def print_board():
        board = f""" 
        {sign_dictionary[0]} | {sign_dictionary[1]} | {sign_dictionary[2]}
        ---------
        {sign_dictionary[3]} | {sign_dictionary[4]} | {sign_dictionary[5]}
        ---------
        {sign_dictionary[6]} | {sign_dictionary[7]} |{sign_dictionary[8]} """

        print(board)  
    index_list = []
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
    def calculate_result(player_one, player_two):
        if sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'X' or sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'X' or sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'X' or sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'X' or sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'X' or sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'X' or sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'X' or sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'X' :
            print(f"Congratulations {player_one}. You won!")
            quit("Thank you both for playing")
        elif sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'O' or sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'O' or sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'O' or sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'O' or sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'O' or sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'O' or sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'O' or sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'O' :
            print(f"Congatulations{player_two}. You won")
            quit("Thank you both for playing")
        
    
    def main():
        # while True: 
        print("Welcome to Tic-Tac-Toe game")
        player_one = input("Enter player one name: ")
        player_two = input("Enter player two name: ")

        score_board = {player_one: 0, player_two: 0} 


        # To Design the Scoreboard
        # To create a scoreboard to capture the scores made during the game and display this when the game ends.
        def my_scoreboard(score_board):  
            print("\t--------------------------------")  
            print("\tThe SCOREBOARD for TIC TAC TOE GAME       ")  
            print("\t--------------------------------")  
        
            list_of_the_two_players = list(score_board.keys())  
            print("\t   ", list_of_the_two_players[0], "\t    ", score_board[list_of_the_two_players[0]])  
            print("\t   ", list_of_the_two_players[1], "\t    ", score_board[list_of_the_two_players[1]])  
        
            print("\t--------------------------------\n") 
        my_scoreboard(score_board)
        # 
        # character_count = 0
        # alphabet_count = 0
        # special_char = '[_-]'
        # alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # for i in range(len(player_one)):
        #     if player_one[i] in special_char
        #         character_count += 1
        #     if player_one[i] in special_char:
        #         alphabet_count += 1


        #if player_one.isalpha >
        print(f"Thank you for joining {player_one} and {player_two}")

        print(f"{player_one} sign will be - X")
        print(f"{player_two} sign will be - O")
        # while True:
        start_game = input('\nEnter 1 to START GAME: ')
        if start_game != "1":
            time.sleep(1)
            print('You need to enter 1 to start game')
        
            print_board()

            for i in range(9):
                if i % 2 == 0:
                    index = take_input(player_one)
                    sign_dictionary[index] = 'X'
                else:
                    index = take_input(player_two)
                    sign_dictionary[index] = 'O'
                print_board()
                calculate_result(player_one, player_two)
            print("This is a TIE, nobody won. Play again?")
    main()
