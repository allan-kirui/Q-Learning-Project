import pygame
import Colors as color

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
MARGIN = 5

class Window:

    def __init__(self):
        self.BOARD_SIZE

    def run(self):


        grid = []
        for row in range(BOARD_SIZE):
            grid.append([])
            for column in range(BOARD_SIZE):
                grid[row].append(0)
        grid[1][5] = 1
        pygame.init()
        window_size = [255, 255]
        scr = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Grid")
        done = False
        clock = pygame.time.Clock()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    grid[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)
            scr.fill(black)
            for row in range(10):
                for column in range(10):
                    color = white
                    if grid[row][column] == 1:
                        color = red
                    pygame.draw.rect(scr,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])
            clock.tick(50)
            pygame.display.flip()
        pygame.quit()

if __name__ == '__main__':
    Window().run()