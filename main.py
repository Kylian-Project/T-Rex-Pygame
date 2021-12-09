#########################################
##### Copyright Kylian & Gabin 1°3 ######
#########################################


import pygame
from pygame import *
import random

pygame.init()

pygame.display.set_caption("Jeu Dino Beta Kylian & Gabin")
taille = largeur, hauteur = 1100, 600  # taille de la fenêtre
fenetre = pygame.display.set_mode(taille)  # def la taille avec la ligne juste au dessus

# Sol
sol = pygame.image.load("img/sol.png").convert_alpha()
nuage = pygame.image.load("img/sprite/cloud.png").convert_alpha()
nuage_rect = nuage.get_rect()

# Colisions
rectangle = pygame.image.load("img/colide/colision.png")
rectangle_large = pygame.image.load("img/colide/colision_large.png")
colide_cactus_rect = rectangle.get_rect()
colide_big_cactus_rect = rectangle_large.get_rect()
colide_dino_rect = rectangle.get_rect()

# Sprite dino
dino = pygame.image.load("img/sprite/t-rex.png").convert_alpha()
dinorect = dino.get_rect()

# Son
saut_sound = pygame.mixer.Sound('song/saut.wav')
pygame.mixer.music.load("song/back_sound.mp3")

# Variable curseur
nbcurseur = 'img/icon/curseur1.png'

# Image menu / icons / Buttons (menu princiaple)
background_menu = pygame.image.load("img/menu.png").convert()
rect_backmenu = background_menu.get_rect()

play_button = pygame.image.load("img/icon/play_but.png").convert_alpha()
rect_play = play_button.get_rect()
rect_play.x, rect_play.y = 402, 276  # place l'image sur l'écran

leave_button = pygame.image.load("img/icon/leave_but.png").convert_alpha()
rect_leave = leave_button.get_rect()
rect_leave.x, rect_leave.y = 402, 389  # place l'image sur l'écran

buy_button = pygame.image.load("img/icon/buy.png").convert_alpha()
rect_buy = buy_button.get_rect()
rect_buy.x, rect_buy.y = 1020, 10  # place l'image sur l'écran

info_button = pygame.image.load("img/icon/info.png").convert_alpha()
rect_info = info_button.get_rect()
rect_info.x, rect_info.y = 10, 10  # place l'image sur l'écran

setting_button = pygame.image.load("img/icon/gear.png").convert_alpha()
rect_setting = setting_button.get_rect()
rect_setting.x, rect_setting.y = 10, 514  # place l'image sur l'écran

# Image menu / icons / Buttons (menu options)
img_back_option = pygame.image.load("img/menu_option.png").convert_alpha()
rect_back_option = img_back_option.get_rect()

close_button = pygame.image.load("img/icon/close.png").convert_alpha()
rect_close = close_button.get_rect()
rect_close.x, rect_close.y = 720, 76  # place l'image sur l'écran

on_button = pygame.image.load("img/icon/on.png").convert_alpha()
rect_on_son = on_button.get_rect()  # button on du son
rect_on_son.x, rect_on_son.y = 653, 263
rect_on_debug = on_button.get_rect()  # button on du mode debug
rect_on_debug.x, rect_on_debug.y = 653, 343

off_button = pygame.image.load("img/icon/off.png").convert_alpha()
rect_off_son = off_button.get_rect()  # button off du son
rect_off_son.x, rect_off_son.y = 653, 263
rect_off_debug = off_button.get_rect()  # button off du mode debug
rect_off_debug.x, rect_off_debug.y = 653, 343

# Image menu / icons / Buttons (menu info)
img_back_info = pygame.image.load("img/menu_info.png").convert_alpha()
rect_back_info = img_back_info.get_rect()

# Image menu / icons / Buttons (menu pause)
img_back_pause = pygame.image.load("img/menu_pause.png").convert_alpha()
rect_back_pause = img_back_pause.get_rect()

resume_button = pygame.image.load("img/icon/reprendre.png").convert_alpha()
rect_resume = resume_button.get_rect()
rect_resume.x, rect_resume.y = 428, 220  # place l'image sur l'écran

