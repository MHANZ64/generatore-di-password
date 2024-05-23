import random
elementi = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
int(input("inserire la lunghezza"))
password_generata = ""

for i in range(lunghezza):
    
    carattere_casuale = random.choice(elementi)
    password_generata += carattere_casuale
    print("password_autogenerata")