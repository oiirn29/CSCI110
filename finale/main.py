#-------------------------------------------------------------------------------
# Name:        python finale
# Purpose:   a simple staking game where the main object gets smaller eatch time it's not lined up right at the base 
#
# Note to John most of the knollage i use to code this project came from this youtube channel https://www.youtube.com/@CodingWithRuss  
#   also there is a posiblity the file path dosen't work i haven't tested it extensively 
# 
# Author: Joshua Mazurak
#
# Created:12/01/2024 - 12/13/2024
# Licence: CC BY
#-------------------------------------------------------------------------------



import pygame

pygame.init() #weeee py GAME

W = 600         #display settings and a function to find the center of the screen 
H = 1000
center_x = W // 2
center_y = H // 2

screen = pygame.display.set_mode((W,H))         #starts the screen and the name for it 
pygame.display.set_caption("leagly distinct rectangle game press spcae bar")

background = pygame.image.load("background\BR_gradient.png")         #loads in images for use 
play_img = pygame.image.load("sprites\PLAY.png")
quit_img = pygame.image.load("sprites\QUIT.png")
in_game_quit_img = pygame.image.load("sprites\IG_QUIT.png")



rect_x = 200        #how the main rectangle is handled and some options for diffrent play
rect_y = H - 25     #start hight of the main rect
block_speed = 4     
step_up = 1         #space between the old rect and the new one after hiting the space bar 
B_width = 150
B_hight = 20
block = []          #running list of the sizes of the perviuse blocks 


button_w = 300      #defines the buttons on the menu screen
button_h = 100

score = 0           #score track win trigger and game states 
max_score = 25
game_over = False
game_win = False
run = False
menu = True
error = False

