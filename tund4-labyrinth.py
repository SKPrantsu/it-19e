import random

map = [
[12, 0, 1, 0, 0], 
[1, 0, 1, 0, 0], 
[1, 0, 0, 1, 0], 
[1, 1, 0, 1, 1], 
[24, 0, 0, 1, 0]]

vaba_tee = 0
sein = 1
lopp = 24

start_x = 0
start_y = 0

def saab_liikuda_paremale(map, praegused_koordinaadid):
    parempool = praegused_koordinaadid[0] + 1
    praegune_rida = praegused_koordinaadid[1]

    if parempool >= len(map[praegune_rida]):
        return False
    if (map[praegune_rida][parempool] == vaba_tee):
        return True
    if (map[praegune_rida][parempool] == lopp):
        return True
    return False

def saab_liikuda_vasakule(map, praegused_koordinaadid):
    vasakpool = praegused_koordinaadid[0] - 1
    praegune_rida = praegused_koordinaadid[1]

    if vasakpool < 0:
        return False
    if (map[praegune_rida][vasakpool] == vaba_tee):
        return True
    if (map[praegune_rida][vasakpool] == lopp):
        return True
    return False

def saab_liikuda_ules(map, praegused_koordinaadid):
    ulespool = praegused_koordinaadid[1] - 1
    praegune_x = praegused_koordinaadid[0]

    if ulespool < 0:
        return False
    if (map[ulespool][praegune_x] == vaba_tee):
        return True
    if (map[ulespool][praegune_x] == lopp):
        return True
    return False

def saab_liikuda_alla(map, praegused_koordinaadid):
    allpool = praegused_koordinaadid[1] + 1
    praegune_x = praegused_koordinaadid[0]

    if allpool >= len(map):
        return False
    if (map[allpool][praegune_x] == vaba_tee):
        return True
    if (map[allpool][praegune_x] == lopp):
        return True
    return False

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

#print("Saab liikuda paremale: " + str(saab_liikuda_paremale(map, [start_x, start_y])))
#print("Saab liikuda vasakule: " + str(saab_liikuda_vasakule(map, [start_x, start_y])))
#print("Saab liikuda ulesse: " + str(saab_liikuda_ules(map, [start_x, start_y])))
#print("Saab liikuda alla: " + str(saab_liikuda_alla(map, [start_x, start_y])))
#print()
#print("Saab liikuda paremale: " + str(saab_liikuda_paremale(map, [1, 1])))
#print("Saab liikuda vasakule: " + str(saab_liikuda_vasakule(map, [1, 1])))
#print("Saab liikuda ulesse: " + str(saab_liikuda_ules(map, [1, 1])))
#print("Saab liikuda alla: " + str(saab_liikuda_alla(map, [1, 1])))
#print()

liikumistee = []
while map[start_y][start_x] != 24:
    liikumistee.append([start_x, start_y])
    valikud = []
    if saab_liikuda_paremale(map, [start_x, start_y]):
        valikud.append('parem')
    if saab_liikuda_vasakule(map, [start_x, start_y]):
        valikud.append('vasak')
    if saab_liikuda_ules(map, [start_x, start_y]):
        valikud.append('ules')
    if saab_liikuda_alla(map, [start_x, start_y]):
        valikud.append('alla')

    suvaline = random.choice(valikud)
    if suvaline == 'parem':
        start_x += 1
    elif suvaline == 'vasak':
        start_x -= 1
    elif suvaline == 'ules':
        start_y -= 1
    elif suvaline == 'alla':
        start_y += 1

    
    

    
    
print(liikumistee)