map = [
[12, 0, 1, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 0, 0, 24]]

start_x = 0
start_y = 0

def print_map():
    for rida in map:
        taisrida = ""
        #print("---------------")
        for element in rida:
            taisrida += str(element) + " "
        print(taisrida)

print_map()