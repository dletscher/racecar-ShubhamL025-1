import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        sensor = observations['lidar']
        velo_car = observations['velocity']

        left = sensor[0]
        midleft = sensor[1]
        front = sensor[2]
        midright = sensor[3]
        right = sensor[4]

# Controlling the Steering of the car to turn left or right.
        if right<1 or midright<1.4:
           steering='left'
        elif left<1 or midleft<1.4:
            steering = 'right'
        elif left-right>0.5:
            steering = 'left'
        elif right-left>0.5:
            steering = 'right'
        else:
            steering = 'straight'

# Go ahead or brake controls.
        if front > 0.7 and velo_car < 0.15:
            goahead = 'accelerate'
        elif front <0.6 or velo_car>0.4:
            goahead = 'coast'
        else:
            goahead = 'coast'

        return (steering, goahead)
