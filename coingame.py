player1Name = ""
player2Name = ""

alfaGameCoins = 16

playerTurn = 1

player1Name = input("Enter  Player 1 Name: ")
player2Name = input("Enter  Player 2 Name: ")

while alfaGameCoins > 0:
    print("\nThere are ", alfaGameCoins, " in left in the game.")
    print("Available options: 1 coin, 2 coins, 3 coins: ")
    if playerTurn == 1:
        print(player1Name + "'s Trun")
        coin = int(input("Enter Coins: "))

        if coin == 1 or coin == 2 or coin == 3:
            if coin < alfaGameCoins:
                alfaGameCoins -= coin
            elif coin == alfaGameCoins:
                alfaGameCoins -= coin
                print(player1Name + " Win!!!")
        playerTurn = 2

    else:
        print(player2Name + "'s Trun")
        coin = int(input("Enter Coins: "))

        if coin == 1 or coin == 2 or coin == 3:
            if coin < alfaGameCoins:
                alfaGameCoins -= coin
            elif coin == alfaGameCoins:
                alfaGameCoins -= coin
                print(player2Name + " Win!!!")

        playerTurn = 1
