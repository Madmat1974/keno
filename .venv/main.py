from kenofuncs import random_drawings
from kenofuncs import sort_ascending
from kenofuncs import matching
from kenofuncs import draw_win
from tkinter import *
import tkinter as tk



    
def main():
    games = 0
    root = tk.Tk()
    root.title("Radio Button Example")

    selected_option = tk.IntVar()
    games_text = tk.Label(root, text="Please choose number of consecutive draws:")
    games_text.grid(row=0, column=0, columnspan=7, pady=10)

# Create a list to store the radio button widgets
    radio_buttons = []

# Create a list of labels and corresponding values for the radio buttons
    radio_button_data = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("10", "10"),
    ("20", "20")
]

    def games_selected():
        nonlocal games
        games = selected_option.get()
        """
        This function is called when a radio button is selected.
        It disables all radio buttons after a selection has been made.
        """
        print(f"Selected value: {selected_option.get()}") # Optional: for testing
        for rb in radio_buttons: # Iterate through the stored radio button widgets
            rb.config(state=tk.DISABLED)  # Disable each radio button


# Create and position the seven radio buttons using grid
    for i, (text, value) in enumerate(radio_button_data):
        radio_button = tk.Radiobutton(
            root,
            text=text,
            variable=selected_option,
            value=value,
            command=games_selected  # Call the function when a radio button is clicked
        )
        radio_button.grid(row=1, column=i, padx=5, pady=5)  # Adjust row/column as needed
        radio_buttons.append(radio_button)  # Add the radio button to the list

    start_button = tk.Button(root, text= "START", command=lambda: normal_mkeno(games))
    start_button.grid(row=2,column=0, columnspan=7, pady=10)

    
    root.mainloop()

def normal_mkeno(games):
    #games = 10
    count_games = 0
    number_of_spots = 10
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