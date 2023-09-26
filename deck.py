#got some thoughts and structures from https://www.youtube.com/watch?v=7BXDcBfk-04
#<Making an UNO card game in Python>
#https://www.youtube.com/watch?v=-Y2YIEhU75M&t=848s
#https://www.youtube.com/watch?v=cVX7hR3bX7A

import itertools
import random
class Deck:
    def __init__(self):
        self.color_list = ['Blue','Red','Yellow','Green']
        self.number = []
        for i in range(10):
            for _ in range(2):
                self.number.append(str(i))
        self.number.remove('0')
        for _ in range(2):
            self.number.extend(['+2', 'Skip', 'Reverse'])
        self.function_card = list(itertools.product(['Skip','Reverse','+2'], self.color_list)) 
        self.function_card.extend([('Wild','Black'),('+4','Black')])
        self.draw_deck = []
        self.discard_deck = []
        self.players_cards_list = [[], [], [], []]
        self.current_card= tuple()
        self.drawn = False
        self.played = False
        self.check_special = 0  
        self.color_chosen = False
        self.background_voice = ""
        self.winner=-1
        self.playing_check = False
        self.extend_time=-1
        self.direction = 1
        self.position = -1
        self.win_check = [True]*4
        self.level1ai = True
        self.choose_emoji = False
        self.ai_name = {1:'ROBINHOOD',2:'PRINCE JOHN',3:'MAID MARIAN'}
        self.player_name_list = ('YOU','ROBINHOOD','PRINCE JOHN','MAID MARIAN')
        self.discard = False
        self.scoreboard_dic={}
    
    def draw_from_stack(a, card_in_hand):
        need = []
        for card in card_in_hand:
            if (a.current_card[0] != card[0] and a.current_card[1] != card[1]) and (card[0] not in ('+4', 'Wild')):
                need.append(True)
            else:
                need.append(False)

        if not a.drawn and ((False in need) is False):
            try:
                a.players_cards_list[0].append(a.draw_deck.pop())
            except:
                a.draw_deck, a.discard_deck = a.discard_deck, a.draw_deck
                random.shuffle(a.draw_deck)
                a.players_cards_list[0].append(a.draw_deck.pop())
            finally:
                a.drawn = True
        

    def check_draw_deck_last_card(self):
        return self.draw_deck[-1]

    def check_discard_deck_last_card(self):
        return self.discard_deck[-1]
        
    
    def creat_deck(self):
        self.draw_deck = list(itertools.product(self.number, self.color_list))  
        for _ in range(4):  
            self.draw_deck.append(('Wild', 'Black'))
            self.draw_deck.append(('+4', 'Black'))
            random.shuffle(self.draw_deck) 

        while self.check_draw_deck_last_card() in self.function_card:  
            random.shuffle(self.draw_deck)

        self.discard_deck.append(self.draw_deck.pop())  
        self.current_card = self.check_discard_deck_last_card()

        for j in range(4): 
            for _ in range(7):
                self.players_cards_list[j].append(self.draw_deck.pop())
    
    def next_position(self, checkings):
        if self.current_card[0] == 'Reverse' and self.check_special == 0:
            self.direction *= -1  
            self.check_special = 1 
        if self.current_card[0] == 'Skip' and self.check_special == 0:
            self.check_special = 1
            self.position = (self.position + self.direction) % 4

        if checkings:
            self.position = (self.position + self.direction) % 4

    def re_set(self):
        self.background_voice = ""  
        self.winner = -1
        self.playing_check = False
        self.extend_time = -1
        self.players_cards_list = [[], [], [], []]
        self.draw_deck = []
        self.discard_deck = []
        self.direction = 1 
        self.position = -1  
        self.check_special = 0  
        self.current_card = tuple()
        self.drawn = False
        self.played = False
        self.color_chosen = False
        self.win_check = [True] * 4
        self.level1ai = True
        self.creat_deck()

    def draw_cards(self):
        if self.drawn == False:
            try:
                self.players_cards_list[0].append(self.draw_deck.pop())
            except:
                self.draw_deck, self.discard_deck = self.discard_deck, self.draw_deck
                random.shuffle(self.draw_deck)
                self.players_cards_list[0].append(self.draw_deck.pop())
            finally:
                self.drawn = True

    def play_card(self, card):
        if self.played == False:
            if (card[0] == self.current_card[0] or card[1] == self.current_card[1]) and (card[0] not in ('+4', 'Wild')):
                self.played = True
                self.drawn = True
                self.discard_deck.append(card)
                self.current_card = self.check_discard_deck_last_card()
                self.players_cards_list[0].remove(self.current_card)
                self.check_special = 0
                self.next_position(False)

        if card[1] == 'Black':
            self.played = True
            self.drawn = True
            self.color_chosen = True
            self.players_cards_list[0].remove(card)
            self.discard_deck.append(card)

    def card_select_color(self, color):
        self.discard_deck[-1] = (self.discard_deck[-1][0], color)
        self.current_card = self.check_discard_deck_last_card()
        self.check_special = 0

    def deal2and4(self, n):
        for _ in range(n):
            try:
                self.players_cards_list[self.position].append(self.draw_deck.pop())
            except:
                self.draw_deck, self.discard_deck = self.discard_deck, self.draw_deck
                random.shuffle(self.draw_deck)
                self.players_cards_list[self.position].append(self.draw_deck.pop())
        self.background_voice = "%s Draws %d cards" % (self.ai_name[self.position], n)
        self.check_special = 1

    def deal_black_cards(self, item):
        self.check_special = 0
        self.discard_deck.append(item)
        self.current_card = self.check_discard_deck_last_card()
        if not self.level1ai:  
            d = dict()
            d['Blue'] = 0
            d['Green'] = 0
            d['Yellow'] = 0
            d['Red'] = 0
            d['Black'] = 0
            for _item in self.players_cards_list[self.position]:
                d[_item[1]] += 1
            d = sorted(d.items(), key=lambda kv: (kv[1], kv[0]))   
            new_color = d[-1][0]  
            if new_color == 'Black':
                new_color = d[-2][0]
        else:
            new_color = random.choice(self.color_list)  
        self.background_voice = "%s plays %s %s, new color is %s" % (self.ai_name[self.position], item[0], item[1], new_color)
        self.current_card = (self.current_card[0], new_color)

    def check_points(self):
        final_points = 0
        self.players_points = []
        for players_deck in self.players_cards_list:
            for card in players_deck:
                if card[0] == 'Wild' or card[0] == '+4':
                    final_points+=50
                elif card[0] in ('+2','Skip','Reverse'):
                    final_points+=20
                elif card[0] in ('0','1','2','3','4','5','6','7','8','9'):
                    final_points+= int(card[0])
            self.players_points.append(final_points)
            final_points = 0
        return self.players_points

    def order_of_players(self):
        lowest = min(self.players_points)
        highest = max(self.players_points)
        print(lowest)
        print(highest)
        list_of_players=[1,2,3,4]
        print(self.players_points)
        removed =[]
        for i in range(4):
            if self.players_points[i] == lowest:
                self.winner_name = self.player_name_list[i]
                print(self.winner_name)
                list_of_players.remove(i+1)
            if self.players_points[i] == highest:
                self.fourth = self.player_name_list[i]
                print(f"fourth is {self.fourth}")
                if self.players_points[i] not in removed:
                    list_of_players.remove(i+1)
                removed.append(highest)

        c1 = list_of_players[0]
        d1 = list_of_players[1]
        if self.players_points[c1-1]<self.players_points[d1-1]:
            self.third = self.player_name_list[d1-1]
            self.second = self.player_name_list[c1-1]
        else:
            self.third = self.player_name_list[c1-1]
            self.second = self.player_name_list[d1-1]
        self.orders = []
        self.orders.append(self.winner_name)
        self.orders.append(self.second)
        self.orders.append(self.third)
        self.orders.append(self.fourth)
        return self.orders

    def scoreboard(self):
        self.final_player_points = sorted(self.players_points)
        for i in range(4):
            self.scoreboard_dic[self.orders[i]] = self.final_player_points[i]
        return self.scoreboard_dic

a = Deck()




