import random

#generate a random number from 1 to x; default is 80 for keno draws
def generate_random(x=81):
    return random.randint(1,80)


#receive an empty list and generate 20(default) or x number of unique randoms
def random_drawings(randolist, x=20):
    while len(randolist)<x:
        r=generate_random()
        while (r in randolist):
            r=generate_random()
        randolist.append(r)
    return randolist

def sort_ascending(a_list):  #func to sort a list in ascending order
    a_list.sort()
    return a_list

def matching(game_list, player_list, match_list): # return a list with matching numbers
    for p in player_list:
        if p in game_list:
            match_list.append(p)
    return match_list
   


boo = [] #game list
player = [] #player list
match = [] #match list
player_quick_pick = True
number_of_spots = 10
random_drawings(boo) #get game drawings list
sort_ascending(boo)  #sort game drawings
random_drawings(player, number_of_spots)
sort_ascending(player)
matching(boo, player, match)
print (boo)
print (player)
print (match)