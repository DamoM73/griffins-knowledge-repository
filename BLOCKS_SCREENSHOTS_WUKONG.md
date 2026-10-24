# WuKong Blocks screenshots still to take

Save each screenshot in `docs/assets/blocks/wukong/`. Where a heading lists several names, the programs are identical, so save the same screenshot under every name.

Fastest way: paste the Python file into MakeCode's Python view (leave out the comment block at the top of an exercise starter), then switch to Blocks. Use the list to check the result.

How to read each list:

- [ ] Indented blocks go inside the block above them.
- [ ] [square brackets] are drop-down choices. (round brackets) are values we type. ⟨angle brackets⟩ are round or pointed blocks that slot into a space, such as a sensor reading or a comparison.
- [ ] A variable name in round brackets, such as (angle), means the variable's own round block from Variables.
- [ ] The text after the long dash (—) is the block category (and group, for the wuKong blocks).
- [ ] To make a function, select Advanced, then Functions, then Make a Function. Its call block appears in Functions once the function exists.
- [ ] For else if and else, select the + at the bottom of the if block.

## Lesson 2: Zero the Servos

### lesson_02_zero_servos.png

Code: `docs/examples/other/wukong/lesson_02_zero_servos.py`

- [ ] on start — Basic
  - [ ] Set [180°] servo [S0] angle to (0) — wuKong
  - [ ] Set [180°] servo [S1] angle to (0) — wuKong
  - [ ] Set [180°] servo [S2] angle to (0) — wuKong
  - [ ] Set [180°] servo [S3] angle to (0) — wuKong
  - [ ] Set [180°] servo [S4] angle to (0) — wuKong
  - [ ] Set [180°] servo [S5] angle to (0) — wuKong
  - [ ] Set [180°] servo [S6] angle to (0) — wuKong
  - [ ] Set [180°] servo [S7] angle to (0) — wuKong
  - [ ] show icon [happy] — Basic

### lesson_02_test_thumb.png = lesson_02_ex1_my_thumb.png = lesson_02_ex2_each_finger.png

Code: `docs/examples/other/wukong/lesson_02_test_thumb.py`

- [ ] on start — Basic
  - [ ] Set [180°] servo [S0] angle to (0) — wuKong
- [ ] on button [A] pressed — Input
  - [ ] Set [180°] servo [S0] angle to (90) — wuKong
- [ ] on button [B] pressed — Input
  - [ ] Set [180°] servo [S0] angle to (0) — wuKong

## Lesson 4: Finger Range

### lesson_04_finger_range.png = lesson_04_ex1_record_range.png = lesson_04_ex2_smaller_steps.png = lesson_04_ex3_no_limits.png

Code: `docs/examples/other/wukong/lesson_04_finger_range.py`

- [ ] on start — Basic
  - [ ] set [angle] to (0) — Variables
  - [ ] Set [180°] servo [S0] angle to (angle) — wuKong
- [ ] on button [A] pressed — Input
  - [ ] if ⟨angle < 180⟩ then — Logic
    - [ ] change [angle] by (10) — Variables
  - [ ] Set [180°] servo [S0] angle to (angle) — wuKong
  - [ ] show number (angle) — Basic
- [ ] on button [B] pressed — Input
  - [ ] if ⟨angle > 0⟩ then — Logic
    - [ ] change [angle] by (-10) — Variables
  - [ ] Set [180°] servo [S0] angle to (angle) — wuKong
  - [ ] show number (angle) — Basic

## Lesson 5: Count to Five

### lesson_05_count.png = lesson_05_ex1_count_to_five.png = lesson_05_ex2_count_open.png = lesson_05_ex3_breathing_light.png

Code: `docs/examples/other/wukong/lesson_05_count.py`

- [ ] on button [A] pressed — Input
  - [ ] show number (1) — Basic
  - [ ] Set [180°] servo [S0] angle to (150) — wuKong
  - [ ] pause (ms) (1000) — Basic
  - [ ] show number (2) — Basic
  - [ ] Set [180°] servo [S1] angle to (150) — wuKong
  - [ ] pause (ms) (1000) — Basic
  - [ ] show number (3) — Basic
  - [ ] Set [180°] servo [S3] angle to (150) — wuKong
  - [ ] pause (ms) (1000) — Basic
