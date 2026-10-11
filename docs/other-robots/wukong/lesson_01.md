# Lesson 1: Build the Frame

!!! learn "In this lesson we will learn"
    - what's in the WuKong Manipulator kit
    - how to mount the servo motors and the WuKong board
    - how to plug each servo motor into a port the right way round
    - how to switch the WuKong board on, off and charge it

!!! terms "Terminology"
    - **expansion board** – a board that the micro:bit plugs into, which adds extra connections and power for motors and sensors.
    - **port** – a socket on the WuKong board that a servo motor plugs into, such as S0.

In this lesson we build the frame of the hand: the palm, the servo motors and the board. We don't fit the white servo arms or the threads yet. Those go on in Lesson 3, after Lesson 2 has set every servo motor to its starting position.

## What we need

| Part | Quantity |
| --- | --- |
| WuKong board (with built-in battery) | 1 |
| acrylic palm | 1 |
| servo motors (180°) with white servo arms | 5 |
| straws and connectors | 8 each |
| cotton thread | 1 |
| screws and screwdriver | 15 and 1 |
| beam frame 5 × 7 | 1 |

We also need a micro:bit, a micro USB data cable, scissors for the thread, and a computer with Chrome or Edge.

!!! warning "Safety and care"
    - Don't bend the fingers or turn the servo arms by hand while the board is switched on. This strains the servo motors.
    - Switch the board off before plugging in or unplugging servo cables.
    - If a servo motor buzzes and gets warm, switch the board off straight away. The thread is usually too tight.

## Mount the servo motors and board

1. Screw the 5 servo motors to the acrylic palm, one under each finger position, with the cable end of each servo motor pointing down.
    - Why: the cables then reach the board without crossing the fingers.
    - Result: all 5 servo motors are firm and don't wobble.
2. Fix the WuKong board to the bottom of the acrylic palm.
    - Why: the WuKong board is an **expansion board**. It holds the micro:bit and powers the servo motors from its battery.

![Servo motors mounted on the palm](../../assets/wukong/servos_mounted.png){ .blocks }

## Plug in the servo cables

1. Plug each servo cable into a servo **port** on the board (S0 to S7). Match the colours: brown wire to the black pin, red wire to the red pin, yellow wire to the blue pin.
    - Why: a cable plugged in the wrong way round won't move the servo motor.
    - Result: every plug has its brown wire on the black pin.
2. Trace each cable from its servo motor to the board, and record which port each finger uses in a table like this:

    | Finger | Port |
    | --- | --- |
    | thumb | |
    | index finger | |
    | middle finger | |
    | ring finger | |
    | little finger | |

    We use this table in every program. The ELECFREAKS instructions use S0, S1, S3, S5 and S7 (thumb to little finger), but any 5 ports work.

3. Insert the micro:bit into the slot on the WuKong board, with the micro:bit's logo facing the buzzer switch side of the board.
    - Result: we can see the micro:bit's display and reach buttons A and B.

![The board fitted and the servo motors connected](../../assets/wukong/board_connected.png){ .blocks }

## Power

The servo motors run from the WuKong board's battery, not the USB cable.

- **Switch on:** press the board's power switch once. The power lights turn on and show the battery level (up to 4 lights).
- **Switch off:** press the power switch twice quickly.
- **Charge:** plug a USB cable into the board's own charging port. A light flashes while it charges, and all 4 lights stay on when it's full (about 20 minutes). A full charge runs the hand for about 40 minutes.
- If the lights flash 3 times and the board switches itself off, the micro:bit isn't pushed in properly.
- Taking the micro:bit out while the board is on cuts the power to the servo motors.

## Exercises

### Exercise 1

Can you complete your port table, then check it with a partner by tracing each cable again?

### Exercise 2

Can you switch the board on, read the battery level from the lights, then switch it off? What does each number of lights tell us?
