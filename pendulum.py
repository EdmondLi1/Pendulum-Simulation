"""
    Author: Edmond Li
    
    Date: Dec 20, 2021
    
    Description: Sprite class for a pendulum simulation.
"""

import pygame
import math

class Pendulum(pygame.sprite.Sprite):
    """This class defines the sprite for our Ball (pendulum)"""

    def __init__(self, screen, length, angle, mass):
        """This initializer takes a screen surface as a parameter, initializes
        the pendulum and rect attributes, and x, y direction of the pendulum."""

        self.window = screen
        # Arbitrary Constants
        self.origin_x = self.window.get_width() / 2 
        self.origin_y = self.window.get_height() / 2 - 50
        self.g = 0.10

        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Set the image and rect attributes for the Ball
        self.image = pygame.image.load("ball.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()

        angle *= math.pi / 180
        self.angle = angle
        self.length = length
        self.mass = mass

        # Centre the pendulum to X0 + LSIN(THRTA) , Y0 + LCOS(THETA)
        self.rect.center = (self.origin_x + self.length * math.sin(self.angle), self.origin_y + self.length * math.cos(self.angle))

        # Instance variables to keep track of the screen surface
        # and set the initial angular acceleration and velocity vector for the ball.
        self.angularAcceleration = 0
        self.angularVelocity = 0


    def update(self, smallAngleApproximation, isDamping):
        """This method will be called automatically to reposition the
        ball sprite on the screen."""

        # Adjust for Small angle appoximations rotationalAcc = -g/L theta vs. rotationalAcc = -g/L sin(theta)

        if smallAngleApproximation:
            self.angularAcceleration = -self.g / self.length * self.angle
        else:
            self.angularAcceleration = -self.g / self.length * math.sin(self.angle)

        self.angularVelocity += self.angularAcceleration

        if isDamping:
            self.angularVelocity *= 0.9995

        self.angle += self.angularVelocity

        self.rect.center = (self.origin_x + self.length * math.sin(self.angle), self.origin_y + self.length * math.cos(self.angle))


    # Getters and Setters
    def getLength(self):
        """Returns the length of the pendulum (string)"""
        return self.length

    def adjustLength(self, length):
        """Changes the length based on the inital length (L = L0 + Lnew)"""
        self.length += length

    def getAngle(self):
        """Returns the angle of the current state of the pendulum"""
        return self.angle            

    def adjustAngle(self, angle):
        """Adjusts the current angle of the pendulum (in radians)"""
        self.angle += angle * math.pi/180
