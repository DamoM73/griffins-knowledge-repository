# XGO Blocks screenshots still to take

Save each screenshot in `docs/assets/blocks/xgo/`. Where a heading lists several names, the programs are identical, so save the same screenshot under every name.

Fastest way: paste the Python file into MakeCode's Python view (leave out the comment block at the top of an exercise starter), then switch to Blocks. Use the list to check the result.

How to read each list:

- [ ] Indented blocks go inside the block above them.
- [ ] [square brackets] are drop-down choices. (round brackets) are values we type. ⟨angle brackets⟩ are round or pointed blocks that slot into a space, such as a sensor reading or a comparison.
- [ ] A variable name in round brackets, such as (power), means the variable's own round block from Variables.
- [ ] The text after the long dash (—) is the block category (and group, for the xgo blocks).
- [ ] The xgo rotate block's words are mixed up: the drop-down after "rotated" is the axis, and the number before "axis" is the angle.
- [ ] For else if and else, select the + at the bottom of the if block.

## Lesson 2: First Program

### lesson_02_first_program.png

Code: `docs/examples/other/xgo/lesson_02_first_program.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
  - [ ] show icon [happy] — Basic

### lesson_02_sit_and_battery.png = lesson_02_ex1_no_set_xgo.png = lesson_02_ex2_stand.png = lesson_02_ex3_battery_face.png

Code: `docs/examples/other/xgo/lesson_02_sit_and_battery.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
  - [ ] show icon [happy] — Basic
- [ ] on button [A] pressed — Input
  - [ ] Execution action [Sit_down] — xgo › Basic
- [ ] on button [B] pressed — Input
  - [ ] show number (⟨get XGO's current power⟩) — Basic

## Lesson 3: Built-in Actions

### lesson_03_wave.png = lesson_03_ex1_test_actions.png

Code: `docs/examples/other/xgo/lesson_03_wave.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] on button [A] pressed — Input
  - [ ] Execution action [Wave] — xgo › Basic

### lesson_03_routine.png = lesson_03_ex2_story.png = lesson_03_ex3_icons.png

Code: `docs/examples/other/xgo/lesson_03_routine.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] on logo [pressed] — Input
  - [ ] Execution action [Stretch_oneself] — xgo › Basic
  - [ ] Execution action [Handshake] — xgo › Basic
  - [ ] restore initial action — xgo › Basic

## Lesson 4: Walking and Turning

### lesson_04_walk_forward.png = lesson_04_ex1_no_stop.png = lesson_04_ex3_square.png

Code: `docs/examples/other/xgo/lesson_04_walk_forward.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] on button [A] pressed — Input
  - [ ] move [Forward] speed (50) % — xgo › Sports
  - [ ] pause (ms) (3000) — Basic
  - [ ] move [Forward] speed (0) % — xgo › Sports

### lesson_04_turn.png

Code: `docs/examples/other/xgo/lesson_04_turn.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] on button [B] pressed — Input
  - [ ] rotate [Left], speed is (50) % — xgo › Sports
  - [ ] pause (ms) (2000) — Basic
  - [ ] rotate [Left], speed is (0) % — xgo › Sports

### lesson_04_timed_steps.png = lesson_04_ex2_step_size.png

Code: `docs/examples/other/xgo/lesson_04_timed_steps.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] on button [A] pressed — Input
  - [ ] set XGO to perform a [forward(0mm~25mm)] translational motion with a step size of (15) mm for (3) seconds — xgo › Sports

## Lesson 5: Body Posture

### lesson_05_body_height.png = lesson_05_ex3_dance.png

Code: `docs/examples/other/xgo/lesson_05_body_height.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] on button [A] pressed — Input
  - [ ] body height (20) % — xgo › Set Servo
  - [ ] pause (ms) (1000) — Basic
  - [ ] body height (100) % — xgo › Set Servo
  - [ ] pause (ms) (1000) — Basic
  - [ ] body height (50) % — xgo › Set Servo

### lesson_05_rotate_body.png = lesson_05_ex1_axes.png = lesson_05_ex2_limits.png

