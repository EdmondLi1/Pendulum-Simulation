"""
    Author: Edmond Li
    
    Date: Dec 20, 2021
    
    Description: Main Program to simulate a pendulum system using damping, and real/approximations of rotational acceleration. 
    Originated due to my interest in pendulums in the SPH4U1/0 Work-Energy Unit.

    - Uses the pendulum.py module (pendulum sprite)
    - utlities.py for buttons and the sidebar
 """

import pygame
import pendulum
import ultilities

def main():
    """Mainline logic of the program."""

    # Utility Constants
    res = (720, 480)
    side_bar_colour = (0, 128, 128)
    isOn = (50, 205, 50)
    isOff = (255, 99, 71)
    button_colour = (194, 178, 128)

    # Intital Condtions
    length = 170
    angle = 45
    mass = 10
    pressStart = False
    preview = True

    # Can manually change these values (i) ADD A BUTTON LATER IN V.2
    angle_increment = 20
    length_increment = 20

    # Adjust variables for Damping and Small Angle Approximation. 
    smallAngleApproximation = False
    isDamping = True

    # Initalize the pygame module
    pygame.init()

    # Screen and background variables
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Pendulum Model")

    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    background = background.convert()

    # Sprite Elements (intialize one pendulum)
    pendulumSprite = pendulum.Pendulum(screen, length, angle, mass)

    # Reference variable for the origin (starting point of rotation)
    origin = (pendulumSprite.origin_x,  pendulumSprite.origin_y)


    # Right Side Bar
    r_side_bar = ultilities.sideBar(screen, screen.get_width() * 3 / 4, 0, side_bar_colour, screen.get_width() / 4, screen.get_height() * 1.5/ 4)

    start_button = ultilities.Button(screen, screen.get_width() * 13 / 16, 30, button_colour, 110, 30, "Start")
    add_pendulum = ultilities.Button(screen, screen.get_width() * 13 / 16, 65, button_colour, 110, 30, "Add Pendulum")
    remove_pendulum = ultilities.Button(screen, screen.get_width() * 13 / 16, 100, button_colour, 110, 30, "Remove Pendulum")

    # Left Side Bar
    l_side_bar = ultilities.sideBar(screen, 0, 0, side_bar_colour, screen.get_width() / 4, screen.get_height() * 1.5/ 4)

    damping_button = ultilities.Button(screen, screen.get_width() * 1 / 21, 45, isOn, 110, 30, "Damping")
    small_angle_approximation_button = ultilities.Button(screen, screen.get_width() * 1 / 21, 80, isOff, 110, 30, "Small Angle Approx")
    # additional_button = ultilities.Button(screen, screen.get_width() * 13 / 16, 105, (0, 200, 0), 100, 30, "Remove Pendulum")

    allButtons = [start_button, add_pendulum, remove_pendulum, damping_button, small_angle_approximation_button]
    pendulumList = [pendulumSprite]

    allSprites = pygame.sprite.OrderedUpdates(elm for elm in pendulumList)

    # Main simulation Loop variable
    clock = pygame.time.Clock() 
    keepGoing = True

    while keepGoing:

        clock.tick(100)

        # SIDE_BAR interface (before simulation starts; pressedStart = False)
        if not pressStart:
            l_side_bar.draw()
            r_side_bar.draw()

            # Changing the colour of damping and small angle approx. Button (Green - ON, Red - OFF)
            colour_db = isOn if isDamping else isOff
            damping_button.setColour(colour_db) 

            colour_saa = isOn if smallAngleApproximation else isOff
            small_angle_approximation_button.setColour(colour_saa) 

            # Draw the buttons
            for button in allButtons:
                button.draw()

        # E - Event Handling
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            # IF User has Quit.
            if event.type == pygame.QUIT:
                keepGoing = False
            
            # If the user pressed down the mouse (left-click)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.isHover(pos, pressStart):
                    pressStart = True
                    preview = False
                    for button in allButtons:
                        button.hide()

                elif add_pendulum.isHover(pos, pressStart):
                    # length += 20
                    angle += angle_increment
                    pendulumList.append(pendulum.Pendulum(screen, length, angle, mass))
                    allSprites = pygame.sprite.OrderedUpdates(elm for elm in pendulumList)
                
                elif remove_pendulum.isHover(pos, pressStart):
                    if len(pendulumList) != 1:
                        angle -= angle_increment
                        pendulumList.pop(len(pendulumList) - 1)
                        allSprites = pygame.sprite.OrderedUpdates(elm for elm in pendulumList)

                elif damping_button.isHover(pos, pressStart):
                    isDamping = not isDamping
                
                elif small_angle_approximation_button.isHover(pos, pressStart):
                    smallAngleApproximation = not smallAngleApproximation
                    
        # Displays the pendulum (not moving; preview, and moving; pressStart)
        if preview:
            allSprites.clear(screen, background)
            allSprites.draw(screen) 
            for sprite in pendulumList:
                pygame.draw.line(background, (0, 0, 0), origin, sprite.rect.center)
    
        elif pressStart:
            allSprites.clear(screen, background)
            allSprites.update(smallAngleApproximation, isDamping)
            allSprites.draw(screen)     
            
            for sprite in pendulumList:
                pygame.draw.line(background, (0, 0, 0), origin, sprite.rect.center)

        # Redraw all surfaces; essentially updating the canvas
        pygame.display.flip()
        screen.blit(background, (0, 0))

        for sprite in pendulumList:
            pygame.draw.line(background, (255, 255, 255), origin, sprite.rect.center)  

main()