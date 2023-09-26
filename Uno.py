import sys

import pygame

from settings import Settings

from card_table import Cardtable

class Uno:
    """a class to manage resources of the game"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Uno Card Game")
        
        #set background color

        self.cardtable = Cardtable(self)

#INSIDE OF THE GAME LOOP
        
        
    def run_game(self):
        """start the main loop of the game"""
        while True:
            self._check_events()
            self._update_screen()
        

    def _check_events(self):
        """check mouse and keyboard events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.cardtable.blitme()
        pygame.display.flip()
            

if __name__ == '__main__':
    #create a game
    ai = Uno()
    ai.run_game()