Code: `docs/examples/other/xgo/lesson_05_rotate_body.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] on button [A] pressed — Input
  - [ ] set XGO to be rotated [X] degrees about the (15) axis — xgo › Sports
  - [ ] pause (ms) (1000) — Basic
  - [ ] set XGO to be rotated [X] degrees about the (-15) axis — xgo › Sports
  - [ ] pause (ms) (1000) — Basic
  - [ ] set XGO to be rotated [X] degrees about the (0) axis — xgo › Sports

## Lesson 6: Robotic Arm

### lesson_06_arm_position.png = lesson_06_ex2_pick_up.png

Code: `docs/examples/other/xgo/lesson_06_arm_position.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
  - [ ] Set the state of robot arm servo as [load] — xgo › Robot Arm(V2)
- [ ] on button [A] pressed — Input
  - [ ] Set the position of the manipulator clampX (80) mm — xgo › Robot Arm(V2)
  - [ ] pause (ms) (1000) — Basic
  - [ ] Set the position of the manipulator clampZ (80) mm — xgo › Robot Arm(V2)
  - [ ] pause (ms) (1000) — Basic
  - [ ] Set the position of the manipulator clampX (20) mm — xgo › Robot Arm(V2)
  - [ ] Set the position of the manipulator clampZ (20) mm — xgo › Robot Arm(V2)

### lesson_06_gripper.png = lesson_06_ex1_clamp_range.png = lesson_06_ex3_stable.png

Code: `docs/examples/other/xgo/lesson_06_gripper.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
  - [ ] Set the state of robot arm servo as [load] — xgo › Robot Arm(V2)
- [ ] on button [A] pressed — Input
  - [ ] Set the position of the manipulator clamp (50) mm — xgo › Robot Arm(V2)
- [ ] on button [B] pressed — Input
  - [ ] Set the position of the manipulator clamp (200) mm — xgo › Robot Arm(V2)

## Lesson 7: Sensor-controlled Dog

### lesson_07_clap.png = lesson_07_ex1_clap_distance.png

Code: `docs/examples/other/xgo/lesson_07_clap.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] on [loud] sound — Input
  - [ ] Execution action [Sit_down] — xgo › Basic
  - [ ] Execution action [Stand] — xgo › Basic

### lesson_07_light_level.png = lesson_07_ex2_bedtime.png

Code: `docs/examples/other/xgo/lesson_07_light_level.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] forever — Basic
  - [ ] if ⟨⟨light level⟩ > 100⟩ then — Logic
    - [ ] move [Forward] speed (30) % — xgo › Sports
  - [ ] else
    - [ ] move [Forward] speed (0) % — xgo › Sports
  - [ ] pause (ms) (200) — Basic

## Lesson 8: Trembling Dog

### lesson_08_show_temperature.png

Code: `docs/examples/other/xgo/lesson_08_show_temperature.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] forever — Basic
  - [ ] show number (⟨temperature (°C)⟩) — Basic
  - [ ] pause (ms) (1000) — Basic

### lesson_08_tremble.png = lesson_08_ex1_threshold.png = lesson_08_ex2_lie_down.png = lesson_08_ex3_too_hot.png

Code: `docs/examples/other/xgo/lesson_08_tremble.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
  - [ ] set [cold] to (22) — Variables
- [ ] forever — Basic
  - [ ] if ⟨⟨temperature (°C)⟩ < cold⟩ then — Logic
    - [ ] repeat (5) times — Loops
      - [ ] set XGO to be rotated [Y] degrees about the (5) axis — xgo › Sports
      - [ ] pause (ms) (100) — Basic
      - [ ] set XGO to be rotated [Y] degrees about the (-5) axis — xgo › Sports
      - [ ] pause (ms) (100) — Basic
    - [ ] set XGO to be rotated [Y] degrees about the (0) axis — xgo › Sports
  - [ ] pause (ms) (1000) — Basic

## Lesson 9: Magnet-controlled Dog

### lesson_09_show_strength.png

Code: `docs/examples/other/xgo/lesson_09_show_strength.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] forever — Basic
  - [ ] show number (⟨magnetic force (µT) [strength]⟩) — Basic
  - [ ] pause (ms) (500) — Basic

### lesson_09_scared_of_magnet.png = lesson_09_ex1_baseline.png = lesson_09_ex2_follow.png = lesson_09_ex3_sides.png

