import random
from deck import *


def ai_play_card(a, item):
    """AI plays a card"""
    a.check_special = 0
    a.discard_deck.append(item)
    a.current_card = a.check_discard_deck_last_card()
    a.background_voice = "%s plays card %s" % (a.ai_name[a.position], a.current_card[1] + " " + a.current_card[0])


def ai_action(a, sounds):
    """AI logic"""
    a.background_voice = ""
    a.win_check[a.position] = False
    a.check = 0
    if (a.current_card[0] == '+2' or a.current_card[0] == '+4') and a.check_special == 0:
        a.deal2and4(int(a.current_card[0][1]))
        a.played_check = 1

    else:
        k = len(a.players_cards_list[a.position])
        a.players_cards_list[a.position].remove(a.players_cards_list[a.position][random.randint(0, k-1)])
        try:
            a.players_cards_list[a.position].append(a.draw_deck.pop())
        except:
            a.draw_deck, a.discard_deck = a.discard_deck, a.draw_deck
            random.shuffle(a.draw_deck)
            a.players_cards_list[a.position].append(a.draw_deck.pop())
        flag = 0
        for card in a.players_cards_list[a.position]:
            if a.current_card[1] in card or a.current_card[0] in card:
                ai_play_card(a, card)

                if card[1] == 'Black':
                    a.deal_black_cards(card)

                a.players_cards_list[a.position].remove(card)

                a.next_position(False)
                flag = 1
                break

        if flag == 0:
            black_flag = 0
            for card in a.players_cards_list[a.position]:
                if 'Black' in card:
                    a.background_voice = "%s plays %s" % (a.ai_name[a.position], card[0] + " " + card[1])
                    a.deal_black_cards(card)
                    a.players_cards_list[a.position].remove(card)
                    black_flag = 1
                    break
            if black_flag == 0:
                try:
                    new_card = (a.draw_deck.pop())
                except:
                    a.draw_deck, a.discard_deck = a.discard_deck, a.draw_deck
                    random.shuffle(a.draw_deck)
                    new_card = (a.draw_deck.pop())

                a.background_voice = "%s draws a card" % a.ai_name[a.position]

                if new_card[1] == 'Black':
                    a.background_voice = "%s plays %s" % (a.ai_name[a.position], new_card[0] + " " + new_card[1])
                    a.deal_black_cards( new_card)
                elif new_card[1] == a.current_card[1] or new_card[0] == a.current_card[0]:
                    ai_play_card(a,new_card)
                else:
                    a.players_cards_list[a.position].append(new_card)
        if len(a.players_cards_list[a.position]) == 1:
            if a.level1ai and random.randint(0, 1):
                a.win_check[a.position] = True
                a.background_voice = "%s shouted UNO!" % a.ai_name[a.position]
                sounds.win_check.play()
            else:
                a.win_check[a.position] = True
                a.background_voice = "%s shouted UNO!" % a.ai_name[a.position]
                sounds.win_check.play()
        

