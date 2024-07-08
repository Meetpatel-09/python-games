words = [
    {'c', 'o', 'm', 'p', 'u', 't', 'e', 'r'},
    {'m', 'o', 'n', 'i', 't', 'o', 'r'},
    {'k', 'e', 'y', 'b', 'o', 'a', 'r', 'd'},
    {'m', 'o', 'u', 's', 'e'}
]

correctWords = [
    "computer",
    "monitor",
    "keyboard",
    "mouse"
]

maxPlayers = 5
playerNames = []
scores = [0, 0, 0, 0, 0]
noOfPlayers = 0

noOfPlayers = int(input("Enter Number of players: "))

if noOfPlayers > maxPlayers or noOfPlayers <= 0:
    print("No more than 5 or less than 0 players..")
else:
    for index in range(noOfPlayers):
        playerCounter = index + 1
        message = "Enter Player " + str(playerCounter) + " name: "
        name = input(
            "Enter Player " + str(playerCounter) + " name: ")
        playerNames.append(name)

    for index in range(noOfPlayers):
        counter = 0
        print(playerNames)
        print("\n\n\nIt is " + str(playerNames[counter]) + "'s turn")

        for word in words:
            print("Rewirte the correct spelling of: ")
            for char in word:
                print(char, end="")
            answer = input("\nAnswer: ")
            if answer == correctWords[counter]:
                print("Correct Answer!!!")
                scores[counter] += 1
            else:
                print("Incorrect Answer!!!")
                print("Correct Answer Is: " + correctWords[counter])

        counter += 1
    else:
        for index in range(noOfPlayers):
            print("Name:", playerNames[index], "Score:", scores[index])
