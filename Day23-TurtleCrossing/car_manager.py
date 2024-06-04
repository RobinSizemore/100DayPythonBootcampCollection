from turtle import Turtle
import random

INITIAL_SPEED = 15
INCREMENT = 5
RANDOM_COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet",
                 "cyan", "magenta", "DarkOrchid", "brown", "pink", "lime", "gray"]


class CarManager(Turtle):
    def __init__(self, lane_centers):
        super().__init__()
        self.lane_centers = lane_centers
        self.cars = []
        self.speed = INITIAL_SPEED

    def player_hit(self):
        pass

    def run(self, turtle_location):
        collision = False
        for i in range(len(self.cars) - 1, -1, -1):  # Iterate in reverse order
            car = self.cars[i]
            car.forward(self.speed)

            # Check whether this car hit the turtle.
            if turtle_location:
                if car.distance(turtle_location) <= 10:
                    collision = True

            # If the car has reached the far side of the screen
            if car.xcor() < -320:
                car.clear()  # Remove the car from the screen
                self.cars.pop(i)  # Remove the car from the list

        if random.randint(0, 20) > 10:
            ycor = random.choice(self.lane_centers)
            new_car = Turtle("square")
            new_car.turtlesize(stretch_len=2.0, stretch_wid=1)
            new_car.setheading(180)
            new_car.color(random.choice(RANDOM_COLORS))
            new_car.teleport(300, ycor)
            new_car.penup()
            self.cars.append(new_car)

        return collision

    def speed_up(self):
        self.speed += INCREMENT

    def reset(self):
        self.speed = INITIAL_SPEED

