import random

#generate a random number from 1-80 and return it
def generate_random():
    return random.randint(0,81)


#receive an empty game list and call generate_random until 20 numbers are called, discard any copies
def game_list_drawings(gamelist):
    while len(gamelist)<20:
        r=generate_random()
        while (r in gamelist):
            r=generate_random()
        gamelist.append(r)
    return gamelist

def sort_ascending(a_list):  #func to sort a list in ascending order
    a_list.sort()
    return a_list


boo = []
game_list_drawings(boo)
sort_ascending(boo)
print (boo)