"""
    Author: Edmond Li
    
    Date: Dec 20, 2021
    
    Description: Module designed for utilities (Side Bar and Button Class)
"""

import pygame

class sideBar():
    def __init__(self, screen, x : int, y : int, colour : tuple, width : int, height : int):
        """This initializer takes a screen surface as a parameter, initializes
        the sidebar surface and rect attributes (xpos, ypos, width, height)"""

        self.window = screen

        self.colour = colour
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    def draw(self):
        """Procedural functionn which draws the sidebar surface, uses regular pygame.draw."""
        pygame.draw.rect(self.window, self.colour, (self.x, self.y, self.width, self.height), 0)


    def hide(self):
        """Function which hides the side bar (redrawing over it with a white colour; should be normalized to background colour)"""
        pygame.draw.rect(self.window, (0, 0, 0), (self.x, self.y, self.width, self.height), 0)


class Button():
    def __init__(self, screen, x : int, y : int, colour : tuple, width : int, height : int, text=""):
        """This initializer takes a screen surface as a parameter, initializes
        the button and rect attributes, along side with the colour of the button."""

        self.window = screen
        self.colour = colour
        self.text = text
    
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    def draw(self, outline=None):
        """Procedural functionn which draws the sidebar surface, uses regular pygame.draw. Takes an outline variable to cast an outline on the button
        if it's present (default to none)."""

        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(self.window, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
            
        pygame.draw.rect(self.window, self.colour, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != "":
            font = pygame.font.SysFont("comicsans", int(self.height * 1.25 / 2))
            text = font.render(self.text, 1, (0,0,0))
            self.window.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))


    def isHover(self, pos : tuple, outOfUse : bool) -> bool:
        """Boolean function onHover, is used to determine if mouse is hovering on the button region. 
        Returns True if the mouse is located within the area, else returns False"""

        # Check if button is outOfUse (is hidden)
        if (not outOfUse):
            # Pos is the mouse position or a tuple of (x,y) coordinates
            if (pos[0] > self.x and pos[0] < self.x + self.width):
                if (pos[1] > self.y and pos[1] < self.y + self.height):
                    return True
        return False


    def hide(self, outline=None):
        """This procedural function will redraw over the button, essentailly hiding it. Takes an outline if there intially was an outline on the"""
        if outline:
            pygame.draw.rect(self.window, (0, 0, 0), (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(self.window, (0, 0, 0), (self.x, self.y, self.width, self.height), 0)


    # Getters and Setters (not all used in the program)
    def getColour(self):
        """Returns the colour of the button."""
        return self.colour
    
    def getDimensions(self):
        """Returns the dimensions; width and height of the button as two seperate variables."""
        return self.height, self.width

    def getPos(self):
        """Returns the leftmost point of the button, the inital position of the button."""
        return self.x, self.y

    def setColour(self, colour : tuple):
        """Sets the new colour of the button."""
        self.colour = colour

    def setDimensions(self, dimensionX : int, dimensionY : int):
        """Sets the new dimenions as two seperate variables and not a tuple (traditional pygame format)"""
        self.width, self.height = dimensionX, dimensionY

    def setPos(self, pos : tuple):
        """Sets the new postion (top left corner) of the button to pos[0], pos[1]."""
        self.x, self.y = pos[0], pos[1]