- [ ] on button [B] pressed — Input
  - [ ] Set [180°] servo [S0] angle to (0) — wuKong
  - [ ] Set [180°] servo [S1] angle to (0) — wuKong
  - [ ] Set [180°] servo [S3] angle to (0) — wuKong
  - [ ] clear screen — Basic

## Lesson 6: Hand Gestures

### lesson_06_gestures.png = lesson_06_ex1_more_gestures.png = lesson_06_ex2_change_angle.png

Code: `docs/examples/other/wukong/lesson_06_gestures.py`

- [ ] function make_fist — Functions
  - [ ] Set [180°] servo [S0] angle to (150) — wuKong
  - [ ] Set [180°] servo [S1] angle to (150) — wuKong
  - [ ] Set [180°] servo [S3] angle to (150) — wuKong
  - [ ] Set [180°] servo [S5] angle to (150) — wuKong
  - [ ] Set [180°] servo [S7] angle to (150) — wuKong
- [ ] function open_hand — Functions
  - [ ] Set [180°] servo [S0] angle to (0) — wuKong
  - [ ] Set [180°] servo [S1] angle to (0) — wuKong
  - [ ] Set [180°] servo [S3] angle to (0) — wuKong
  - [ ] Set [180°] servo [S5] angle to (0) — wuKong
  - [ ] Set [180°] servo [S7] angle to (0) — wuKong
- [ ] on button [A] pressed — Input
  - [ ] call make_fist — Functions
- [ ] on button [B] pressed — Input
  - [ ] call open_hand — Functions

## Lesson 7: Rock, Paper, Scissors

### lesson_07_rock_paper_scissors.png = lesson_07_ex1_icons.png = lesson_07_ex2_tally.png = lesson_07_ex3_score.png

Code: `docs/examples/other/wukong/lesson_07_rock_paper_scissors.py`

- [ ] function rock — Functions
  - [ ] Set [180°] servo [S0] angle to (150) — wuKong
  - [ ] Set [180°] servo [S1] angle to (150) — wuKong
  - [ ] Set [180°] servo [S3] angle to (150) — wuKong
  - [ ] Set [180°] servo [S5] angle to (150) — wuKong
  - [ ] Set [180°] servo [S7] angle to (150) — wuKong
- [ ] function paper — Functions
  - [ ] Set [180°] servo [S0] angle to (0) — wuKong
  - [ ] Set [180°] servo [S1] angle to (0) — wuKong
  - [ ] Set [180°] servo [S3] angle to (0) — wuKong
  - [ ] Set [180°] servo [S5] angle to (0) — wuKong
  - [ ] Set [180°] servo [S7] angle to (0) — wuKong
- [ ] function scissors — Functions
  - [ ] Set [180°] servo [S0] angle to (150) — wuKong
  - [ ] Set [180°] servo [S1] angle to (0) — wuKong
  - [ ] Set [180°] servo [S3] angle to (0) — wuKong
  - [ ] Set [180°] servo [S5] angle to (150) — wuKong
  - [ ] Set [180°] servo [S7] angle to (150) — wuKong
- [ ] on [shake] — Input
  - [ ] set [choice] to (⟨pick random (1) to (3)⟩) — Variables
  - [ ] if ⟨choice = 1⟩ then — Logic
    - [ ] call rock — Functions
  - [ ] else if ⟨choice = 2⟩ then
    - [ ] call paper — Functions
  - [ ] else
    - [ ] call scissors — Functions

## Lesson 8: Smooth Movement

### lesson_08_smooth_curl.png = lesson_08_ex1_pause_test.png = lesson_08_ex2_step_size.png = lesson_08_ex3_slow_open.png = lesson_08_ex4_smooth_fist.png

Code: `docs/examples/other/wukong/lesson_08_smooth_curl.py`

- [ ] on button [A] pressed — Input
  - [ ] set [angle] to (0) — Variables
  - [ ] while ⟨angle ≤ 150⟩ do — Loops
    - [ ] Set [180°] servo [S1] angle to (angle) — wuKong
    - [ ] change [angle] by (5) — Variables
    - [ ] pause (ms) (20) — Basic
