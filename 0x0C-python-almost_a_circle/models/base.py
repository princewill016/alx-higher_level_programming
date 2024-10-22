#!/usr/bin/python3
"""
This module contains the Base class which serves as the foundation for all other classes in the project.
It manages the id attribute and provides visualization capabilities using Turtle graphics.
"""
import json
import os
import csv
import turtle
import random

class Base:
    """
    Base class for all other classes in the project.
    
    Attributes:
        __nb_objects (int): Private class attribute to keep track of number of objects
        id (int): Public instance attribute for identification
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # ... (previous methods remain the same) ...

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Open a window and draw all Rectangles and Squares using Turtle graphics.
        
        Args:
            list_rectangles (list): List of Rectangle instances to draw
            list_squares (list): List of Square instances to draw
        """
        # Set up the screen
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.bgcolor("white")
        
        # Create and configure the turtle
        t = turtle.Turtle()
        t.speed(2)  # Set drawing speed (1=slowest, 10=fast, 0=fastest)
        t.pensize(2)
        
        # Helper function to generate random colors
        def random_color():
            return (
                random.random(),  # Red component
                random.random(),  # Green component
                random.random()   # Blue component
            )
        
        # Helper function to draw a shape
        def draw_shape(shape, is_square=False):
            # Calculate starting position (centered)
            start_x = shape.x - 200
            start_y = shape.y - 200
            
            # Set random color
            t.fillcolor(random_color())
            t.pencolor("black")
            
            # Move to starting position
            t.penup()
            t.goto(start_x, start_y)
            t.pendown()
            
            # Start filling
            t.begin_fill()
            
            # Draw the shape
            for _ in range(4):
                if is_square:
                    t.forward(shape.size)
                else:
                    t.forward(shape.width if _ % 2 == 0 else shape.height)
                t.left(90)
            
            # End filling
            t.end_fill()
        
        # Draw all rectangles
        for rect in list_rectangles:
            draw_shape(rect)
            
        # Draw all squares
        for square in list_squares:
            draw_shape(square, is_square=True)
        
        # Hide the turtle
        t.hideturtle()
        
        # Keep the window open (close on click)
        screen.exitonclick()
