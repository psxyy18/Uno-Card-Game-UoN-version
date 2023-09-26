
def set_curr_player(uno, default):
    
    if uno.current[0] == 'Reverse' and uno.special_check == 0:
        uno.direction_check *= -1 
        uno.special_check = 1 
    if uno.current[0] == 'Skip' and uno.special_check == 0:
        uno.special_check = 1
        uno.position = (uno.position + uno.direction_check) % 4

    if default:
        uno.position = (uno.position + uno.direction_check) % 4


def re_initialize(uno):
    #reinitialize constructors
    uno.message = "" 
    uno.winner = -1
    uno.player_playing = False
    uno.play_lag = -1
    uno.player_list = [[], [], [], []]
    uno.deck1 = list()
    uno.deck2 = list()
    uno.direction_check = 1  
    uno.position = -1 
    uno.special_check = 0  
    uno.current = tuple()
    uno.drawn, uno.played, uno.choose_color = False, False, False
    uno.uno = [True] * 4
    uno.easy = True