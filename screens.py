# This is a sample Python script.
import pygame
import sys
from DEBOOOK import *
pygame.init()
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
screen = pygame.display.set_mode((800, 500))
WIDTH = 800
HEIGHT = 600
LINE_COLOR = (0 , 0 , 0 )
stand_screen = pygame.image.load("stand.png").convert_alpha(screen)
stand_screen = pygame.transform.scale(stand_screen,(544,544))

hit_screen = pygame.image.load("Hit.jpg").convert_alpha(screen)
hit_screen = pygame.transform.scale(hit_screen,(800,600))

quit_screen = pygame.image.load("Quit.jpeg").convert_alpha(screen)
quit_screen = pygame.transform.scale(quit_screen,(800,600))

double_pic = pygame.image.load('Double.jpg').convert_alpha(screen)
double_pic = pygame.transform.scale(double_pic,(800, 600))

split_pic = pygame.image.load('Split.jpg').convert_alpha(screen)
split_pic = pygame.transform.scale(split_pic,(800, 600))


def draw_stand(win):

    start_title_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 50)
    win.fill((255, 255, 240))
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
        center=(WIDTH // 2 -100, HEIGHT // 2 + 220))

    win.blit(exit_surface, exit_rectangle)

    quit_text = button_font.render("Exit", 0, (255, 255, 255))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2 + 100, HEIGHT // 2 + 220))
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
                    sys.exit()
                if exit_rectangle.collidepoint(event.pos):
                    main()
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
        center=(WIDTH // 2 +225, HEIGHT // 2 + 160))

    win.blit(exit_surface, exit_rectangle)

    quit_text = button_font.render("Exit", 0, (255, 255, 255))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2 +350 , HEIGHT // 2 + 160))
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
                    main()

    pass


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
                    sys.exit()
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
                    sys.exit()
                if exit_rectangle.collidepoint(event.pos):
                    draw_debook_opened(screen)

    pass
