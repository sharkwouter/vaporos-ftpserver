import pygame
import os.path


display_width = 1280
display_height = 720

black = (0, 0, 0)
white = (255, 255, 255)

font_regular = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
font_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

if not os.path.isfile(font_regular):
    font_regular = "fonts/DejaVuSansMono.ttf"

if not os.path.isfile(font_bold):
    font_bold = "fonts/DejaVuSansMono-Bold.ttf"


class Button():
    A = 0
    B = 1
    X = 2
    Y = 3
    LB = 4
    RB = 5
    SEL = 6
    START = 7
    HOME = 8
    LTHUMB = 9
    RTHUMB = 10


class GUI:

    def __init__(self, server):
        self.quit = False
        self.server = server
        self.url = server.get_url()

    def run(self):
        self.__setup()
        self.__mainloop()

    def __mainloop(self):
        while not self.quit:
            self.__check_events()
            self.__display_text("You can now connect to the following ftp server:",
                                (display_width/2), (display_height/2 - 48), 32, font=font_regular)
            self.__display_text(self.url, (display_width/2), (display_height/2), 48, font=font_bold)
            self.__display_text("Open this in your file browser",
                                (display_width / 2), (display_height / 2 + 48), 32, font=font_regular)
            self.__display_text("Press start to exit",
                                (display_width / 2), (display_height - 64), 32, font=font_regular)
            self.__update()

        self.__quit()

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == Button.SEL or event.button == Button.START:
                    self.quit = True

    def __display_text(self, text, x, y, size, text_color=white, font=font_regular):
        font = pygame.font.Font(font, size)
        text_surface = font.render(text, True, text_color)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (x, y)
        self.screen.blit(text_surface, text_rectangle)


    def __update(self):
        pygame.display.update()
        self.clock.tick(30)

    def __setup(self):
        pygame.init()

        self.screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("vaportransport: transfer files easily")

        pygame.joystick.init()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        for joystick in joysticks:
            joystick.init()

        self.clock = pygame.time.Clock()

    def __quit(self):
        pygame.quit()
        quit()
