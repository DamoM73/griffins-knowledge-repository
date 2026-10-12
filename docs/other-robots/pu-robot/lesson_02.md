# Lesson 2: Remote Control Show

!!! learn "In this lesson we will learn"
    - the names of the PU Robot's main parts and what each one does
    - how servo motors let the robot move a bit like a person
    - how to drive the robot and start its actions with the remote controller

!!! terms "Terminology"
    - **degrees of freedom** – the number of separate ways a robot can move. Each servo motor adds one, so the PU Robot has six.
    - **joystick** – a stick that we push in different directions to control something, which gives a number for how far it's pushed.
    - **autonomous** – able to work by itself, without a person controlling each move.

Before we write our own programs, let's get to know the robot. In this lesson we look closely at its parts, then drive it with the remote controller and put on an imitation show.

## What we need

- a PU Robot, charged and still running its factory program
- the remote controller, with a micro:bit V2 inside it running the remote's factory program, and batteries fitted
- a clear space on the floor

!!! warning "Do this lesson before downloading our own program"
    The remote controller only works with the factory program. Once we download our own program to the robot, the remote stops working until our teacher puts the factory program back.

## Parts of the robot

The PU Robot has six servo motors: one in each leg, one in each foot, one in the neck and one in the head. Each servo motor moves one joint, so the robot has six **degrees of freedom**. Our arms and legs work the same way, with joints that bend and turn, but we have many more degrees of freedom than the robot.

<figure markdown="span">
  ![The outside parts of the PU Robot, numbered 1 to 16](../../assets/pu-robot/lesson_02_parts.png){ width="420" }
  <figcaption>The outside of the PU Robot. Image: <a href="https://wiki.elecfreaks.com/en/microbit/robot/pu-robot-kit/pu-robot-kit-case-01">ELECFREAKS</a>.</figcaption>
</figure>

| No. | Part | What it does |
| --- | --- | --- |
| 1 | head shell | holds the circuit board, battery and head servo motor, and has holes for building block pins |
| 2 | lamp holder brackets (2) | hold the lamp heads on the head shell |
| 3 | lamp heads (2) | light up in different colours |
| 4 | shoulder bracket | holds the neck servo motor and joins the neck to the chest |
| 5 | chest bracket | holds the leg servo motors and joins the shoulders to the legs |
| 6 | front cover | holds the ultrasonic sensor on the chest |
| 7 | rear cover | keeps the wires tidy, and has pin holes for the backpack and other building blocks |
| 8 | left leg bracket | holds the left foot servo motor |
| 9 | left leg cover | protects the left foot servo motor and joins the leg to the foot |
| 10 | right leg bracket | holds the right foot servo motor |
| 11 | right leg cover | protects the right foot servo motor and joins the leg to the foot |
| 12 | left foot | turned by the left foot servo motor |
| 13 | right foot | turned by the right foot servo motor |
| 14 | backpack | clips onto the rear cover and can carry small things |
| 15 | ultrasonic sensor | measures how far away things are |
| 16 | building block pin adapters (5) | join building block parts to the top of the head |

Inside the head we find the parts that control the robot.