Code: `docs/examples/other/xgo/lesson_09_scared_of_magnet.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] forever — Basic
  - [ ] if ⟨⟨magnetic force (µT) [strength]⟩ > 200⟩ then — Logic
    - [ ] move [Backward] speed (30) % — xgo › Sports
  - [ ] else
    - [ ] move [Forward] speed (0) % — xgo › Sports
  - [ ] pause (ms) (200) — Basic

## Lesson 10: Compass and Treasure Hunt

### lesson_10_show_heading.png

Code: `docs/examples/other/xgo/lesson_10_show_heading.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] forever — Basic
  - [ ] show number (⟨compass heading (°)⟩) — Basic
  - [ ] pause (ms) (500) — Basic

### lesson_10_face_north.png = lesson_10_ex1_face_east.png = lesson_10_ex2_shortest_turn.png = lesson_10_ex3_treasure_hunt.png

Code: `docs/examples/other/xgo/lesson_10_face_north.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
  - [ ] set [heading] to (0) — Variables
- [ ] forever — Basic
  - [ ] set [heading] to (⟨compass heading (°)⟩) — Variables
  - [ ] if ⟨⟨heading > 15⟩ and ⟨heading < 345⟩⟩ then — Logic
    - [ ] rotate [Left], speed is (20) % — xgo › Sports
    - [ ] clear screen — Basic
  - [ ] else
    - [ ] rotate [Left], speed is (0) % — xgo › Sports
    - [ ] show string ("N") — Basic
  - [ ] pause (ms) (100) — Basic

## Lesson 11: Teach a Pose

### lesson_11_teach_pose.png = lesson_11_ex1_two_legs.png = lesson_11_ex2_animation.png = lesson_11_ex3_memory.png

Code: `docs/examples/other/xgo/lesson_11_teach_pose.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
- [ ] on button [A] pressed — Input
  - [ ] set XGO [left front] leg servo [unload] — xgo › Set Servo
- [ ] on button [B] pressed — Input
  - [ ] Record the current status of the XGO as [pose1] — xgo › Set Servo
  - [ ] set XGO [left front] leg servo [load] — xgo › Set Servo
  - [ ] restore initial action — xgo › Basic
- [ ] on logo [pressed] — Input
  - [ ] Setting the XGO to [pose1] state — xgo › Set Servo

## Lesson 12: Radio Remote

### lesson_12_remote.png = lesson_12_ex3_tilt.png = lesson_12_ex4_action.png

Code: `docs/examples/other/xgo/lesson_12_remote.py`

- [ ] on start — Basic
  - [ ] radio set group (42) — Radio
- [ ] on button [A] pressed — Input
  - [ ] radio send number (1) — Radio
- [ ] on button [B] pressed — Input
  - [ ] radio send number (0) — Radio

### lesson_12_dog.png = lesson_12_ex1_group.png = lesson_12_ex2_turning.png

Code: `docs/examples/other/xgo/lesson_12_dog.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
  - [ ] radio set group (42) — Radio
- [ ] on radio received (receivedNumber) — Radio
  - [ ] if ⟨receivedNumber = 1⟩ then — Logic
    - [ ] move [Forward] speed (50) % — xgo › Sports
  - [ ] else
    - [ ] move [Forward] speed (0) % — xgo › Sports

## Lesson 13: Sense the Feelings

### lesson_13_dog_sender.png = lesson_13_ex1_speeds.png = lesson_13_ex2_actions.png = lesson_13_ex3_strength.png

Code: `docs/examples/other/xgo/lesson_13_dog_sender.py`

- [ ] on start — Basic
  - [ ] set XGO TX [P14] RX [P13] — xgo › Basic
  - [ ] radio set group (42) — Radio
- [ ] on button [A] pressed — Input
  - [ ] move [Forward] speed (50) % — xgo › Sports
- [ ] on button [B] pressed — Input
  - [ ] move [Forward] speed (0) % — xgo › Sports
- [ ] forever — Basic
  - [ ] radio send value ("x") = (⟨acceleration (mg) [x]⟩) — Radio
  - [ ] radio send value ("y") = (⟨acceleration (mg) [y]⟩) — Radio
  - [ ] radio send value ("z") = (⟨acceleration (mg) [z]⟩) — Radio
  - [ ] pause (ms) (100) — Basic

### lesson_13_receiver.png

Code: `docs/examples/other/xgo/lesson_13_receiver.py`

- [ ] on start — Basic
  - [ ] radio set group (42) — Radio
- [ ] on radio received (name) (value) — Radio
  - [ ] serial write value (name) = (value) — Advanced › Serial
