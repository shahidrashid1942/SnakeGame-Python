from turtle import Turtle

SEGMENT_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        """
        Classs dealing with everythin snake related; from the creation to movement, to extension
        | Keeps track of snake segments and creates the initial snake
        """
        self.all_segments = []
        self.creat_snake()
        self.head = self.all_segments[0]

    def creat_snake(self):
        """
        By calling the add_segment method it creates three segments in predefined position
        | The segment_position is a pre-defined varaible
        """
        for position in SEGMENT_POSITION:
            self.add_segment(position)
        
    def add_segment(self, position):
        """
        In simple terms it adds a segment to the snake by appending the new segment to the all_segment list
        """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.all_segments.append(new_segment)

    def extend(self):
        """
        A method trigerred when the snake captures the food
        | It basically increases the all_segments list by adding a new item(segment)
        """
        self.add_segment(self.all_segments[-1].position())

    def move(self):
        """
        A method the directs the movements of the segments
        | It works by the pushing the each subsequent segment into the position of the previous segment
        | using this method whenever the snake moves, the last fragment move to the position of secondlast and so on
        | Move distance is a pre-defined variable by moving it 20 paces forward
        """
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg_num - 1].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        """
        Simple method that checks the heading of the snake and triggers the movement
        | If the snake is Down it will not move Up
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        """
        Simple method that checks the heading of the snake and triggers the movement
        | If the snake is Up it will not move Down
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        """
        Simple method that checks the heading of the snake and triggers the movement
        | If the snake is Right it will not move Left
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        """
        Simple method that checks the heading of the snake and triggers the movement
        | If the snake is Left it will not move Right
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)