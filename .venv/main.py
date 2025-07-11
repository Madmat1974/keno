from kenofuncs import random_drawings
from kenofuncs import sort_ascending
from kenofuncs import matching
from kenofuncs import draw_win
import tkinter as tk



    
def main():
    games = 0
    number_of_spots = 0
    root = tk.Tk()
    root['bg'] = 'lightblue'
    root.title("Mkeno")

    # Tkinter variables to hold the selected values for each group
    selected_option = tk.IntVar()
    spot_option = tk.IntVar()

    # Label for the first group of radio buttons
    games_text = tk.Label(root,bg='light blue', text="Please choose number of consecutive draws:")
    games_text.grid(row=0, column=0, columnspan=5, pady=9)

    # Create a list to store the radio button widgets for the first group
    games_radio_buttons = []

    # Data for the first group of radio buttons
    radio_button_data = [
        ("1", 1), 
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("10", 10),
        ("20", 20)
    ]

    def games_selected():
        nonlocal games
        games = selected_option.get()
        print(f"Selected number of games: {games}")
        # Disable all radio buttons in the first group after a selection is made
        for rb in games_radio_buttons:
            rb.config(state=tk.DISABLED)

    # Create and position the seven radio buttons for the first group
    for i, (text, value) in enumerate(radio_button_data):
        radio_button = tk.Radiobutton(
            root,
            text=text,
            variable=selected_option,
            value=value,
            bg = 'light blue',
            command=games_selected
        )
        radio_button.grid(row=1, column=i, padx=5, pady=5)
        games_radio_buttons.append(radio_button)

    # Label for the second group of radio buttons
    spots_text = tk.Label(root, bg = 'light blue', text="Please choose number of spots:")
    spots_text.grid(row=2, column=0, columnspan=4, pady=8)

    # Create a list to store the radio button widgets for the second group
    spot_radio_buttons = []

    # Data for the second group of radio buttons
    spot_button_data = [
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ("9", 9),
        ("10", 10)
    ]

    def on_checkbox_click(checkbox_number, var):
        nonlocal selected_checkbox_numbers

        if var.get:
            if len(selected_checkbox_numbers) < number_of_spots:
                selected_checkbox_numbers.append(checkbox_number)
            else:
                var.set(False) #unchecks the box if the spot limit reached
        else:
            if checkbox_number in selected_checkbox_numbers:
                selected_checkbox_numbers.remove(checkbox_number)

    def enable_checkboxes():
        # Enable checkboxes once a spot is selected
        for cb in checkboxes_widgets:
            cb.config(state=tk.NORMAL)

    def spot_selected():
        nonlocal number_of_spots
        number_of_spots = spot_option.get()
        print(f"Selected number of spots: {number_of_spots}")
        # Disable all radio buttons in the second group after a selection is made
        for rb in spot_radio_buttons:
            rb.config(state=tk.DISABLED)
        enable_checkboxes() #enable checkboxes

    # Create and position the ten radio buttons for the second group
    for i, (text, value) in enumerate(spot_button_data):
        radio_button = tk.Radiobutton(
            root,
            text=text,
            variable=spot_option,
            value=value,
            bg = 'light blue',
            command=spot_selected
        )
        radio_button.grid(row=3, column=i, padx=5, pady=5)
        spot_radio_buttons.append(radio_button)

    #Checkboxes Section
    checkboxes_label = tk.Label(root,bg='light blue', text="Select the spotted numbers:")
    checkboxes_label.grid(row=4, column=0, columnspan=4, pady=10)

    checkbox_vars = [] #store booleanvariable for each checkbox
    checkboxes_widgets = [] #store checkbutton widgetsthingsmathings
    selected_checkbox_numbers = [] #list of player numbers

    num_checkboxes = 80
    checkboxes_per_row = 10
    starting_row = 5

    for i in range(num_checkboxes):
        row=starting_row + (i // checkboxes_per_row)
        column = i % checkboxes_per_row
        checkbox_number = i + 1

        var = tk.BooleanVar() #var for each checkbox
        checkbox_vars.append(var)

        cb = tk.Checkbutton(
            root,
            text = f"{checkbox_number}",
            bg = 'light blue',
            variable=var,
            onvalue=True,
            offvalue=False,
            state=tk.DISABLED, #disabled until spot chosen
            command=lambda num=checkbox_number, v=var: on_checkbox_click(num,v)
        )
        cb.grid(row=row, column=column, padx=2, pady=2, sticky="w")
        checkboxes_widgets.append(cb)

    

    start_button = tk.Button(root, text= "START", command=lambda: normal_mkeno(games, selected_checkbox_numbers, results_text))
    start_button.grid(row=15,column=1, columnspan=10, pady=5)

    results_text = tk.StringVar()
    results_text.set("Results will be shown here..")

    results_label = tk.Label(root,bg='light blue', textvariable=results_text, wraplength=600, justify="left", font=("Arial", 8))
    results_label.grid(row=starting_row + (num_checkboxes // checkboxes_per_row) + 3, column=0, columnspan=8, pady=10)

    root.mainloop()

def normal_mkeno(games, player, results_string_var):
    #games = 10
    count_games = 0
    result_message= f"{games} game/s starting with your chosen numbers\n Your numbers: {player}\n\n"
    results_string_var.set(result_message)
    
    while (count_games < games): 
        boo = [] #game list
        #player = [] #player list
        match = [] #match list
        count_games += 1
        random_drawings(boo) #get game drawings list
        sort_ascending(boo)  #sort game drawings
        #random_drawings(player, number_of_spots)
        sort_ascending(player)
        matching(boo, player, match)
        print (boo)
        print (player)
        print (match)
        print(f"Player matched {len(match)} numbers out of {len(player)} picked number/s after {count_games} game/s")
        result_message+=(f"GAME DRAW: {boo}\nMatches: {match}\n\n")
        results_string_var.set(result_message)


if __name__ == "__main__":
    main()