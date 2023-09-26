
from functions import *
import random

def choose_a_color(m, ess, music_on, sound):
    if 395 < m[0] < 440 and 390 < m[1] < 450:  # Red Button
        ess.choose_color = False
        play_this_card_2(ess, "Red")
        if music_on:
            sound.click.play()
    if 450 < m[0] < 495 and 390 < m[1] < 450:  # Green Button
        ess.choose_color = False
        play_this_card_2(ess, "Green")
        if music_on:
            sound.click.play()
    if 505 < m[0] < 550 and 390 < m[1] < 450:  # Blue Button
        ess.choose_color = False
        play_this_card_2(ess, "Blue")
        if music_on:
            sound.click.play()
    if 560 < m[0] < 605 and 390 < m[1] < 450:  # Yellow Button
        ess.choose_color = False
        play_this_card_2(ess, "Yellow")
        if music_on:
            sound.click.play()


def take_from_stack(uno, card_in_hand):
    need = []
    for card in card_in_hand:
        if (uno.current[0] != card[0] and uno.current[1] != card[1]) and (card[0] not in ('+4', 'Wild')):
            need.append(True)
        else:
            need.append(False)

    if not uno.drawn and ((False in need) is False):
        try:
            uno.player_list[0].append(uno.deck1.pop())
        except:
            uno.deck1, uno.deck2 = uno.deck2, uno.deck1
            random.shuffle(uno.deck1)
            uno.player_list[0].append(uno.deck1.pop())
        finally:
            uno.drawn = True


def play_this_card(uno, card):
    if not uno.played:
        if (card[0] == uno.current[0] or card[1] == uno.current[1]) and (card[0] not in ('+4', 'Wild')):
            uno.played = True
            uno.deck2.append(card)
            uno.current = peek(uno.deck2)
            uno.player_list[0].remove(uno.current)
            uno.special_check = 0
            set_next_player(uno, False)

        if card[1] == 'Black':
            uno.played = True
            uno.choose_color = True
            uno.player_list[0].remove(card)
            uno.deck2.append(card)


def play_this_card_2(uno, color):
    uno.deck2[-1] = (uno.deck2[-1][0], color)
    uno.current = peek(uno.deck2)
    uno.special_check = 0
