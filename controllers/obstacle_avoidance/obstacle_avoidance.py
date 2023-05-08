"""ObstacleAvoidance controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# get the time step of the current world.
time_step = 32
MAXIMUMSPEED = 4.5
def robot_run(robot): 
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getDevice('motorname')
    #  ds = robot.getDevice('dsname')
    #  ds.enable(timestep)

    motorleft = robot.getDevice('left_motor')
    motorright = robot.getDevice('right_motor')
    
    motorleft.setPosition(float('inf'))
    motorright.setPosition(float('inf'))
    
    motorleft.setVelocity(0.0)
    motorright.setVelocity(0.0)
    
    
   # ir0 = robot.getDevice('ps0')
   # ir0.enable(TIMESTEP)
    
    pslist = []
    for ind in [0, 1, 2, 5, 6, 7]:
        sensorname = 'ps' + str(ind)
        pslist.append(robot.getDevice(sensorname))
        pslist[-1].enable(time_step)
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(time_step) != -1:
    
        speedleft = MAXIMUMSPEED
        speedright = MAXIMUMSPEED
        # Read the sensors:
        # Enter here functions to read sensor data, like:
        #  val = ds.getValue()
        for ps in pslist:
            psvalue = ps.getValue()
            if psvalue > 80:
                # turn
                speedright = -MAXIMUMSPEED
                
      

        # Process sensor data here.

        # Enter here functions to send actuator commands, like:
            #  motor.setPosition(10.0)
        motorleft.setVelocity(speedleft)
        motorright.setVelocity(speedright)

    # Enter here exit cleanup code.

if __name__ == "__main__":
     # creat the Robot instance
    my_robot = Robot()
    robot_run(my_robot)
