from random import choice


class RandomWalk:
    #A class to generate random walks

    def __init__(self, num_pts=5000):
        #Initialize walk attributes
        self.num_pts = num_pts

        #All walks start at the origin
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        #Calculate all of the points in a walk randomly

        #Keep taking steps until the walk reaches the desired length(num points)
        while len(self.x_values) < self.num_pts:

            #Get step in x and y directions
            x_step, y_step = self.get_step()

            #Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        # Decide which direction to go and how far in that direction
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4, 5, 6])
        x_step = x_direction * x_distance

        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4, 5, 6])
        y_step = y_direction * y_distance
        return (x_step, y_step)
