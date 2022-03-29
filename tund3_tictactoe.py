board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
symbols = {"0":"X", "1":"O"}

def print_board():
    fullrida = ""
    for rida in board:
        for slot in rida:
            fullrida += slot + " "
        print(fullrida + "\n")
        fullrida = ""

def player_input(player):
    number = int(input("Sisesta ruudu nr: "))
    if number > 9:
        print("mida viiulit")
        exit()

    rida = (number-1) // 3
    indeks = (number-1) - (rida*3)





board[rida][indeks] = "X"

