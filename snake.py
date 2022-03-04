from tkinter import RIGHT
from turtle import Turtle

STARTING_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[-1]
        self.last_head_pos = ()
        self.last_tail_pos = ()
        self.move_to = 0
        self.move_from = 1

    # Process of creating a segment.
    def add_segment(self, position):
        new_segment = Turtle(shape = "square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    # Three segments are created and arranged as to make the beginner snake.
    def create_snake(self):
        for start_pos in STARTING_POSITIONS:
            self.add_segment(position = start_pos)
            
    
    # The tail segment takes the previous head segment's position, the previous tail position is saved in the event of adding a segment, and the head is moved forward.
    def move(self):
        self.last_head_pos = self.segments[-1].pos()
        self.last_tail_pos = self.segments[0].pos()
        self.segments[0].goto(self.last_head_pos)
        self.segments[-1].forward(MOVE_DISTANCE)

    # After moving the order of the list needs to represent what is happening graphically.
    def reorder(self):
        self.move_to = 0
        self.move_from = 1
        for _ in range(len(self.segments) - 2):
            self.segments.insert(self.move_to, self.segments.pop(self.move_from))
            self.move_to += 1
            self.move_from +=1 

    # Adds a segment and adds it the last known tail position.
    def extend(self):
        self.add_segment(position = self.last_tail_pos)
        self.segments.insert(0, self.segments.pop(-1))


    # Following four methods change the snake head's direction.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
