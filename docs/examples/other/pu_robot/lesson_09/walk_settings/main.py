steps = 4
speed = 5
robotPu.set_walk_speed(robotPu.MoveDirection.FORWARD, steps, speed)
basic.pause(1000)
robotPu.set_walk_speed(robotPu.MoveDirection.BACKWARD, steps, speed)
