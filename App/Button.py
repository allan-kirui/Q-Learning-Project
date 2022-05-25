import pygame


class Button:
    text = None
    rect = None
    surface = None
    size = None
    screen = None
    bg = None

    def __init__(self, screen, text, pos, font, feedback=""):
        self.screen = screen
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.bg = "black"
        self.change_text(text)

    def change_text(self, text):
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        self.screen.blit(self.surface, (self.x, self.y))

    def clickMove(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if self.bg == "red":
                        self.bg = "navy"
                    else:
                        self.bg = "red"
                    self.change_text(self.feedback)

                    return True
