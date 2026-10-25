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

## Lesson 9: Tilt Control

### lesson_09_tilt_control.png = lesson_09_ex1_jitter.png = lesson_09_ex2_tilt_y.png = lesson_09_ex3_wave_curl.png

Code: `docs/examples/other/wukong/lesson_09_tilt_control.py`

- [ ] forever — Basic
  - [ ] set [tilt_angle] to (⟨⟨rotation (°) [roll]⟩ + 90⟩) — Variables (the 0 + 0 block is in Math, and rotation (°) is in Input › more)
  - [ ] set [finger_angle] to (⟨constrain (tilt_angle) between low (0) and high (150)⟩) — Variables
  - [ ] Set [180°] servo [S0] angle to (finger_angle) — wuKong
  - [ ] Set [180°] servo [S1] angle to (finger_angle) — wuKong
  - [ ] Set [180°] servo [S3] angle to (finger_angle) — wuKong
  - [ ] Set [180°] servo [S5] angle to (finger_angle) — wuKong
  - [ ] Set [180°] servo [S7] angle to (finger_angle) — wuKong
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