- [ ] on button [B] pressed — Input
  - [ ] Set [180°] servo [S1] angle to (0) — wuKong

## Lesson 9: Tilt Control

### lesson_09_tilt_control.png = lesson_09_ex1_jitter.png = lesson_09_ex2_tilt_y.png = lesson_09_ex3_wave_curl.png

Code: `docs/examples/other/wukong/lesson_09_tilt_control.py`

- [ ] forever — Basic
  - [ ] set [angle] to (⟨map (⟨acceleration (mg) [x]⟩) from low (-1023) high (1023) to low (0) high (150)⟩) — Variables
  - [ ] set [angle] to (⟨constrain (angle) between low (0) and high (150)⟩) — Variables
  - [ ] Set [180°] servo [S0] angle to (angle) — wuKong
  - [ ] Set [180°] servo [S1] angle to (angle) — wuKong
  - [ ] Set [180°] servo [S3] angle to (angle) — wuKong
  - [ ] Set [180°] servo [S5] angle to (angle) — wuKong
  - [ ] Set [180°] servo [S7] angle to (angle) — wuKong
  - [ ] pause (ms) (50) — Basic

## Lesson 10: Grip Challenge

### lesson_10_grip_test.png = lesson_10_ex1_trials.png = lesson_10_ex2_improve.png

Code: `docs/examples/other/wukong/lesson_10_grip_test.py`

- [ ] function make_fist — Functions
  - [ ] Set [180°] servo [S0] angle to (150) — wuKong
  - [ ] Set [180°] servo [S1] angle to (150) — wuKong
  - [ ] Set [180°] servo [S3] angle to (150) — wuKong
  - [ ] Set [180°] servo [S5] angle to (150) — wuKong
  - [ ] Set [180°] servo [S7] angle to (150) — wuKong
- [ ] function open_hand — Functions
  - [ ] Set [180°] servo [S0] angle to (0) — wuKong
  - [ ] Set [180°] servo [S1] angle to (0) — wuKong
  - [ ] Set [180°] servo [S3] angle to (0) — wuKong
  - [ ] Set [180°] servo [S5] angle to (0) — wuKong
  - [ ] Set [180°] servo [S7] angle to (0) — wuKong
- [ ] on button [A] pressed — Input
  - [ ] call make_fist — Functions
  - [ ] pause (ms) (5000) — Basic
  - [ ] call open_hand — Functions

## Lesson 11: Radio Remote

### lesson_11_remote.png = lesson_11_ex3_copy_tilt.png

Code: `docs/examples/other/wukong/lesson_11_remote.py`

- [ ] on start — Basic
  - [ ] radio set group (42) — Radio
- [ ] on button [A] pressed — Input
  - [ ] radio send number (1) — Radio
- [ ] on button [B] pressed — Input
  - [ ] radio send number (2) — Radio

### lesson_11_hand.png = lesson_11_ex1_group.png = lesson_11_ex2_more_gestures.png

Code: `docs/examples/other/wukong/lesson_11_hand.py`

- [ ] on start — Basic
  - [ ] radio set group (42) — Radio
- [ ] function make_fist — Functions
  - [ ] Set [180°] servo [S0] angle to (150) — wuKong
  - [ ] Set [180°] servo [S1] angle to (150) — wuKong
  - [ ] Set [180°] servo [S3] angle to (150) — wuKong
  - [ ] Set [180°] servo [S5] angle to (150) — wuKong
  - [ ] Set [180°] servo [S7] angle to (150) — wuKong
- [ ] function open_hand — Functions
  - [ ] Set [180°] servo [S0] angle to (0) — wuKong
  - [ ] Set [180°] servo [S1] angle to (0) — wuKong
  - [ ] Set [180°] servo [S3] angle to (0) — wuKong
  - [ ] Set [180°] servo [S5] angle to (0) — wuKong
  - [ ] Set [180°] servo [S7] angle to (0) — wuKong
- [ ] on radio received (receivedNumber) — Radio
  - [ ] if ⟨receivedNumber = 1⟩ then — Logic
    - [ ] call make_fist — Functions
  - [ ] else
    - [ ] call open_hand — Functions