menu_button = pygame.image.load("img/icon/menu_button.png").convert_alpha()
rect_menu = menu_button.get_rect()
rect_menu.x, rect_menu.y = 428, 300  # place l'image sur l'écran

leave_button_pause = pygame.image.load("img/icon/quitter.png").convert_alpha()
rect_leave_button = leave_button_pause.get_rect()
rect_leave_button.x, rect_leave_button.y = 428, 380  # place l'image sur l'écran

setting_button2 = pygame.image.load("img/icon/gear2.png").convert_alpha()
rect_setting2 = setting_button2.get_rect()
rect_setting2.x, rect_setting2.y = 400, 434  # place l'image sur l'écran

rect_close2 = close_button.get_rect()
rect_close2.x, rect_close2.y = 670, 73  # place l'image sur l'écran

# Image menu / icons / Buttons (menu fin)
img_back_fin = pygame.image.load("img/menu_fin.png").convert_alpha()
rect_back_fin = img_back_fin.get_rect()

replay_button = pygame.image.load("img/icon/rejouer.png").convert_alpha()
rect_replay = replay_button.get_rect()
rect_replay.x, rect_replay.y = 37, 284  # place l'image sur l'écran

menu_button2 = pygame.image.load("img/icon/menu_button2.png").convert_alpha()
rect_menu2 = menu_button2.get_rect()
rect_menu2.x, rect_menu2.y = 402, 500  # place l'image sur l'écran

rect_leave_button2 = leave_button.get_rect()
rect_leave_button2.x, rect_leave_button2.y = 767, 284  # place l'image sur l'écran

# Image menu / icons / Buttons (menu fin)
img_back_shop = pygame.image.load("img/menu_shop.png").convert_alpha()
rect_back_shop = img_back_shop.get_rect()

rect_close3 = close_button.get_rect()
rect_close3.x, rect_close3.y = 720, 170  # place l'image sur l'écran

# Variable menu option
music_on = 1 #variable musique activer au début du jeu
debug_on = 0 #variable mode debug désactiver au debut du jeu

#-------------------------------------------------------------------------------------------------------------#

def option_menu():
    """
        Procédure du menu principale, appelé en premier lors du lancement du jeu
    """
    global menu, rectangle, rectangle_large, nbcurseur, on_button, off_button, music_on, debug_on
    in_option = 1 #variable de la boucle en dessous
    while in_option:
        pointer() #appele la procédure du changement de pointeur de souris
        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                in_option = 0  # On arrête la boucle
                menu = 0 #termine la boucle menu
            if event.type == KEYDOWN:  # si une touche pressé
                if event.key == K_ESCAPE:  # si touche echap pressé
                    in_option = 0  # On arrête la boucle
            if event.type == pygame.MOUSEBUTTONDOWN:  # si click souris pressé
                if rect_on_son.collidepoint(event.pos): #si button "son on" clické
                    music_on = not music_on #music_on reçois sont inverse quand clické
                    if music_on: #si musique activer
                        pygame.mixer.music.play(-1, 0.0, 0)
                        pygame.mixer.music.set_volume(100)
                        on_button = pygame.image.load("img/icon/on.png").convert_alpha() #affiche image bonton "on"
                        print('musique :', music_on) #print dans la console (sert a rien)
                    else:
                        pygame.mixer.music.set_volume(0)
                        on_button = pygame.image.load("img/icon/off.png").convert_alpha() #afffiche image button "off"
                        print('musique :', music_on) #print dans la console (sert a rien)
                if rect_off_debug.collidepoint(event.pos): #si button "debug off" clické
                    debug_on = not debug_on #mode debug reçoit sont inverse quand clické
                    if debug_on: #si debug activé
                        off_button = pygame.image.load("img/icon/on.png").convert_alpha() #reçoit button "on"
                        rectangle = pygame.image.load("img/colide/colision_debug.png") #reçoit image du mode debug
                        rectangle_large = pygame.image.load("img/colide/colision_large_debug.png")
                        print('debug :', debug_on) #print dans la console (sert a rien)
                    else:
                        off_button = pygame.image.load("img/icon/off.png").convert_alpha() #reçoit button "off"
                        rectangle = pygame.image.load("img/colide/colision.png") #reçoit image normal
                        rectangle_large = pygame.image.load("img/colide/colision_large.png") 
                        print('debug :', debug_on) #print dans la console (sert a rien)
                if rect_close.collidepoint(event.pos): #si croix clické
                    in_option = 0 #ferme la boucle option
        if rect_close.collidepoint(pygame.mouse.get_pos()) or rect_on_son.collidepoint(
                pygame.mouse.get_pos()) or rect_off_son.collidepoint(
                pygame.mouse.get_pos()) or rect_on_debug.collidepoint(
                pygame.mouse.get_pos()) or rect_off_debug.collidepoint(pygame.mouse.get_pos()):
                #si souris survole croix, button on-off son et debug
            nbcurseur = "img/icon/curseur2.png"  # affiche le curseur 2, la main
        else:  # sinon, laisse le curseur 1
            nbcurseur = "img/icon/curseur1.png"
        fenetre.blit(img_back_option, rect_back_option)
        fenetre.blit(close_button, rect_close)
        fenetre.blit(on_button, rect_on_son)
        fenetre.blit(off_button, rect_off_debug)

