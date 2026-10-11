# Lesson 13: Radio Remote

!!! learn "In this lesson we will learn"
    - how two micro:bits send messages to each other by radio
    - how to program a second micro:bit as a joystick remote control
    - how to make the robot respond to messages from the remote

!!! terms "Terminology"
    - **radio** – a way of sending and receiving messages without wires, using invisible radio waves.
    - **radio group** – a number from 0 to 255 that sets which micro:bits can hear each other's radio messages.
    - **joystick** – a stick that we push in different directions to control something, which gives a number for how far it's pushed.

The PU Robot kit comes with a remote controller shell that holds a second micro:bit V2. The two micro:bits talk to each other by **radio**. In this lesson we write two programs: one for the remote and one for the robot.

## What we need

- the PU Robot
- the remote controller shell, with a second micro:bit V2 inside it

!!! warning "Each pair needs its own radio group"
    Every micro:bit on the same **radio group** hears the same messages. If two pairs in the class use the same group, one remote will control both robots. Each pair needs a different group number, used in both programs.

## The remote

The remote reads how far the **joystick** is pushed forwards or backwards, and sends that number to the robot. The number goes from -1 to 1, with 0 in the middle.

=== "Blocks"

    ![Blocks for the remote controller](../../assets/blocks/pu-robot/lesson_13_controller.png){ .blocks }

    Blocks used: **set controller radio group**, **send value** and **read joystick value** (robot PU > Controller), **forever** and **pause (ms)** (Basic).

=== "Python"

    ```python linenums="1"
    --8<-- "examples/other/pu_robot/lesson_13/controller/main.py"
    ```

??? note "Code explanation"
    - **line 1** → sets the remote's radio group to 160 and shows the number on the display.
    - **line 3** → defines the function that the forever loop repeats.
    - **line 4** → reads how far the joystick is pushed forwards or backwards and sends that number to the robot as a speed value.
    - **line 5** → waits 50 milliseconds, so the remote sends about 20 messages a second.
    - **line 6** → tells the micro:bit to run `on_forever` again and again.

## The robot

The robot listens for speed values. Each time one arrives, an event handler decides what to do with it.

=== "Blocks"

    ![Blocks for the robot receiver](../../assets/blocks/pu-robot/lesson_13_robot.png){ .blocks }

    Blocks used: **enable remote control on group** and **on value received** (robot PU > Remote Control), **if then else** and **0 > 0** (Logic), **set robot move direction** and **stop action** (robot PU > Actions).

=== "Python"

    ```python linenums="1"
    --8<-- "examples/other/pu_robot/lesson_13/robot/main.py"
    ```

Download each program to its own micro:bit. Put one in the robot and one in the remote, then switch both on.

!!! primm "PRIMM"
    1. **Predict** what the robot will do when you push the joystick forwards, and when you let go.
    2. **Run** both programs.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → turns on remote control and sets the robot's radio group to 160.
    - **line 3** → defines a function called `on_speed_received`, which gets the speed value in `value`.
    - **line 4** → checks whether the joystick is pushed more than halfway forwards…
    - **line 5** → …and if it is, starts the robot walking forward.
    - **line 6** → otherwise…
    - **line 7** → …stops the robot.
    - **line 8** → connects `on_speed_received` to the event of a speed value arriving.

!!! tip "Putting the factory program back"
    Once we download our own program, the remote's buttons no longer do what the PU Robot's instructions say. Our teacher can put the factory program back on both micro:bits.

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Each exercise has starter code. Copy it into MakeCode's Python view, or build the same program in Blocks, then change it.

### Exercise 1

Can you change 160 to your pair's radio group in both programs, and test that your remote only controls your robot?

Starter code:

```python linenums="1"
--8<-- "examples/other/pu_robot/lesson_13/ex1_group/main.py"
```

### Exercise 2

What happens if you pull the joystick backwards? If the robot walks forward when you pull back, the joystick values are the other way around. Can you fix it?

Starter code:

```python linenums="1"
--8<-- "examples/other/pu_robot/lesson_13/ex2_reverse/main.py"
```

### Exercise 3

Can you add walking backward, and turning left and right? It should:

- walk backward when the joystick is pulled more than halfway back
- send the joystick's turn value from the remote as well
- turn left or right when the turn value is past halfway

Starter code:

```python linenums="1"
--8<-- "examples/other/pu_robot/lesson_13/ex3_full_control/main.py"
```

### Exercise 4

Can you use the remote's B1 to B4 buttons to start modes such as dance and kick? Hint: on the remote, use **initialize controller buttons** and **B1 pressed** (robot PU > Controller), and send a button value. On the robot, use **on button value received**.

Starter code:

```python linenums="1"
--8<-- "examples/other/pu_robot/lesson_13/ex4_buttons/main.py"
```
