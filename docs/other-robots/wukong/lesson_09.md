# Lesson 9: Tilt Control

!!! learn "In this lesson we will learn"
    - how the accelerometer measures tilt
    - how to map a number from one range to another
    - how to control the fingers by tilting the micro:bit

!!! terms "Terminology"
    - **accelerometer** – a sensor that measures movement and tilt in three directions and can recognise gestures such as shaking.
    - **milli-g** – the unit for accelerometer readings, where about 1024 milli-g equals the pull of gravity.
    - **map** – to convert a number from one range to another, such as a tilt from -1023 to 1023 into an angle from 0 to 150.

The micro:bit's **accelerometer** measures how it's tilted. When we tilt the board left and right, the x reading goes from about -1023 to 1023 **milli-g**. Our fingers need an angle from 0 to 150, so we **map** one range onto the other.

## Map the tilt to an angle

=== "Blocks"

    ![Blocks for the tilt control example](../../assets/blocks/wukong/lesson_09_tilt_control.png){ .blocks }

    Blocks used: **forever** and **pause (ms)** (Basic), **set angle to** and **angle** (Variables), **map** and **constrain** (Math), **acceleration (mg) x** (Input), **Set servo angle to** (wuKong).

=== "Python"

    ```python linenums="1"
    --8<-- "examples/other/wukong/lesson_09_tilt_control.py"
    ```

!!! primm "PRIMM"
    1. **Predict** what the hand will do as you slowly tilt the board from left to right.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    === "Blocks"

        - **forever** → runs the blocks inside again and again.
            - **set angle to map acceleration (mg) x from low -1023 high 1023 to low 0 high 150** → reads the x tilt and maps it from the range -1023 to 1023 into the range 0 to 150.
            - **set angle to constrain angle between low 0 and high 150** → keeps the angle between 0 and 150, in case the reading goes past 1023.
            - **Set 180° servo S0 angle to angle** to **Set 180° servo S7 angle to angle** (5 blocks) → set all 5 fingers to the angle.
            - **pause (ms) 50** → waits 50 milliseconds before reading the tilt again.

    === "Python"

        - **line 1** → defines the function that the forever loop repeats.
        - **line 2** → reads the x tilt and maps it from the range -1023 to 1023 into the range 0 to 150.
        - **line 3** → keeps the angle between 0 and 150, in case the reading goes past 1023.
        - **lines 4–8** → set all 5 fingers to the angle.
        - **line 9** → waits 50 milliseconds before reading the tilt again.
        - **line 10** → tells the micro:bit to run `on_forever` again and again.

!!! tip "Why constrain?"
    If we tilt or shake the board quickly, the accelerometer can read more than 1023. Then map gives an angle bigger than 150, which could strain the servo motors. **Constrain** keeps the angle inside the range we choose.

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Each exercise has starter code in Blocks and Python. Build the blocks in MakeCode, or copy the Python into MakeCode's Python view, then change it.

### Exercise 1

Does the hand open and close smoothly as you tilt? Why might it jitter? Try changing the pause and see whether it helps.

Starter code:

=== "Blocks"

    ![Blocks starter code for Exercise 1](../../assets/blocks/wukong/lesson_09_ex1_jitter.png){ .blocks }

=== "Python"

    ```python linenums="1"
    --8<-- "examples/other/wukong/lesson_09_ex1_jitter.py"
    ```

### Exercise 2

Can you control the hand by tilting forwards and backwards instead? Hint: use **acceleration (mg) y**.

Starter code:

=== "Blocks"

    ![Blocks starter code for Exercise 2](../../assets/blocks/wukong/lesson_09_ex2_tilt_y.png){ .blocks }

=== "Python"

    ```python linenums="1"
    --8<-- "examples/other/wukong/lesson_09_ex2_tilt_y.py"
    ```

### Exercise 3

Can you give each finger a different range, so the fingers curl one after another as you tilt? For example, the thumb curls over the first part of the tilt and the little finger over the last part.

Starter code:

=== "Blocks"

    ![Blocks starter code for Exercise 3](../../assets/blocks/wukong/lesson_09_ex3_wave_curl.png){ .blocks }

=== "Python"

    ```python linenums="1"
    --8<-- "examples/other/wukong/lesson_09_ex3_wave_curl.py"
    ```