#-------------------------------------------------------------------------------------------------------------#

def pointer():
    """
        procédure qui place une image de curseur sur celui de base en temps réel
    """
    curseur = pygame.image.load(
        nbcurseur).convert_alpha()  # "convert_alpha()" permet d'importer l'image avec sa transparence (png)
    curseur_rect = curseur.get_rect()
    x, y = pygame.mouse.get_pos()  # prend la position de la souris en temps réel
    curseur_rect.x, curseur_rect.y = x, y  # applique les postions de la lignes au dessus au nouveaux curseur
    fenetre.blit(curseur, curseur_rect)  # affiche le nouveau curseur
    pygame.display.flip()  # raffraichit l'écran

#-------------------------------------------------------------------------------------------------------------#

def end_menu():
    """
        Procédure du menu fin appelé en fin de partie pour ouvrir le menu "Game Over"
    """
    global nbcurseur, score1, score2
    in_end = 1
    while in_end:
        pointer()
        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                in_end = 0  # On arrête la boucle
            if event.type == KEYDOWN:  # si une touche pressé
                if event.key == K_ESCAPE:  # si touche echap pressé
                    in_end = 0  # On arrête la boucle
                if event.key == K_RETURN:  # si touche echap pressé
                    in_end = 0  # On arrête la boucle
                    jouer() # On appele la procédure du jeu
            if event.type == pygame.MOUSEBUTTONDOWN:  # si click souris pressé
                if rect_leave_button2.collidepoint(event.pos):
                    in_end = 0 # On arrête la boucle
                if rect_replay.collidepoint(event.pos):
                    in_end = 0 # On arrête la boucle
                    jouer() # On appele la procédure du jeu
                if rect_menu2.collidepoint(event.pos):
                    in_end = 0 # On arrête la boucle
                    main_menu() # On appele le menu principale
        if rect_replay.collidepoint(pygame.mouse.get_pos()) or rect_leave_button2.collidepoint(
                pygame.mouse.get_pos()) or rect_menu2.collidepoint(pygame.mouse.get_pos()):
                #si curseur survole le button play, quitter ou menu principale
            nbcurseur = "img/icon/curseur2.png"  # affiche le curseur 2, la main
        else:  # sinon, laisse le curseur 1
            nbcurseur = "img/icon/curseur1.png"
        fenetre.blit(img_back_fin, rect_back_fin)
        fenetre.blit(replay_button, rect_replay)
        fenetre.blit(leave_button, rect_leave_button2)
        fenetre.blit(menu_button2, rect_menu2)
        fenetre.blit(score1, (635, 295)) # Blit score de la partie
        fenetre.blit(score2, (600, 390)) # Blit meilleur score, celui qui est sauvegardé dans un fichier txt
#-------------------------------------------------------------------------------------------------------------#

