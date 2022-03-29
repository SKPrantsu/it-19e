print("Game started")
print("1 2 3")
print("4 5 6")
print("7 8 9")
 
player1 = input("P1, sisesta player1 nr: ")
print(player1)
if player1 == "1":
    print("X 2 3")
    print("4 5 6")
    print("7 8 9")
    player2 = input("P2, sisesta ruudu nr: ")

    if player2 == "1":
        print("Ei saa kaiku teha")
 
    if player2 == "2":
        print("X O 3")
        print("4 5 6")
        print("7 8 9")
 
    if player2 == "3":
        print("X 2 O")
        print("4 5 6")
        print("7 8 9")
    
    if player2 == "4":
        print("X 2 3")
        print("O 5 6")
        print("7 8 9")

if player1 == "2":
    print("1 X 3")
    print("4 5 6")
    print("7 8 9")
    player2 = input("P2, sisesta ruudu nr: ")

    if player2 == "1":
        print("O X 3")
        print("4 5 6")
        print("7 8 9")
 
    if player2 == "2":
        print("Ei saa kaiku teha")
 
    if player2 == "3":
        print("1 X O")
        print("4 5 6")
        print("7 8 9")
    
    if player2 == "4":
        print("1 X 3")
        print("O 5 6")
        print("7 8 9")

if player1 == "3":
    print("1 2 X")
    print("4 5 6")
    print("7 8 9")
    player2 = input("P2, sisesta ruudu nr: ")

    if player2 == "1":
        print("O 2 X")
        print("4 5 6")
        print("7 8 9")

    if player2 == "2":
        print("1 O X")
        print("4 5 6")
        print("7 8 9")
 
    if player2 == "3":
        print("Ei saa kaiku teha")
    
    if player2 == "4":
        print("1 2 X")
        print("O 5 6")
        print("7 8 9")