<figure markdown="span">
  ![Inside the PU Robot's head, with parts numbered 1 to 10](../../assets/pu-robot/lesson_02_inside_parts.png){ width="420" }
  <figcaption>Inside the head, with the cover off. Image: <a href="https://wiki.elecfreaks.com/en/microbit/robot/pu-robot-kit/pu-robot-kit-case-01">ELECFREAKS</a>.</figcaption>
</figure>

| No. | Part | What it does |
| --- | --- | --- |
| 1 | head shell | holds everything inside the head |
| 2 | micro:bit | the robot's brain, which runs the program |
| 3 | head servo motor | tilts the head up and down |
| 4 | head servo bracket | holds the head servo motor in place |
| 5 | neck bracket | joins the neck and head servo motors to the head shell |
| 6 | rear cover | keeps the wires tidy |
| 7 | left leg bracket | holds the left foot servo motor |
| 8 | right leg bracket | holds the right foot servo motor |
| 9 | left foot | turned by the left foot servo motor |
| 10 | right foot | turned by the right foot servo motor |

!!! warning "Look, don't twist"
    We can look at every part, but never twist the joints by hand, especially while the robot is switched on. This damages the servo motors.

## The remote controller

The remote controller holds a second micro:bit, which sends commands to the robot by radio. We drive with the **joystick** and start actions with buttons B1 to B4. B1 makes the robot **autonomous**: it walks and explores by itself until we take control again.

<figure markdown="span">
  ![The front and back of the remote controller, with controls numbered 1 to 12](../../assets/pu-robot/lesson_02_remote.png)
  <figcaption>The front and back of the remote controller. Image: <a href="https://wiki.elecfreaks.com/en/microbit/robot/pu-robot-kit/pu-robot-kit-case-01">ELECFREAKS</a>.</figcaption>
</figure>

| No. | Control | What it does |
| --- | --- | --- |
| 1 | joystick | push forwards or backwards to walk (the further we push, the faster it goes), tilt left or right to turn (the further we tilt, the sharper the turn), tilt a long way left or right to step sideways, and press it down to rest |
| 2 | tilting the remote | while we use the joystick, tilt the whole remote forwards or backwards to nod the head, or left or right to turn the head |
| 3 | B1 | starts autonomous mode, where the robot walks and explores by itself |
| 4 | B2 | jumps |
| 5 | B3 | dances to music, with the lights changing colour on the beat |
| 6 | B4 | kicks a ball |
| 7 | micro:bit logo | touch it and the robot talks or sings, depending on what it has been doing |
| 8 | micro:bit button A | changes the radio channel up by one and shows it on the display |
| 9 | micro:bit button B | changes the radio channel down by one and shows it on the display |
| 10 | micro:bit reset button | restarts the remote and sets the channel back to 6 |
| 11 | buttons A and B together | shows the real channel number, which is the number on the display plus 160 |
| 12 | power switch | switches the remote on and off |

!!! tip "Wait for each jump and kick to finish"
    Pressing B2 or B4 again before the robot finishes the last jump or kick can make it fall over. Wait until it stands still before pressing again.

!!! warning "Each pair needs its own channel"
    If several robots and remotes in the room are on the same channel, one remote can control more than one robot. Our teacher will tell us which channel to use.

## Drive the robot

1. Put the robot on the floor and press the power button on its chin once.
    - Why: the robot needs to be on a flat surface for its calibration.
    - Result: the robot moves its joints and then stands still.
2. Switch the remote on with its power switch.
    - Result: the remote's micro:bit display shows the channel number.
3. Set the channel our teacher gave us, using buttons A and B on the remote's micro:bit.
    - Why: this stops our remote controlling another pair's robot.
4. Push the joystick gently forwards, then let go.
    - Result: the robot walks forward slowly, then stops.
5. Try each of B1 to B4, waiting for each action to finish.
    - Result: the robot explores by itself, jumps, dances and kicks.

## Imitation show

Robots like the PU Robot are designed by copying how people and animals move. Let's turn that around and see how well the robot can copy us.

1. One person does a simple move, such as walking forward three steps, nodding, looking left and right, or kicking.
2. Their partner uses the remote to make the robot copy the move.
3. Swap roles, and try a move that combines two actions, such as walking then kicking.

As we watch, think about which of the robot's servo motors move for each action, and what the robot can't copy because it doesn't have the joints.

## Exercises

### Exercise 1

Without looking at the tables, can you point to the ultrasonic sensor, the head servo motor and the lamp heads? Check each one with a partner.

### Exercise 2

Can you drive the robot across the room, turn it around, and drive it back to where it started?

### Exercise 3

Choose one move the robot copied well and one it couldn't copy. For each one, explain why, using the words servo motor and degrees of freedom.

### Exercise 4

Can you plan a 30-second show that uses walking, turning, a head movement and at least two of B1 to B4? Write the steps down in order, then perform it for the class.
