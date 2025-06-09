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
        elif left-right>0.5: #Here i tried to use this difference to keep it in Center.
            steering = 'left'
        elif right-left>0.5:
            steering = 'right'
        else:
            steering = 'straight'

# Go ahead or brake controls.
        if front<0.7:
            goahead = 'brake'
        elif front>1.5: #this change made it to change its velocity depending upon its distence of front sensor.
            if velocity<0.15:
                goahead = 'accelerate'
            else:
                goahead = 'coast'
        elif front>1:
            if velocity<0.12:
                goahead= 'accelerate'
            else:
                goahead = 'coast'
        else:
            goahead = 'coast'
        return (steering, goahead)
