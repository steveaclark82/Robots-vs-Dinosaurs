from robot import Robot


class Fleet:
        

    def __init__(self):
        self.robot = []
        

    def create_fleet(self):

        robot1 = Robot('Robocop')
        robot2 = Robot('Masterblaster')
        robot3 = Robot('Destroyer')
        
        self.robot.append(robot1)
        self.robot.append(robot2)
        self.robot.append(robot3)
