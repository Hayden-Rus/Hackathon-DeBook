import pygame, sys, math
pygame.init()
screen = pygame.display.set_mode((800, 600))
WIDTH = 800
HEIGHT = 600
LINE_COLOR = (0 , 0 , 0 )
background = pygame.image.load("Start Screen.png").convert_alpha(screen)
debook_open = pygame.image.load("debook_opened.jpeg").convert_alpha(screen)
debook_open = pygame.transform.scale(debook_open,(960,720))
red_card = pygame.image.load('Player Card.jpg')
red_card = pygame.transform.scale(red_card,(200, 250))
blue_card = pygame.image.load('Dealers Card.jpg')
blue_card = pygame.transform.scale( blue_card,(200, 250))
def draw_debook_cover(win):
    start_title_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 50)

    win.blit(background, (0, 0))
    pygame.display.flip()

    title_surface = start_title_font.render("DEBOOK", 0, ((255, 255, 245)))
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 - 150))
    win.blit(title_surface, title_rectangle)

    exit_text = button_font.render("Enter", 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 220))

    win.blit(exit_surface, exit_rectangle)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
               if exit_rectangle.collidepoint(event.pos):
                   # sys.exit()
                draw_debook_opened(screen)
def draw_debook_opened(win):
    start_title_font = pygame.font.Font(None, 50)
    button_font = pygame.font.Font(None, 40)
    win.blit(debook_open, (-80, -55))
    win.blit(red_card, (125, 150))
    red_card_caption =  start_title_font.render("Player Hand:", 0, ((255, 0,0)))
    rcaption_rectangle = red_card_caption.get_rect(
        center=(WIDTH // 2 - 167, HEIGHT // 2 -200))
    win.blit(red_card_caption, rcaption_rectangle)
    blue_card_caption =  start_title_font.render("Dealer's Face Up:", 0, ((0, 0, 0)))
    bcaption_rectangle = blue_card_caption.get_rect(
        center=(WIDTH // 2 + 175, HEIGHT // 2 - 200))
    win.blit(blue_card_caption, bcaption_rectangle)
    win.blit(blue_card,(475, 150))
    pygame.display.flip()




    submit_text = button_font.render("SUBMIT", 0, (255, 255, 220))
    submit_surface = pygame.Surface((submit_text.get_size()[0] + 10, submit_text.get_size()[1] + 10))
    submit_surface.fill((0,200,50))
    submit_surface.blit(submit_text, (5, 5))



    submit_rectangle = submit_surface.get_rect(
        center=(WIDTH // 2 + 260, HEIGHT // 2 + 265))

    win.blit(submit_surface, submit_rectangle)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
               if submit_rectangle.collidepoint(event.pos):
                   sys.exit()


if __name__ == '__main__':
    pygame.display.set_caption("Feeling Lucky?")
    draw_debook_cover(screen)
