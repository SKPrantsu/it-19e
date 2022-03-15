"""
numbrid = [1, 2, 3, 4, 5, -3, 34, 6, 7, 8, 69, 9, 10]
max = numbrid[0]
min = numbrid[0]

for x in numbrid:
    if x > max:
        max = x

print("Koige suurem number: " + str(max))

for x in numbrid:
    if x < min:
        min = x

print("Koige vaiksem number: " + str(min))
"""


""" 
numbrid = []

for x in range(0, 10):
    numbrid.append(int(input("Number " + str(x+1) + ": ")))

for x in numbrid:
    print(x)
"""


vanused = []

mitu_vanust = int(input("Mitu vanust tahad sisestada?: "))

for x in range(0, mitu_vanust):
    vanused.append(int(input("Vanus nr " + str(x+1) + ": ")))

vanuste_summa = 0
for x in vanused:
    vanuste_summa += x

keskmine = vanuste_summa / mitu_vanust

print("Vanuste keskmine on: " + str(keskmine))