from car import Car
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
STARTING_NUMBER_OF_CARS = 20

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        # create a bunch of cars all over the board
        for _ in range(STARTING_NUMBER_OF_CARS):
            position = (random.randint(-300, 300), random.randint(-300, 300))
            car = Car(random.choice(COLORS), position)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            # if car reaches left side of screen, create new car, remove old car
            if car.xcor() < -320:
                self.all_cars.remove(car)  # if this was a serious project, these objects should be deleted, not just removed from the array
                new_car = Car(random.choice(COLORS),
                              (300, random.randint(-300, 300)))
                self.all_cars.append(new_car)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT

    def is_turtle_collision(self, turtle):
        for car in self.all_cars:
            if turtle.distance(car) <= 25:
                print("COLLISIOS")
                return True
        return False
