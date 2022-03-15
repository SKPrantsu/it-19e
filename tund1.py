def plus(a, b):
    return a + b
 
def minus(a, b):
    return a - b
 
print("Kas tahad liita või lahutada?") # print functions with string argument
tehe = input("Palun sisesesta + või -") # - või +
muutuja1 = int(input("Sisesta nr1: ")) # type cast from string input to int
muutuja2 = int(input("Sisesta nr2: "))

if tehe == "+":
    tulemus = plus(muutuja1, muutuja2) # function call / execution
 
if tehe == "-":
    tulemus = minus(muutuja1, muutuja2) # function call / execution
 
print(tulemus)