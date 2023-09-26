import pygame


class Image(object):
    def __init__(self):
        # Loading required image files
        self.icon = pygame.image.load("images/icon.png")
        self.load = pygame.image.load("images/uno_load.png")
        self.bg = pygame.image.load("images/background.png")
        self.back = pygame.image.load("images/return-button.png")
        self.mute = pygame.image.load("images/mute.png")
        self.unmute = pygame.image.load("images/unmute.png")
        self.p1 = pygame.image.load("images/woman.png")
        self.p2 = pygame.image.load("images/man.png")
        self.p3 = pygame.image.load("images/woman (1).png")
        self.p4 = pygame.image.load("images/man (1).png")
        self.card_back = pygame.image.load("images/Back.png")
        self.card_back_l = pygame.image.load("images/Back_left.png")
        self.card_back_r = pygame.image.load("images/Back_right.png")
        self.card_back_i = pygame.image.load("images/Back_inverted.png")
        self.done = pygame.image.load("images/checked.png")
        self.emoji = pygame.image.load("images/emoji.png")
        self.emoji_list = [pygame.image.load("images/emoji1.png"),
                           pygame.image.load("images/emoji2.png"),
                           pygame.image.load("images/emoji3.png"),
                           pygame.image.load("images/emoji4.png")]
        self.dialogue = pygame.image.load("images/dialogue.png")
        self.line = pygame.image.load("images/minus-line.png")
        self.uno = pygame.image.load("images/UNO.png")
        self.uno_button = pygame.image.load("images/UNOButton.png")
        self.red = pygame.image.load("images/SmallRed.png")
        self.blue = pygame.image.load("images/SmallBlue.png")
        self.yellow = pygame.image.load("images/SmallYellow.png")
        self.green = pygame.image.load("images/SmallGreen.png")

class Sound(object):
    def __init__(self):
        # Loading required sound files
        self.back_g = "sound/BG_MUSIC.mp3"
        self.click = pygame.mixer.Sound('sound/click.wav')
        self.uno = pygame.mixer.Sound("sound/UNO.mp3")
        self.victory = pygame.mixer.Sound("sound/VICTORY.mp3")


class TextFont(object):
    def __init__(self):
        self.silom = "fonts/Silom.ttf"

