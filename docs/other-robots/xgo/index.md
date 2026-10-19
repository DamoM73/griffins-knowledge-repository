# XGO Robot Dog

The ELECFREAKS XGO Robot Kit V2 is a four-legged robot dog. Each leg has three servo motors, and a robotic arm with a gripper is mounted on its back. A micro:bit V2 plugs into a slot on the dog's head and sends commands to the dog's own control board.

Work through the lessons in order. Each lesson adds one new part of the dog.

| Lesson | What we do |
| --- | --- |
| [Lesson 1: Meet the XGO](lesson_01.md) | switch the dog on and off, charge it and set up MakeCode |
| [Lesson 2: First Program](lesson_02.md) | connect the micro:bit to the dog, make it sit and check the battery |
| [Lesson 3: Built-in Actions](lesson_03.md) | use the dog's 19 built-in actions |
| [Lesson 4: Walking and Turning](lesson_04.md) | walk, turn and step for a set time |
| [Lesson 5: Body Posture](lesson_05.md) | raise, lower and tilt the body without walking |
| [Lesson 6: Robotic Arm](lesson_06.md) | move the arm and open and close the gripper |
| [Lesson 7: Sensor-controlled Dog](lesson_07.md) | react to sound and light |
| [Lesson 8: Trembling Dog](lesson_08.md) | tremble when the temperature drops |
| [Lesson 9: Magnet-controlled Dog](lesson_09.md) | back away from a magnet |
| [Lesson 10: Compass and Treasure Hunt](lesson_10.md) | turn to face north and follow compass directions |
| [Lesson 11: Teach a Pose](lesson_11.md) | move a leg by hand, record the pose and replay it |
| [Lesson 12: Radio Remote](lesson_12.md) | drive the dog from a second micro:bit |
| [Lesson 13: Sense the Feelings](lesson_13.md) | log and graph the dog's movement data (extension) |

Lessons 8, 9, 10 and 13 are based on activities from the ELECFREAKS XGO Robot Kit wiki, written for the first XGO kit and updated here for the V2 dog.

!!! warning "Every program starts with set XGO"
    Every XGO program must start with **set XGO TX P14 RX P13** in **on start**. Without it, the dog ignores every command. Lesson 2 explains why.
