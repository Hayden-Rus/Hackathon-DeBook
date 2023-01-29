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
double_pic = pygame.image.load('Double.jpg').convert_alpha(screen)
double_pic = pygame.transform.scale(double_pic,(800, 600))
split_pic = pygame.image.load('Split.jpg').convert_alpha(screen)
split_pic = pygame.transform.scale(split_pic,(800, 600))



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
    soft = False
    x_cord = None
    y_cord = None
    start_title_font = pygame.font.Font(None, 50)
    button_font = pygame.font.Font(None, 40)
    instruction_font = pygame.font.Font(None, 20)
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
    hit_enter = instruction_font.render("(Click And Hit Enter)", 0, ((0, 0,0)))
    hit_enter_rectangle = hit_enter.get_rect(
        center=(WIDTH // 2  -200, HEIGHT // 2 +280))
    win.blit(hit_enter, hit_enter_rectangle)
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
                                if (int(val) < 21 and int(val)>3):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_1:
                                val += str(1)
                                if (int(val) < 21 and int(val)>3):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_2:
                                val += str(2)
                                if (int(val) < 21 and int(val)>3):
                                    draw_text(x_cord, y_cord, val)
                                else:
                                    break
                            if event.key == pygame.K_3:
                                val += str(3)
                                if (int(val) < 21 and int(val)>3):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_4:
                                val += str(4)
                                if (int(val) < 21 and int(val)>3):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_5:
                                val += str(5)
                                if (int(val) < 21 and int(val)>3):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_6:
                                val += str(6)
                                if (int(val) < 21 and int(val)>3):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_7:
                                val += str(7)
                                if (int(val) < 21 and int(val)>3):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_8:
                                val += str(8)
                                if (int(val) < 21 and int(val)>3):
                                    draw_text(x_cord, y_cord, val)
                            if event.key == pygame.K_9:
                                val += str(9)
                                if (int(val) < 21 and int(val)>3):
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
                                if (int(dealer) < 12):
                                    draw_text(x_cord, y_cord, dealer)
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

                if(224 <= x_cord <= 254 and 535 <= y_cord <= 565):
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if(soft):
                                soft = False
                            else:
                                soft = True
                            print(soft)
                            if soft == True:

                                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(232, 543, 15, 15))
                                pygame.display.update()
                            else:
                                pygame.draw.rect(screen, (255, 255, 240), pygame.Rect(224, 535, 30, 30))
                                pygame.display.update()


                    #(screen, (255, 255, 240), pygame.Rect(225, 535, 30, 30))
                    #







                if submit_rectangle.collidepoint((x_cord,y_cord)):
                    print(val,dealer,soft)
                     # sys.exit()
                    val = int(val)
                    dealer = int(dealer)
                    if((val == 12) and (soft == True)):
                        split(screen)
                    elif val < 5:
                        draw_hit(screen)
                    elif((5<=val <=8) and (2<=dealer <= 11)):
                        print("problem1")
                        draw_hit(screen)



                    elif((9<= val <= 11) and (2<= dealer <= 6) and (soft == False)):
                        print("problem")
                        double_screen(screen)


                    elif((val == 9) and (7<= dealer <= 11) and (soft == False)):
                        print("problem3")
                        draw_hit(screen)



                    elif((10<= val <=  11) and (7<=  dealer <= 9) and (soft == False)):
                        print("problem4")
                        double_screen(screen)


                    elif((val == 10) and (dealer == 10 or dealer == 11) and (soft == False)):
                        print("problem5")
                        draw_hit(screen)




                    elif((val == 11) and (dealer == 10 or dealer == 11) and (soft == False)):
                        print("problem6")
                        double_screen(screen)


                    elif((val == 12) and (dealer == 2 or dealer ==  3) and (soft == False)):
                        print("problem7")
                        draw_hit(screen)




                    elif((val == 12) and (4 <= dealer <= 6) and (soft == False)):
                        print("problem8")
                        draw_stand(screen)


                    elif((val == 12) and (7<= dealer <= 11) and (soft == False)):
                        print("problem9")
                        draw_hit(screen)



                    elif((13 <= val <= 16) and (2 <= dealer <= 6) and (soft == False)):
                        print("problem10")
                        draw_stand(screen)


                    elif((val == 13 or val == 14) and (7 <= dealer <= 11) and (soft == False)):
                        print("problem11")
                        draw_hit(screen)



                    elif((val == 15 or val == 16) and (7<= dealer <= 9) and (soft == False)):
                        print("problem12")
                        draw_hit(screen)



                    elif((val == 15 or val == 16) and (dealer == 10 or dealer == 11) and (soft == False)):
                        print("problem13")
                        draw_hit(screen)



                    elif((val == 17) and (2 <= dealer <= 11) and (soft == False)):
                        print("problem14")
                        draw_stand(screen)


                    elif((18 <= val <= 20) and (2 <=dealer <= 11) and (soft == False)):
                        print("problem15")
                        draw_stand(screen)


                    elif((13 <= val <= 16) and (dealer == 2 or dealer == 3) and (soft == True)):
                        print("problem16")
                        draw_hit(screen)


                    elif((val == 13) and (dealer == 4) and (soft == True)):
                        print("problem17")
                        draw_hit(screen)


                    elif((val == 13) and (dealer == 5 or dealer ==  6) and (soft == True)):
                        print("problem18")
                        double_screen(screen)


                    elif((val == 13) and (7 <= dealer <= 11) and (soft == True)):
                        print("problem19")
                        draw_hit(screen)



                    elif((14 <= val <= 16) and (4<= dealer <= 6) and (soft == True)):
                        print("problem20")
                        double_screen(screen)


                    elif((14 <= val <= 16) and (7<= dealer <= 11) and (soft == True)):
                        print("problem21")
                        draw_hit(screen)



                    elif((val == 17) and (dealer == 2) and (soft == True)):
                        print("problem22 ")
                        draw_hit(screen)



                    elif((val == 17) and (3<= dealer <=6) and (soft == True)):
                        print("problem23")
                        double_screen(screen)


                    elif((val == 17) and (7 <= dealer <= 11) and (soft == True)):
                        print("problem 24")
                        draw_hit(screen)



                    elif((val == 18) and (2<= dealer <= 6) and (soft == True)):
                        print("problem25")
                        double_screen(screen)


                    elif((val == 18) and (dealer == 7 or  dealer == 8) and (soft == True)):
                        print("problem26")
                        draw_stand(screen)


                    elif((val == 18) and (9<= dealer <= 11) and (soft == True)):
                        print("problem 27")
                        draw_hit(screen)



                    elif((val == 19 or val == 20) and (2 <=dealer <= 5) and (soft == True)):
                        print("problem28")
                        draw_stand(screen)


                    elif((val == 19) and (dealer == 6) and (soft == True)):
                        print("problem29")
                        double_screen(screen)


                    elif((val == 19) and (7 <= dealer <= 11) and (soft == True)):
                        print("problem30")
                        draw_stand(screen)


                    elif((val == 20) and (6<= dealer <= 11) and (soft == True)):
                        print("problem31")
                        draw_stand(screen)


                    else:
                        split(screen)
















def double_screen(win):
    start_title_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 50)
    win.fill((255, 255, 240))
    win.blit(double_pic, (0, 0))
    pygame.display.flip()

    title_surface = start_title_font.render("You know you gotta Double it!!", 0, ((255,255,0)))
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 80))
    win.blit(title_surface, title_rectangle)

    exit_text = button_font.render("Return", 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2 - 100, HEIGHT // 2 + 270))

    win.blit(exit_surface, exit_rectangle)

    quit_text = button_font.render("Quit", 0, (255, 255, 255))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2 + 100, HEIGHT // 2 + 270))
    win.blit(quit_surface, quit_rectangle)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rectangle.collidepoint(event.pos):
                    draw_quit(win)
                if exit_rectangle.collidepoint(event.pos):
                   draw_debook_opened(screen)

    pass
stand_screen = pygame.image.load("stand.png").convert_alpha(screen)
stand_screen = pygame.transform.scale(stand_screen,(544,544))

hit_screen = pygame.image.load("Hit.jpg").convert_alpha(screen)
hit_screen = pygame.transform.scale(hit_screen,(800,600))

quit_screen = pygame.image.load("Quit.jpeg").convert_alpha(screen)
quit_screen = pygame.transform.scale(quit_screen,(800,700))

def split(win):
    start_title_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 50)
    win.fill((255, 255, 240))
    win.blit(split_pic, (0, 0))
    pygame.display.flip()

    title_surface = start_title_font.render("SPLIT THEM!!!", 0, ((255, 0, 0)))
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    win.blit(title_surface, title_rectangle)

    exit_text = button_font.render("Return", 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2 - 100, HEIGHT // 2 + 270))

    win.blit(exit_surface, exit_rectangle)

    quit_text = button_font.render("Quit", 0, (255, 255, 255))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2 + 100, HEIGHT // 2 + 270))
    win.blit(quit_surface, quit_rectangle)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rectangle.collidepoint(event.pos):
                    sys.exit()
                if exit_rectangle.collidepoint(event.pos):
                    draw_debook_opened(screen)

    pass

def draw_stand(win):

    start_title_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 50)
    win.fill((211, 211, 211))
    win.blit(stand_screen, (100, 75))
    pygame.display.flip()

    title_surface = start_title_font.render("Stand, Trust Its a Facecard", 0, ((200, 0, 0)))
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2 , HEIGHT // 2 - 200))
    win.blit(title_surface, title_rectangle)

    exit_text = button_font.render("Return", 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2 -115, HEIGHT // 2 + 220))

    win.blit(exit_surface, exit_rectangle)

    quit_text = button_font.render("Exit", 0, (255, 255, 255))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2 + 115, HEIGHT // 2 + 220))
    win.blit(quit_surface, quit_rectangle)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rectangle.collidepoint(event.pos):
                    draw_quit(win)
                if exit_rectangle.collidepoint(event.pos):
                    draw_debook_opened(win)

    pass
def draw_hit(win):
    start_title_font = pygame.font.Font(None, 65)
    sub_title_font = pygame.font.Font(None, 30)
    button_font = pygame.font.Font(None, 50)

    win.blit(hit_screen, (0, 0))
    pygame.display.flip()

    title_surface = start_title_font.render("Hit, there's a 0.1% chance you bust", 0, ((200, 0, 0)))
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 250))
    win.blit(title_surface, title_rectangle)

    sub_surface = sub_title_font.render("(we are not liable for lost money :D)", 0, ((200, 0, 0)))
    sub_rectangle = sub_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 215))
    win.blit(sub_surface, sub_rectangle)

    exit_text = button_font.render("Return", 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2 - 100, HEIGHT // 2 + 255))

    win.blit(exit_surface, exit_rectangle)

    quit_text = button_font.render("Quit", 0, (255, 255, 255))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2 + 100, HEIGHT // 2 + 255))
    win.blit(quit_surface, quit_rectangle)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rectangle.collidepoint(event.pos):
                    draw_quit(win)
                if exit_rectangle.collidepoint(event.pos):
                    draw_debook_opened(screen)
    pass
def draw_quit(win):

    start_title_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 50)
    win.fill((255, 255, 240))
    win.blit(quit_screen, (0, 0))
    pygame.display.flip()


    exit_text = button_font.render("Return", 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2 +225, HEIGHT // 2 + 250))

    win.blit(exit_surface, exit_rectangle)

    quit_text = button_font.render("Exit", 0, (255, 255, 255))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2 +350 , HEIGHT // 2 + 250))
    win.blit(quit_surface, quit_rectangle)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rectangle.collidepoint(event.pos):
                    draw_quit(win)
                if exit_rectangle.collidepoint(event.pos):
                    draw_debook_opened(screen)

    pass

def split(win):
    start_title_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 50)
    win.fill((255, 255, 240))
    win.blit(split_pic, (0, 0))
    pygame.display.flip()

    title_surface = start_title_font.render("SPLIT THEM!!!", 0, ((255, 0, 0)))
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    win.blit(title_surface, title_rectangle)

    exit_text = button_font.render("Return", 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2 - 100, HEIGHT // 2 + 270))

    win.blit(exit_surface, exit_rectangle)

    quit_text = button_font.render("Quit", 0, (255, 255, 255))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2 + 100, HEIGHT // 2 + 270))
    win.blit(quit_surface, quit_rectangle)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rectangle.collidepoint(event.pos):
                    draw_quit(win)
                if exit_rectangle.collidepoint(event.pos):
                    draw_debook_opened(screen)

    pass



def main():
    pygame.display.set_caption("Feeling Lucky?")
    draw_debook_cover(screen)

if __name__ == '__main__':
    main()
    #hehehehe