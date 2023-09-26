from AI_action import *
from classes import *
from functions import *
from player_action import *
import time

pygame.init()

img = Image()
pm = Mode()
sound = Sound()
fnt = TextFont()
c = commen()

root = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('UNO')
pygame.display.set_icon(img.icon)

pygame.mixer.music.load(sound.back_g)
pygame.mixer.music.play(-1)  
pygame.mixer.music.set_volume(0.3)  

active = True  
c.play_mode = pm.load  

disp = False
win_dec = False  
pen_check = False  
emo_chosen = -1
discard_flag = False

create_deck(c)


while active:
    
    for inp in pygame.event.get(): # Event supervised

        if inp.type == pygame.QUIT:
            active = False

        # Mouse click Check
        if inp.type == pygame.MOUSEBUTTONDOWN:
            m = pygame.mouse.get_pos()  # get mouse location

            if (750 < m[0] < 785 or 940 < m[0] < 975) and (120< m[1] < 150) and c.play_mode == pm.load: 
                if music_on:
                    sound.click.play()
                if c.easy:
                    c.easy = False
                else:
                    c.easy = True

            if 925 < m[0] < 990 and 500 < m[1] < 565 and emo_chosen == -1:  
                c.choose_emoji = True
                if music_on:
                    sound.click.play()

            if 10 < m[0] < 160 and 25 < m[1] < 170 and c.play_mode == pm.load:  
                if music_on:
                    sound.click.play()
                c.play_mode = pm.turn

            if 0 < m[0] < 265 and 340 < m[1] < 405 and c.play_mode == pm.load:  
                if music_on:
                    sound.click.play()
                c.play_mode = pm.info

            if 10 < m[0] < 42 and 10 < m[1] < 42 and (
                    c.play_mode == pm.in_game or c.play_mode == pm.info):  
                if music_on:
                    sound.click.play()
                re_initialize(c)
                c.play_mode = pm.load

            if 420 < m[0] < 555 and 425 < m[1] < 543 and c.play_mode == pm.win: 
                if music_on:
                    sound.click.play()
                re_initialize(c)
                win_dec = False
                c.play_mode = pm.load

            if 960 < m[0] < 1000 and 0 < m[1] < 40:  
                if music_on:
                    sound.click.play()
                if music_on:
                    pygame.mixer.music.pause()
                    music_on = False
                else:
                    pygame.mixer.music.unpause()
                    music_on = True

            if c.player_playing:  
                if 850 < m[0] < 916 and 500 < m[1] < 565:  
                    if music_on:
                        sound.uno.play()

                    c.uno[0] = True

                if 775 < m[0] < 840 and 505 < m[1] < 570:  
                    emo_chosen = -1
                    if music_on:
                        sound.click.play()
                    c.player_playing = False


                if c.discard is True:
                    if c.drawn is False:
                        take_from_stack(c, c.player_list[0])
                        if c.drawn and ((c.player_list[0][-1][0] == c.current[0] or c.player_list[0][-1][1] == c.current[1]) or
                                c.player_list[0][-1][0] in ('+4', 'Wild')):
                            if c.player_list[0][-1][1] != 'Black':
                                c.player_playing = False
                            play_this_card(c, c.player_list[0][-1])
                            c.discard = False

                    for i in range(625, 625 - 50 * len(c.player_list[0]),
                                   -50):  # 2nd Detecting the card clicked by user
                        if i < m[0] < i + 50 and 470 < m[1] < 585:

                            play_this_card(c, c.player_list[0][int((625 - i) / 50)])

                            if music_on:
                                sound.card_played.play()
                    c.discard = False
                    continue

                if c.discard is False:
                    for i in range(625, 625 - 50 * len(c.player_list[0]), -50):  # Detecting the card clicked by user
                        if i < m[0] < i + 50 and 470 < m[1] < 585:
                            c.deck2.reverse()
                            c.deck2.append(c.player_list[0][int((625 - i) / 50)])
                            c.deck2.reverse()
                            c.player_list[0].remove(c.player_list[0][int((625 - i) / 50)])
                            c.player_list[0].append(c.deck1.pop())
                            c.discard = True
                    # continue

            # Post sending emoji operation
            if c.choose_emoji:
                if 395 < m[0] < 440 and 390 < m[1] < 450:  # Laugh Cry
                    emo_chosen = 0
                    if music_on:
                        sound.click.play()
                if 450 < m[0] < 495 and 390 < m[1] < 450:  # Heart
                    emo_chosen = 1
                    if music_on:
                        sound.click.play()
                if 505 < m[0] < 550 and 390 < m[1] < 450:  # Crying
                    emo_chosen = 2
                    if music_on:
                        sound.click.play()
                if 560 < m[0] < 605 and 390 < m[1] < 450:  # Tongue
                    emo_chosen = 3
                    if music_on:
                        sound.click.play()

            # if discard_flag is True:
            #     c.discard = True
            # else:
            #     c.discard = False
            # Post black card operation, New color picker
            if c.choose_color:
                choose_a_color(m, c, music_on, sound)

    if c.play_mode == pm.load:
        # Blitting cential images and texts
        root.blit(img.load, (0, 0))
        text = pygame.font.Font(fnt.silom, 50).render("<", True, (0 , 0 , 128))
        root.blit(text, [750, 120])
        text = pygame.font.Font(fnt.silom, 50).render(">", True, (0 , 0 , 128))
        root.blit(text, [950, 120])
        if c.easy:
            text = pygame.font.Font(fnt.silom, 30).render("LEVEL 1", True, (0 , 0 , 128))
            root.blit(text, [818, 127])
        else:
            text = pygame.font.Font(fnt.silom, 30).render("LEVEL 2", True, (0 , 0 , 128))
            root.blit(text, [818, 127])

    elif c.play_mode == pm.turn:
        root.blit(img.bg, (0, 0))
        root.blit(img.back, (10, 10))
        root.blit(img.p1, (290, 30))
        root.blit(img.p2, (865, 90))
        root.blit(img.p3, (55, 440))
        root.blit(img.p4, (675, 490))
        text = pygame.font.Font(fnt.silom, 25).render("YOU", True, (255, 238, 46))
        root.blit(text, [690, 460])
        text = pygame.font.Font(fnt.silom, 25).render("PRINCE JOHN", True, (255, 238, 46))
        root.blit(text, [270, 4])
        text = pygame.font.Font(fnt.silom, 25).render("MAID MARIAN", True, (255, 238, 46))
        root.blit(text, [830, 60])
        text = pygame.font.Font(fnt.silom, 25).render("ROBINHOOD", True, (255, 238, 46))
        root.blit(text, [30, 410])
        text = pygame.font.Font(fnt.silom, 25).render(c.message, True, (255, 238, 46))
        root.blit(text, [340, 210])
        a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(a)
        result = a[0:4]
        print(result)

        root.blit(pygame.image.load("./images/Blue" + str(result[0]) + ".png"), (590 - 50 * 3, 470))
        root.blit(pygame.image.load("./images/Blue" + str(result[1]) + ".png"), (40, 315 - 30 * 3))
        root.blit(pygame.image.load("./images/Blue" + str(result[2]) + ".png"), (380 + 30 * 3, 20))
        root.blit(pygame.image.load("./images/Blue" + str(result[3]) + ".png"), (845, 190 + 30 * 3))

        c.position = result.index(max(result)) - 1
        c.play_mode = pm.in_game
        pen_check = True
        pygame.display.update()
        time.sleep(2)

    elif c.play_mode == pm.in_game:

        for i in c.player_list:
            if len(i) == 0:
                win_dec = True
                c.winner = c.player_list.index(i)
                break

        if c.play_lag == -1 and music_on:
            sound.shuffled.play()

        root.blit(img.bg, (0, 0))
        root.blit(img.back, (10, 10))
        root.blit(img.card_back, (340, 240))
        try:
            root.blit(pygame.image.load("images/" + c.current[1] + str(c.current[0]) + ".png"), (580, 240))
        except:
            root.blit(pygame.image.load("images/" + c.current[1] + ".png"), (580, 240))
        root.blit(img.p1, (290, 30))
        root.blit(img.p2, (865, 90))
        root.blit(img.p3, (55, 440))
        root.blit(img.p4, (675, 490))

        text = pygame.font.Font(fnt.silom, 20).render("YOU", True, (255, 238, 46))
        root.blit(text, [690, 460])
        text = pygame.font.Font(fnt.silom, 20).render("PRINCE JOHN", True, (255, 238, 46))
        root.blit(text, [270, 4])
        text = pygame.font.Font(fnt.silom, 20).render("MAID MARIAN", True, (255, 238, 46))
        root.blit(text, [830, 60])
        text = pygame.font.Font(fnt.silom, 20).render("ROBINHOOD", True, (255, 238, 46))
        root.blit(text, [30, 410])

        text = pygame.font.Font(fnt.silom, 20).render(c.message, True, (255, 238, 46))
        root.blit(text, [340, 210])

        for i in range(len(c.player_list[1])):
            root.blit(img.card_back_l, (40, 315 - 30 * i))
        for i in range(len(c.player_list[2])):
            root.blit(img.card_back_i, (380 + 30 * i, 20))
        for i in range(len(c.player_list[3])):
            root.blit(img.card_back_r, (845, 190 + 30 * i))
        for i in range(len(c.player_list[0])):
            root.blit(
                pygame.image.load("images/" + c.player_list[0][i][1] + str(c.player_list[0][i][0]) + ".png"),
                (590 - 50 * i, 470))

        if c.choose_color:
            root.blit(img.red, (395, 390))
            root.blit(img.green, (450, 390))
            root.blit(img.blue, (505, 390))
            root.blit(img.yellow, (560, 390))

        if c.choose_emoji:
            root.blit(img.emoji_list[0], (395, 390))
            root.blit(img.emoji_list[1], (450, 390))
            root.blit(img.emoji_list[2], (505, 390))
            root.blit(img.emoji_list[3], (560, 390))
        if emo_chosen > -1 and c.player_playing:
            root.blit(img.dialogue, (750, 450))
            root.blit(img.emoji_list[emo_chosen], (767, 455))
            c.choose_emoji = False

        if c.player_playing:  
            c.message = ""

            if not c.drawn and not c.played:  
                if c.current[0] == '+2' and c.special_check == 0:  
                    for _ in range(2):
                        try:
                            c.player_list[0].append(c.deck1.pop())
                        except:
                            c.deck1, c.deck2 = c.deck2, c.deck1
                            random.shuffle(c.deck1)
                            c.player_list[0].append(c.deck1.pop())
                    c.special_check = 1
                    c.player_playing = False

                elif c.current[0] == '+4' and c.special_check == 0:  # Draw 4
                    for _ in range(4):
                        try:
                            c.player_list[0].append(c.deck1.pop())
                        except:
                            c.deck1, c.deck2 = c.deck2, c.deck1
                            random.shuffle(c.deck1)
                            c.player_list[0].append(c.deck1.pop())
                    c.special_check = 1
                    c.player_playing = False
                # else:
                #     for card in c.player_list[0]:
                #         if (c.current[0] != card[0] and c.current[1] != card[1]) and (card[0] not in ('+4', 'Wild')) \
                #                 and (card[0] not in ('Reverse', 'Skip', '+2')):
                #             take_from_stack(c, c.player_list[0])
                #             if music_on:
                #                 sound.card_drawn.play()

            root.blit(img.line, (682, 550))
            root.blit(img.done, (775, 505))
            root.blit(img.emoji, (925, 500))
            root.blit(img.uno_button, (850, 500))

        else:
            if c.play_lag == 140:  
                disp = False
                pen_check = False

                set_curr_player(c, True)

                if c.position == 0:
                    c.uno[0] = False
                    c.player_playing = True

                else:
                    
                    c.played = False 
                    c.drawn = False

                    ai_action(c, sound)

                c.play_lag = 0  
            else:
                if win_dec and c.play_lag == 70: 
                    c.play_mode = pm.win

                if not pen_check:  
                    if c.position != -1 and len(c.player_list[c.position]) == 1 and not c.uno[c.position]:  # Penalty
                        # check_add = False
                        for j in range(2):
                            if c.position != j: 
                                c.player_list[c.position].append(c.player_list[j].pop())

                        c.message = "Penalty!"
                        c.uno[c.position] = True
                    pen_check = True

                c.play_lag += 1

                if not disp:
                    disp = True

                if (c.position + c.direction_check) % 4 == 1:
                    root.blit(img.line, (67, 512))
                elif (c.position + c.direction_check) % 4 == 2:
                    root.blit(img.line, (293, 85))
                elif (c.position + c.direction_check) % 4 == 3:
                    root.blit(img.line, (870, 145))

    elif c.play_mode == pm.info:
        root.blit(img.help, (0, 0))
        root.blit(img.back, (10, 10))

    elif c.play_mode == pm.win and c.winner != -1:

        if music_on:
            sound.victory.play()

        string = ""
        if c.winner == 0:
            string = "Well Done! You've Won this Round!"
        else:
            string = "%s has won this Round" % c.bot_map[c.winner]

        root.blit(img.win, (0, 0))
        text = pygame.font.Font(fnt.pacifico, 40).render(string, True, (255, 238, 46))
        root.blit(text, [190, 100])

    if music_on:
        root.blit(img.mute, (960, 8))
    else:
        root.blit(img.unmute, (960, 8))

    pygame.display.update()
