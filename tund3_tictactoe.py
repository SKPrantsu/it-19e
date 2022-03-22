board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
number = int(input("Sisesta ruudu nr: "))
if number > 9:
    print("mida viiulit")
    exit()

rida = (number-1) // 3
indeks = (number-1) - (rida*3)
board[rida][indeks] = "X"

fullrida = ""
for rida in board:
    for slot in rida:
        fullrida += slot + " "
    print(fullrida + "\n")
    fullrida = ""