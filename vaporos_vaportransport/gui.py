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
            self.__update()

        self.__quit()

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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

        self.clock = pygame.time.Clock()

    def __quit(self):
        pygame.quit()
        quit()
