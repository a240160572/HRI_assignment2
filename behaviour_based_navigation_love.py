import math
import random
import numpy as np
import matplotlib.pyplot as plt

print("\n"+'Braitenberg vehicles type Love selected'+"\n")
velocity_track = 0

degree = math.pi/180.0 # radians per degree

def FTarget(target_distance, target_angle):

    #do something useful here
    Ftar= - math.sin(-target_angle)
    return Ftar

def FObstacle(obs_distance, obs_angle):
    too_far=10 #cm

    if obs_distance < too_far:
        #do something useful here
        Fobs=0 # needs replacing !
    else:
        Fobs=0
    return Fobs

def FStochastic():
    """FStochastic adds noise to the turnrate force. This is just to make the simulation more realistic by adding some noie something useful here"""
    Kstoch=0.03
    
    Fstoch =Kstoch*random.randint(1,100)/100.0
    return Fstoch

def FOrienting():
    #do something useful here
    Forient=0
    return Forient

def compute_velocity(target_distance, target_angle_robot):
    
    global velocity_track
    
    max_velocity = 1.0
    max_distance = 8.0 #m
    min_distance = 3.0 #m

    if target_distance>max_distance:
        velocity = max_velocity
    else:
        velocity = np.exp(target_distance-max_distance)

    velocity_track = np.append(velocity_track,velocity)
    plt.plot(velocity_track,'-o')
    return velocity

def compute_turnrate(target_dist, target_angle, sonar_distance_left, sonar_distance_right):
    max_turnrate = 0.349 #rad/s # may need adjustment!

    delta_t = 1 # may need adjustment!
    sonar_angle_left = 30 * degree
    sonar_angle_right = -30 * degree
    
    Fobs_left = FObstacle(sonar_distance_left, sonar_angle_left)
    Fobs_right = FObstacle(sonar_distance_right, sonar_angle_right)
#    print(Fobs_left,Fobs_right)

    FTotal = FTarget(target_dist, target_angle) + \
             Fobs_left + \
             Fobs_right + \
             FOrienting() + \
             FStochastic()
             
    # turnrate: d phi(t) / dt = sum( forces ) 
    turnrate =  FTotal*delta_t
    
    #normalise turnrate value
    if turnrate>max_turnrate:
        turnrate=1.0
    else:
        turnrate=turnrate/max_turnrate

    return turnrate

if __name__=="__main__":
    pass
