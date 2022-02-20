n = 4


def winnerSquareGame(n):
    # print((n ** (1 / 2)), int(n ** (1 / 2)))
    if (n ** (1 / 2)) == int(n ** (1 / 2)):
        print(True)
    else:
        winnerSquareGame()
