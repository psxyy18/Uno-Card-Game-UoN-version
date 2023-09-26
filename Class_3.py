#import pygame



class commen(object):
    def __init__(self):
        self.player_list = [[], [], [], []]  
        self.draw_deck = list()
        self.discard_deck = list()
        self.direction_check = 1 
        self.position = -1 
        self.current_card = list()  
        self.discard_list = False

        self.drawn = False 
        self.played = False
        self.choose_card_color = False
        self.player_playing = False
        self.winner = -1
        self.play_card_lag = -1
        self.play_card_mode = ""

        self.played_check = 0  
        self.fundation_check = 0  
        self.uno = [True] * 4  
        self.message = "DEALING THE CARDS"  
        self.level1 = True  
        self.bot_map = {1: "ROBINHOOD", 2: "PRINCE JOHN", 3: "MAID MARIAN"}  
        self.color = ['Blue', 'Red', 'Green', 'Yellow']  
