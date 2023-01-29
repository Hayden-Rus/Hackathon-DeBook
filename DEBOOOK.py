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
main = False



def draw_text(x,y,value):
    if (190 <= x <= 250 and 420 <= y <= 480):
        font = pygame.font.SysFont('arial', 25)
        text = font.render(str(value), True, (0, 0, 0))
        screen.blit(text, (205,440))
    else:
        font = pygame.font.SysFont('arial', 25)
        text = font.render(str(value), True, (0, 0, 0))
        screen.blit(text, (565, 440))
    pygame.display.update()
def clear(x,y):
    if(190 <= x <= 250 and 420 <= y <= 480):
        rectangle(190, 420,60)
    else:
        rectangle(550, 420,60)
    pygame.display.update()

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


def rectangle(x,y,size):
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(x-(size*.055), y-(size*.055), size*1.133, size*1.133))
    pygame.draw.rect(screen, (255,255,240), pygame.Rect(x, y, size, size))
def draw_debook_opened(win):
    soft = 0
    x_cord = None
    y_cord = None
    start_title_font = pygame.font.Font(None, 50)
    button_font = pygame.font.Font(None, 40)
    win.blit(debook_open, (-80, -55))
    win.blit(red_card, (125, 150))

    red_card_caption =  start_title_font.render("Player Hand:", 0, ((255, 0,0)))
    rcaption_rectangle = red_card_caption.get_rect(
        center=(WIDTH // 2 - 167, HEIGHT // 2 -200))
    win.blit(red_card_caption, rcaption_rectangle)
    soft_caption = start_title_font.render("Soft", 0, ((255, 0, 0)))
    soft_rectangle = soft_caption.get_rect(
        center=(WIDTH // 2  -225, HEIGHT // 2 +250))
    win.blit(soft_caption, soft_rectangle)
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
    rectangle(190,420,60)
    rectangle(550, 420,60)
    rectangle(225, 535,30)
    win.blit(submit_surface, submit_rectangle)

    pygame.display.update()
    val = ""
    dealer = ""
    while True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_cord, y_cord = event.pos
                print(x_cord, y_cord)
            if(x_cord != None):
                if ((190 <= x_cord <= 250 and 420 <= y_cord <= 480)):
                    if event.type == pygame.KEYDOWN:
                        if len(val) < 2:
                            if event.key == pygame.K_0:
                                val += str(0)
                                if (int(val) < 21):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_1:
                                val += str(1)
                                if (int(val) < 21):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_2:
                                val += str(2)
                                if (int(val) < 21):
                                    draw_text(x_cord, y_cord, val)
                                else:
                                    break
                            if event.key == pygame.K_3:
                                val += str(3)
                                if (int(val) < 21):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_4:
                                val += str(4)
                                if (int(val) < 21):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_5:
                                val += str(5)
                                if (int(val) < 21):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_6:
                                val += str(6)
                                if (int(val) < 21):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_7:
                                val += str(7)
                                if (int(val) < 21):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_8:
                                val += str(8)
                                if (int(val) < 21):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_9:
                                val += str(9)
                                if (int(val) < 21):
                                    draw_text(x_cord, y_cord, val)
                        if event.key == pygame.K_BACKSPACE:
                            print("blah")
                            val = ""
                            clear(x_cord,y_cord)
                if(550 <= x_cord <= 610 and 420 <= y_cord <= 480):
                    if event.type == pygame.KEYDOWN:
                        if len(dealer) < 2:
                            if event.key == pygame.K_0:
                                dealer += str(0)
                                if (int(dealer) < 12):
                                    draw_text(x_cord, y_cord, dealer)
                            if event.key == pygame.K_1:
                                dealer += str(1)
                                if (int(dealer) < 12):
                                    draw_text(x_cord, y_cord, dealer)
                            if event.key == pygame.K_2:
                                dealer += str(2)
                                if (int(dealer) < 12):
                                    draw_text(x_cord, y_cord, dealer)
                                else:
                                    break
                            if event.key == pygame.K_3:
                                dealer += str(3)
                                if (int(dealer) < 12):
                                    draw_text(x_cord, y_cord, dealer)
                            if event.key == pygame.K_4:
                                dealer += str(4)
                                if (int(dealer) < 12):
                                    draw_text(x_cord, y_cord, dealer)
                            if event.key == pygame.K_5:
                                dealer += str(5)
                                if (int(dealer) < 12):
                                    draw_text(x_cord, y_cord, dealer)
                            if event.key == pygame.K_6:
                                dealer += str(6)
                                if (int(val) < 12):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_7:
                                dealer += str(7)
                                if (int(dealer) < 12):
                                    draw_text(x_cord, y_cord, dealer)
                            if event.key == pygame.K_8:
                                dealer += str(8)
                                if (int(dealer) < 12):
                                    draw_text(x_cord, y_cord, dealer)
                            if event.key == pygame.K_9:
                                dealer += str(9)
                                if (int(dealer) < 12):
                                    draw_text(x_cord, y_cord, dealer)
                        if event.key == pygame.K_BACKSPACE:
                            print("blah")
                            dealer = ""
                            clear(x_cord,y_cord)

                if(224<=x_cord <= 254 and 535 <=y_cord <=565):
                    # if soft == True:
                    #     soft = False
                    # else
                    #     soft = True
                    soft = 1- soft
                    if(soft == 1):
                        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(225, 535, 30, 30))
                        pygame.display.update()
                    else:
                        pygame.draw.rect(screen, (255, 255, 240), pygame.Rect(225, 535, 30, 30))
                        pygame.display.update()






                if submit_rectangle.collidepoint((x_cord,y_cord)):
                    sys.exit()
#hi




if __name__ == '__main__':
    pygame.display.set_caption("Feeling Lucky?")
    draw_debook_cover(screen)
    #sammy hii
