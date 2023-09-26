from functions import *
import random


def ai_play_card(uno, card):
    uno.special_check = 0
    uno.deck2.append(card)
    uno.current = peek(uno.deck2)
    uno.message = "%s plays card %s" % (uno.bot_map[uno.position], uno.current[1] + " " + uno.current[0])


def ai_action(uno, sounds):
    uno.message = ""
    uno.uno[uno.position] = False
    uno.check = 0
    if (uno.current[0] == '+2' or uno.current[0] == '+4') and uno.special_check == 0:
        dealwith_Plus2_Plus4(uno, int(uno.current[0][1]))
        uno.played_check = 1

    else:
        k = len(uno.player_list[uno.position])
        uno.player_list[uno.position].remove(uno.player_list[uno.position][random.randint(0, k)])
        try:
            uno.player_list[uno.position].append(uno.deck1.pop())
        except:
            uno.deck1, uno.deck2 = uno.deck2, uno.deck1
            random.shuffle(uno.deck1)
            uno.player_list[uno.position].append(uno.deck1.pop())

        flag = 0
        for card in uno.player_list[uno.position]:
            if uno.current[1] in card or uno.current[0] in card:
                ai_play_card(uno, card)

                if card[1] == 'Black':
                    dealwith_black(uno, card)

                uno.player_list[uno.position].remove(card)

                set_next_player(uno, False)
                flag = 1
                break

        if flag == 0:
            black_flag = 0
            for card in uno.player_list[uno.position]:
                if 'Black' in card:
                    uno.message = "%s plays %s" % (uno.bot_map[uno.position], card[0] + " " + card[1])
                    dealwith_black(uno, card)
                    uno.player_list[uno.position].remove(card)
                    black_flag = 1
                    break
            if black_flag == 0:
                try:
                    new_card = (uno.deck1.pop())
                except:
                    uno.deck1, uno.deck2 = uno.deck2, uno.deck1
                    random.shuffle(uno.deck1)
                    new_card = (uno.deck1.pop())

                uno.message = "%s draws a card" % uno.name_map[uno.position]

                if new_card[1] == 'Black':
                    uno.message = "%s plays %s" % (uno.bot_map[uno.position], new_card[0] + " " + new_card[1])
                    dealwith_black(uno, new_card)
                elif new_card[1] == uno.current[1] or new_card[0] == uno.current[0]:
                    ai_play_card(uno, new_card)
                else:
                    uno.player_list[uno.position].append(new_card)
        if len(uno.player_list[uno.position]) == 1:
            if uno.easy and random.randint(0, 1):
                uno.uno[uno.position] = True
                uno.message = "%s shouted UNO!" % uno.bot_map[uno.position]
                sounds.uno.play()
            else:
                uno.uno[uno.position] = True
                uno.message = "%s shouted UNO!" % uno.bot_map[uno.position]
                sounds.uno.play()
