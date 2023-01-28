playing = True
while playing:
    player = int(input("Your Hands Total: "))
    dealer = int(input("Dealers Face Up: "))
    if player == 21:
        print("Blackjack, You Win")
        break
