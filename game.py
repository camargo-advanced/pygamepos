import pygame
import sys
from pygame.locals import *
from galaxy import Galaxy
from utils import *
from sales import Sales
print(sys.platform)
COLOR_DEPTH = 8
FPS = 30
SCREEN_SIZE = (800, 480) # 5:3 aspect ratio for raspberrypi screen 7"
RASPBERRYPI_PLATFORM = 'linux'

class Game():
    def __init__(self):
        pygame.init()  # initialize pygame library and set screen mode
        if sys.platform == RASPBERRYPI_PLATFORM:
            self.screen = pygame.display.set_mode(
                flags=pygame.FULLSCREEN,
                depth=COLOR_DEPTH)  # initialize the display
        else:
            self.screen = pygame.display.set_mode(
                size=SCREEN_SIZE,
                depth=COLOR_DEPTH)  # initialize the display
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Vegan Bunny POS")  # set window caption
        #pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()  # the time starts

    def new_game(self):
        # build a new galaxy from scratch
        self.galaxy = Galaxy(self.screen_rect)
        # build the sales screeen to put order to the gui caos
        Sales(self.galaxy)

    def run(self):
        self.new_game()
        # game main loop!
        done = False
        while not done:

            # Press Q (all systems) or ALT+F4 (Windows) or CMD+Q (MAC) to quit the game !
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == KEYDOWN and event.key == K_q or event.type == QUIT:
                    done = True

            # set the framerate, updates entities in the galaxy
            # render the entities on buffer and flips the buffer to screen
            time_passed = self.clock.tick(FPS)/1000.0
            self.galaxy.update(time_passed, event_list)
            self.galaxy.render(self.screen)
            self.galaxy.cleanup()

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    Game().run()  # start the game !