def shop_menu():
    """
        Procédure du menu shop appelé lors du click sur l'icon shop
    """
    global nbcurseur, menu
    in_shop = 1
    while in_shop:
        pointer()
        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                in_shop = 0  # On arrête la boucle
                menu = 0
            if event.type == KEYDOWN:  # si une touche pressé
                if event.key == K_ESCAPE:  # si touche echap pressé
                    in_shop = 0  # On arrête la boucle
            if event.type == pygame.MOUSEBUTTONDOWN:  # si click souris pressé
                if rect_close3.collidepoint(event.pos):
                    in_shop = 0
        if rect_close3.collidepoint(pygame.mouse.get_pos()):
            #si curseur survole le button play, quitter ou menu principale
            nbcurseur = "img/icon/curseur2.png"  # affiche le curseur 2, la main
        else:  # sinon, laisse le curseur 1
            nbcurseur = "img/icon/curseur1.png"
        fenetre.blit(img_back_shop, rect_back_shop)
        fenetre.blit(close_button, rect_close3)

#-------------------------------------------------------------------------------------------------------------#

def main_menu():
    """
        Procédure du menu principale appelé en premier lors du lancement du programme
        Peut être appellé a chaque fois que l'on veut retourner au menu
    """
    global nbcurseur, music_on, debug_on, rectangle, rectangle_large, img_back_option, menu
    pygame.mouse.set_visible(False)  # cacher la souris de base pour mettre la nouvelle (personnalisé)
    if music_on:
        pygame.mixer.music.play(-1, 0.0, 0)
    menu = 1
    while menu:
        pointer()  # appelle la fonction pour le nouveau pointeur
        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                menu = 0  # On arrête la boucle
            if event.type == KEYDOWN:  # si une touche pressé
                if event.key == K_ESCAPE:  # si touche echap pressé
                    menu = 0  # quitte le menu, ferme donc la fenêtre
            if rect_play.collidepoint(pygame.mouse.get_pos()) or rect_leave.collidepoint(
                    pygame.mouse.get_pos()) or rect_info.collidepoint(pygame.mouse.get_pos()) or rect_buy.collidepoint(
                    pygame.mouse.get_pos()) or rect_setting.collidepoint(pygame.mouse.get_pos()):
                nbcurseur = "img/icon/curseur2.png"  # affiche le curseur 2, la main
            else:  # sinon, laisse le curseur 1
                nbcurseur = "img/icon/curseur1.png"
            if event.type == pygame.MOUSEBUTTONDOWN:  # si click souris pressé
                if rect_play.collidepoint(event.pos):
                    jouer()
                    menu = 0
                if rect_leave.collidepoint(event.pos):
                    menu = 0
                if rect_info.collidepoint(event.pos):
                    #autre façons de faire un menu sans passer par une procédure
                    in_info = 1
                    while in_info:
                        pointer()
                        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
                            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                                in_info = 0  # On arrête la boucle
                                menu = 0
                            if event.type == KEYDOWN:  # si une touche pressé
                                if event.key == K_ESCAPE:  # si touche echap pressé
                                    in_info = 0  # On arrête la boucle
                            if rect_close.collidepoint(pygame.mouse.get_pos()):
                                nbcurseur = "img/icon/curseur2.png"  # affiche le curseur 2, la main
                            else:  # sinon, laisse le curseur 1
                                nbcurseur = "img/icon/curseur1.png"
                            if event.type == pygame.MOUSEBUTTONDOWN:  # si click souris pressé
                                if rect_close.collidepoint(event.pos):
                                    in_info = 0
                        fenetre.blit(img_back_info, rect_back_info)
                        fenetre.blit(close_button, rect_close)
                elif rect_setting.collidepoint(event.pos):
                    img_back_option = pygame.image.load("img/menu_option.png").convert_alpha()
                    option_menu()
                elif rect_buy.collidepoint(event.pos):
                    shop_menu()

        fenetre.blit(background_menu, rect_backmenu)  # affiche image de fond menu
        fenetre.blit(play_button, rect_play)
        fenetre.blit(leave_button, rect_leave)
        fenetre.blit(buy_button, rect_buy)
        fenetre.blit(info_button, rect_info)
        fenetre.blit(setting_button, rect_setting)

#-------------------------------------------------------------------------------------------------------------#

