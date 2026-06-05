import run
import progress

game_runs = True




### Game Start

while game_runs:
    
    print("\nWelcome to Rogue Terminal! A turn-based dungeon crawler rougelite.\n")
    while True:
        menu_choice = input("\nEnter 's' to start a new run, 'u' to access the upgrade menu, or 'e' to exit the game: ")
        
        match menu_choice:
            case "s":
                run.start_run()
            case "u":
                progress.upgrade_menu()
            case "e":
                validation = input("\nDo you really want to quit? Press Y/n: ")
                if validation   == "y":
                    exit()
                else:
                    pass
            case _:
                print("Invalid Option, please try again.")
