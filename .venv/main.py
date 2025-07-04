from kenofuncs import random_drawings
from kenofuncs import sort_ascending
from kenofuncs import matching



def main():

 
    player_quick_pick = True
    number_of_spots = 10
    games = 10
    count_games = 0
    draw_until_win = False
    
        

    while (count_games < games): 
        boo = [] #game list
        player = [] #player list
        match = [] #match list
        count_games += 1
        random_drawings(boo) #get game drawings list
        sort_ascending(boo)  #sort game drawings
        random_drawings(player, number_of_spots)
        sort_ascending(player)
        matching(boo, player, match)
        print (boo)
        print (player)
        print (match)
        print(f"Player matched {len(match)} numbers out of {len(player)} picked number/s after {count_games} game/s")



if __name__ == "__main__":
    main()