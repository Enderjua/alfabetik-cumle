import time
import random

sentence = input("Cümleyi gir bro: ")

alfabe = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
screen = ""
i=0

while screen!=sentence:
    x=random.randint(0,52)
    if(alfabe[x]==sentence[i]):
        screen+=sentence[i]
        i+=1
        print(screen)
    else:
        time.sleep(0.01)
        print(screen+alfabe[x])