def jouer():
    global x_pos_sol, y_pos_sol, x_pos_obs, y_pos_obs, x_pos_cloud, y_pos_cloud, sol, obstacle1, obstacle1rect, dino, dinorect, \
        perso_liste_number, nb_obstacle, dino_jump, jump_hauteur

    #Police décriture et taille
    font = pygame.font.Font(None, 60)

    #Premier obstacle en début de partie
    obstacle1 = pygame.image.load("img/sprite/cactus1.png").convert_alpha()
    obstacle1rect = obstacle1.get_rect()

    colide_big_cactus_rect.x, colide_big_cactus_rect.y = 0, 0  # évite le bug ou la collision touche le dino dès
    # le depart

    #Def de variables
    perso_liste_number = 0
    nb_obstacle = 0
    continuer = 1
    vitesse_jeu = 5
    score = 0

    x_pos_sol = 0
    y_pos_sol = 450

    x_pos_cloud, y_pos_cloud = 1500, 200

    dinorect.x, dinorect.y = 10, 335
    x_pos_obs, y_pos_obs = 1100, 335

    JUMP_HAUTEUR = 4
    dino_jump = False
    jump_hauteur = JUMP_HAUTEUR

    #--------------------------------------------------------------#

    def background():
        """
            Procédure pour l'image du sol qui avance en arrière plan
        """
        global x_pos_sol, y_pos_sol
        image_width = sol.get_width()
        fenetre.blit(sol, (x_pos_sol, y_pos_sol)) #blit du 1er sol dès le debut
        fenetre.blit(sol, (image_width + x_pos_sol, y_pos_sol)) #blit du 2eme sol ensuite pour eviter un trou
        if x_pos_sol <= -image_width: #si le sol sort de l'écran (par la gauche)
            fenetre.blit(sol, (image_width + x_pos_sol, y_pos_sol)) #blit du suivant
            x_pos_sol = 0
        x_pos_sol -= vitesse_jeu #fait défiler le sol de droite a gauche

    #--------------------------------------------------------------#

    def cloud():
        """
            Procédure pour l'image du nuage qui avance en arrière plan
        """
        global x_pos_cloud, y_pos_obs
        image_width3 = nuage.get_width()
        fenetre.blit(nuage, nuage_rect) # blit du premier nuage du début
        if x_pos_cloud <= -image_width3: #si le nuage sort de l'écran (par la gauche)
            x_pos_cloud = random.randint(1100, 3000) # nombre aléatoire pour l'écartement entre 2 nuages
            fenetre.blit(nuage, nuage_rect)
        x_pos_cloud -= vitesse_jeu - 2 # -2 pour le faire défiler moins vite que le sol
        nuage_rect.x, nuage_rect.y = x_pos_cloud, y_pos_cloud # img nuage prend x_pos_cloud et y_pos_cloud

    #--------------------------------------------------------------#

    def jump():
        """
            Procédure pour le saut du personnage
        """
        global dino_jump, jump_hauteur, dino
        if dino_jump:
            dino = pygame.image.load("img/sprite/t-rex-jump.png").convert_alpha()
            dinorect.y -= jump_hauteur * 3 # hauteur du dino reçoit 4*3 (au debut)
            jump_hauteur -= 0.1 # puis 4 perd 0.1 par 0.1 pour faire effet de saut
        if jump_hauteur < - JUMP_HAUTEUR: #des que le perso est bien redescendu
            dinorect.y = 335 #pour bien le placer parfaitement
            dino_jump = False #arrête le saut
            jump_hauteur = JUMP_HAUTEUR # jump_hauteur reprend 4 pour le prochain saut

    #--------------------------------------------------------------#

    def obstacle():
        """
            Procédure pour afficher et faire défiler aléatoirement les obstacle (catctus et oiseau)
        """
        global x_pos_obs, y_pos_obs, obstacle1, nb_obstacle
        image_width2 = obstacle1.get_width()
        fenetre.blit(obstacle1, obstacle1rect) #blit du 1er obstacle dès le debut
        if x_pos_obs <= -image_width2: #si l'obstacle sort de l'écran (par la gauche)
            nb_obstacle = random.randint(1, 4) #prend un nombre pour l'obstacle aléatoire
            x_pos_obs = random.randint(1100, 2000) #prend un nombre pour l'écartement entre deux obstacle aléatoire
            if nb_obstacle == 1:
                obstacle1 = pygame.image.load("img/sprite/cactus1.png").convert_alpha()
                y_pos_obs = 335 #place le cactus (y)
            elif nb_obstacle == 2:
                obstacle1 = pygame.image.load("img/sprite/cactus2.png").convert_alpha()
                y_pos_obs = 370
            elif nb_obstacle == 3:
                obstacle1 = pygame.image.load("img/sprite/cactus3.png").convert_alpha()
                y_pos_obs = 335
            elif nb_obstacle == 4:
                obstacle1 = pygame.image.load("img/sprite/bird1.png").convert_alpha()
                y_pos_obs = 310 #place l'oiseau plus haut (y)
            fenetre.blit(obstacle1, obstacle1rect)
        x_pos_obs -= vitesse_jeu #fait avance l'obstacle de droite a gauche
        obstacle1rect.x, obstacle1rect.y = x_pos_obs, y_pos_obs #obstacle prend coordonnées de x_pos_obs et y_pos_obs
        if nb_obstacle == 3: #si gros cactus
            #gros rectangle de colision se palce sur l'obstacle
            colide_big_cactus_rect.x, colide_big_cactus_rect.y = obstacle1rect.centerx, obstacle1rect.y + 20 # +20 pour bien le placer
        elif nb_obstacle == 4: #si oiseau
            #rectangle de colision se palce sur l'obstacle
            colide_cactus_rect.centerx, colide_cactus_rect.y = obstacle1rect.centerx, obstacle1rect.y - 20 # -20 car l'oiseau est en hauteur
        else: #si autre obstacle
            colide_cactus_rect.centerx, colide_cactus_rect.y = obstacle1rect.centerx, obstacle1rect.y

    while continuer:
        global nbcurseur, img_back_option, score1, score2
        fenetre.fill((0, 255, 255))
        pygame.time.Clock().tick(200)  # pour ralentir la boucle de jeu (500)
        fenetre.blit(rectangle, colide_cactus_rect) #blit rectangle de colision sur cactus
        fenetre.blit(rectangle, colide_dino_rect) #blit rectangle de colision sur dino
        if nb_obstacle == 3: #si osbtacle double cactus (plus grosse colision)
            fenetre.blit(rectangle_large, colide_big_cactus_rect) #blit un plus gros rectangle sur le double cactus

        colide_dino_rect.x, colide_dino_rect.centery = dinorect.centerx, dinorect.centery

        for event in pygame.event.get():
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                continuer = 0  # On arrête la boucle
            if event.type == KEYDOWN:  # si une touche pressé
                if event.key == K_ESCAPE:  # si touche echap pressé
                    in_pause = 1
                    while in_pause:
                        pointer()
                        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
                            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                                in_pause = 0  # On arrête la boucle
                                continuer = 0
                            if event.type == KEYDOWN:  # si une touche pressé
                                if event.key == K_ESCAPE:
                                    in_pause = 0  # On arrête la boucle
                            if event.type == pygame.MOUSEBUTTONDOWN:  # si click souris pressé
                                if rect_resume.collidepoint(event.pos) or rect_close2.collidepoint(event.pos):
                                    in_pause = 0
                                if rect_menu.collidepoint(event.pos):
                                    in_pause = 0
                                    continuer = 0
                                    main_menu()
                                if rect_leave_button.collidepoint(event.pos):
                                    in_pause = 0  # On arrête la boucle
                                    continuer = 0
                                if rect_setting2.collidepoint(event.pos):
                                    img_back_option = pygame.image.load("img/menu_option2.png").convert_alpha()
                                    option_menu()
                        if rect_resume.collidepoint(pygame.mouse.get_pos()) or rect_menu.collidepoint(
                                pygame.mouse.get_pos()) or rect_leave_button.collidepoint(
                                pygame.mouse.get_pos()) or rect_setting2.collidepoint(
                                pygame.mouse.get_pos()) or rect_close2.collidepoint(pygame.mouse.get_pos()):
                            nbcurseur = "img/icon/curseur2.png"  # affiche le curseur 2, la main
                        else:  # sinon, laisse le curseur 1
                            nbcurseur = "img/icon/curseur1.png"
                        fenetre.blit(img_back_pause, rect_back_pause)
                        fenetre.blit(resume_button, rect_resume)
                        fenetre.blit(menu_button, rect_menu)
                        fenetre.blit(leave_button_pause, rect_leave_button)
                        fenetre.blit(setting_button2, rect_setting2)
                        fenetre.blit(close_button, rect_close2)

        obstacle() #appelle la procédure des obstacles 

        if colide_dino_rect.colliderect(colide_cactus_rect) or colide_dino_rect.colliderect(colide_big_cactus_rect): #si dino touche obstacle
            with open('sav.txt', 'r') as f: #ouvre le fichier "sav.txt" en mode lecture
                liste = f.read().splitlines() #liste reçoit les info du fichier
                if score > int(liste[1]): #si le score est supérieur a celui du fichier
                    sauvegarde = ['best_score', score] #la liste "sauvegarde" reçoit le score actuelle
                    with open('sav.txt', 'w') as f: #ouvre le fichier "sav.txt" en mode écriture
                        for item in sauvegarde:
                            f.write(f'{item}\n') #écrit le nouveau score
            continuer = 0 #termine la boucle du jeu
            end_menu() #ouvre le menu fin

        if dino_jump: #tant que "dino_jump" est True
            jump() #appelle la procédure du saut

        perso_liste_number += 1 # variable animation des perso et score
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            if dinorect.y < 335:  # ce if / else n'a pas de sens mais fonctionne mieux de cette façons (moins de bugs)
                pass
            else:
                #change l'image du dino coucher pour animation de marche
                if perso_liste_number % 50 == 20:
                    dinorect.y = 380 #place le dino en hauteur (y)
                    dino = pygame.image.load("img/sprite/t-rex-down.png").convert_alpha()
                if perso_liste_number % 50 == 0:
                    dinorect.y = 380
                    dino = pygame.image.load("img/sprite/t-rex-down-2.png").convert_alpha()
        elif dinorect.y >= 335:
            #change l'image du dino debout pour animation de marche
            if perso_liste_number % 50 == 20:
                dinorect.y = 335 #place le dino en hauteur (y)
                dino = pygame.image.load("img/sprite/t-rex.png")
            if perso_liste_number % 50 == 0:
                dinorect.y = 335
                dino = pygame.image.load("img/sprite/t-rex2.png")

        if nb_obstacle == 4: #si l'obstacle est l'oiseau
            #change l'image de l'oiseau pour faire une animations de vol
            if perso_liste_number % 50 == 20:
                obstacle1 = pygame.image.load("img/sprite/bird1.png").convert_alpha()
            if perso_liste_number % 50 == 0:
                obstacle1 = pygame.image.load("img/sprite/bird2.png").convert_alpha()

        if perso_liste_number % 30 == 0:
            score += 1 #augmente de 1 le score en fonction de la varible "perso_liste_number" diviser par 30

        if score % 10 == 0:
            vitesse_jeu += 0.01 #augmenter la vitesse du jeu tout les 10 de scores

        if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and not keys[pygame.K_DOWN]:
            dino_jump = True
            if dinorect.y >= 335 and music_on: #si le dino n'est pas déja en l'air et que le son est activer
                saut_sound.play() #joue le song du saut

        # score du dino
        score1 = font.render(str(score), 1, (212, 120, 0))
        fenetre.blit(score1, (920, 130))

        with open('sav.txt', 'r') as f:  #ouvre le fichier "sav.txt" en mode lecture
            liste = f.read().splitlines() #liste reçoit les info du fichier
            if score > int(liste[1]): #si le score actuelle est plus grand que le score du fichier
                score2 = font.render(str(score), 1, (212, 120, 0))
            else: #sinon prend le meilleur score écrit dans le fichier
                score2 = font.render(str(liste[1]), 1, (212, 120, 0))

        # Mot "Score" a l'écran
        txt = font.render(str("SCORE"), 1, (212, 120, 0))
        fenetre.blit(txt, (760, 130))

        background()
        cloud()
        fenetre.blit(dino, dinorect)
        pygame.display.flip()


main_menu()

pygame.quit()


#########################################
##### Copyright Kylian & Gabin 1°3 ######
#########################################