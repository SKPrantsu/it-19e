map = [
[12, 0, 1, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 0, 0, 24]]

vaba_tee = 0
sein = 1

start_x = 0
start_y = 0

def saab_liikuda_paremale(map, praegused_koordinaadid):
    parempool = praegused_koordinaadid[0] + 1
    praegune_rida = praegused_koordinaadid[1]
    if (map[praegune_rida][parempool] == vaba_tee):
        return True
    else:
        return False

print(saab_liikuda_paremale(map, [start_x, start_y]))
print(saab_liikuda_paremale(map, [1, 1]))

def print_map():
    for rida in map:
        taisrida = ""
        #print("---------------")
        for element in rida:
            taisrida += str(element) + " "
        print(taisrida)

def print_map2():
    for x in map:
        print(x)

print_map2()