rect = pygame.Rect(rect_x, rect_y, B_width, B_hight)            #defines all the rectangles used
start = pygame.Rect(center_x -button_w //2, center_y -button_h //2, button_w, button_h)
quit = pygame.Rect(center_x -button_w //2, center_y + button_h , button_w, button_h)
in_game_quit = pygame.Rect(center_x+225, center_y-500,75,30)

#area for glitch stuff
area_x = W
area_y = H      #glitch fix yay.... would get stuck outside the screen this checks for the rect in the screen.... still dosen't work right
window_rect = pygame.Rect(center_x - area_x//2, center_y - area_y//2, area_x, area_y)           

clock = pygame.time.Clock()         #how quick the game refeshes

high_score_file = "highscore.txt"           #name of the score file


def read_all_scores():              # Function to read all scores from the file       

    try:
        with open(high_score_file, "r") as file:            #opens/ makes the file

            scores = [line.strip().split(",") for line in file.readlines()]         

            return [(name, int(score)) for name, score in scores]
        
    except FileNotFoundError:
        return []

def save_score(name, score):        # Function to append a new score to the file

    try:

        with open(high_score_file, "a") as file:

            file.write(f"{name},{score}\n")  # Append the new score
            
    except:
        return

def get_highest_score():            # Display the highest score

    if read_all_scores():

        return max(read_all_scores(), key=lambda x: x[1])  # Get the player with the highest score
    return ("No Name", 0)

read_all_scores()           #calls all the deffs
get_highest_score()


while menu:         #menu loop

    clock.tick(60)          #updates in a sec

    for event in pygame.event.get():            #allows for quiting the game 
        if event.type == pygame.QUIT:
            menu = False
    
    mouse_pos = pygame.mouse.get_pos()          #finds the loction of the mouse cuersur for the bottons 

    if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and start.collidepoint(mouse_pos)):          #checks for play button clicked
        run = True
        menu = False

    if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and quit.collidepoint(mouse_pos)):          #checks for quit button clicked
        menu = False
        
        

    if menu:
        screen.blit(background, (0, 0))         #renders the background 
        pygame.draw.rect(screen, (100,0,0), start)          #button calls 
        pygame.draw.rect(screen, (75,0,0), quit)            #button calls 
        screen.blit(play_img, start)            #renders buttons 
        screen.blit(quit_img, quit)         #renders buttons

    font = pygame.font.Font(None, 36)       #defines the font to be use 
    high_score_name, high_score_value = get_highest_score()  # Get the highest score
    high_score_text = font.render(f"Last High Score: {high_score_name}: {high_score_value}", True, (0,0,0)) #how to render the font
    screen.blit(high_score_text, (10, 10))          #renders the font
    
    if menu:
        pygame.display.flip()           #update screen
    
    

while run:          #main game loop

    clock.tick(60)          #updates in a sec

    for event in pygame.event.get():            #allows for quiting the game 
        if event.type == pygame.QUIT:
            run = False
            save_score(player_name, score)          #saves the score 

    

        if (event.type == pygame.KEYDOWN) and not game_over:        #checks for a key in use 
            if event.key == pygame.K_SPACE:         #find the exact key

                if len(block) > 0:          #calls the string of blocks if there's any 
                    last_block = block[-1]      #takes the blcok from before the one just made and gives a var 
                    last_block_X = last_block.x     #pulls the x vall from the last block 
                    last_block_width = last_block.width         #pulls the width vall from the last block
                    overlap = max(0, min(rect.right, last_block.right) - max(rect.left, last_block.left))           #math that finds the new size based of the overlap
                    
                    if overlap > 0:     #greater the 0 continise the game and sortens the blocks total langth 
                        rect.width = overlap
                        rect.x = max(rect.x, last_block.x)
                        score += 1          #you started stackig yay
                    else:               #no overlap = woomp woomp didn't mange it did you ? 
                        game_over = True

                block.append(rect.copy())           #adds the rectand that's inuse to the string

                if not game_over:       #jumps the next block up
                    rect.y += -B_hight + -1

                if block_speed >= -1:           #adds speed to the block dependent on the direction
                    block_speed += step_up
                elif block_speed <= 1:
                    block_speed -= step_up

    rect.x += block_speed           #gives block speed

    player_name = "Player score"            #sets the name of the rec log

    screen.blit(background, (0, 0))     #draws the background
    
    if not game_over:           #creates first rectangle
        pygame.draw.rect(screen, (255, 216, 37), rect) 

    
    for placed_block in block:
        pygame.draw.rect(screen, (255, 147, 42), placed_block)             #draws placed blocks
        
    if (rect.left <= 0 or rect.right >= W) and not game_over or game_win and rect.colliderect(window_rect):    #wall boucy checks for the walls and give positive or negitive speed
        block_speed = -block_speed
    elif game_over:
        block_speed = 0 

    if not rect.colliderect(window_rect):           #error handler checks if the main rect is coliding with the invisable rect the size of the screen and yells if it's not
        game_over = True
        error = True
        font = pygame.font.Font(None, 36)
        error = font.render("Unexpected Error! Please Restart", True, (255,0,0))
        screen.blit(error, (50, 500))

 
    font = pygame.font.Font(None, 36)           #writes score in the top left of the game window
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))


    
    if game_over or score>=max_score and not error:   #end screen and gives option to restart the game 

        restart_text = font.render("Hold R to Restart", True, (0,0,0))
        screen.blit(restart_text, (W // 2 - restart_text.get_width() // 2, H // 2))


        if pygame.key.get_pressed()[pygame.K_r]:  #checks if the R key is held down and resets the game values for a new start
            save_score(player_name, score)          #saves score
            block = []
            rect.width = B_width
            rect.x = rect_x
            rect.y = rect_y
            block_speed = 4
            score = 0
            game_over = False
            game_win = False
            run = True

    mouse_pos = pygame.mouse.get_pos()          #checks mouse cursure location

    if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and in_game_quit.collidepoint(mouse_pos)):          #checks for quit button clicked and quits game
        run = False
        save_score(player_name, score)
        

    if not game_over or run:        #checks if the loop is closed before rendering to avoid consle errors
        pygame.draw.rect(screen, (0,0,0), in_game_quit)
        screen.blit(in_game_quit_img, in_game_quit)
        

    
    
        pygame.display.flip()       #screen update


pygame.quit()           #ends script 
