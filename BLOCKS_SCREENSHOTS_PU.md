# PU Robot Blocks screenshots

Build each program in MakeCode with the PU Robot extension added, switch to Blocks, and save a screenshot of just the blocks over the placeholder with the same name in `docs/assets/blocks/pu-robot/`.

Faster: paste the Python file into MakeCode's Python view and switch to Blocks. MakeCode builds the blocks for you. Use the list below to check the result.

How to read each list:

- Indented blocks go inside the block above them.
- [square brackets] are drop-down choices. (round brackets) are values we type. ⟨angle brackets⟩ are round or pointed blocks that slot into a space, such as a sensor reading or a comparison.
- A variable name in round brackets, such as (mood), means the variable's own round block from Variables.
- The text after the long dash (—) is the block category (and group, for the robot PU blocks).
- For else if and else, select the + at the bottom of the if block.
- Leave out the comment block at the top of each exercise starter.

## Lesson 3: First Program

### lesson_03_first_program.png

Example — code in `docs/examples/other/pu_robot/lesson_03/first_program/main.py`

- on start — Basic
  - set walk speed range forward (2) backward (2) — robot PU › Setup
  - show icon [happy] — Basic
  - walk [forward] for (3) steps at speed (5) — robot PU › Actions

### lesson_03_forever_loop.png

Example — code in `docs/examples/other/pu_robot/lesson_03/forever_loop/main.py`

- forever — Basic
  - show icon [happy] — Basic
  - pause (ms) (1000) — Basic
  - show icon [heart] — Basic
  - pause (ms) (1000) — Basic

### lesson_03_ex1_heart_walk.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_03/ex1_heart_walk/main.py`

- on start — Basic
  - set walk speed range forward (2) backward (2) — robot PU › Setup
  - show icon [happy] — Basic
  - walk [forward] for (3) steps at speed (5) — robot PU › Actions

### lesson_03_ex2_countdown.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_03/ex2_countdown/main.py`

- on start — Basic
  - set walk speed range forward (2) backward (2) — robot PU › Setup
  - show icon [happy] — Basic
  - walk [forward] for (3) steps at speed (5) — robot PU › Actions

### lesson_03_ex3_faces.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_03/ex3_faces/main.py`

- forever — Basic
  - show icon [happy] — Basic
  - pause (ms) (1000) — Basic
  - show icon [heart] — Basic
  - pause (ms) (1000) — Basic

## Lesson 4: Lights and Eyes

### lesson_04_ambience_light.png

Example — code in `docs/examples/other/pu_robot/lesson_04/ambience_light/main.py`

- on start — Basic
  - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
  - pause (ms) (1000) — Basic
  - set ambience light [1] to RGB (0, 0, 255) — robot PU › Actuators

### lesson_04_eyes.png

Example — code in `docs/examples/other/pu_robot/lesson_04/eyes/main.py`

- on start — Basic
  - set left eye [on] right eye [off] — robot PU › Actuators
  - pause (ms) (1000) — Basic
  - set left eye [on] right eye [on] — robot PU › Actuators
  - pause (ms) (1000) — Basic
  - set left eye brightness (10) — robot PU › Actuators

### lesson_04_repeat_flash.png

Example — code in `docs/examples/other/pu_robot/lesson_04/repeat_flash/main.py`

- on start — Basic
  - repeat (5) times — Loops
    - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
    - pause (ms) (500) — Basic
    - set ambience light [all] to RGB (0, 0, 255) — robot PU › Actuators
    - pause (ms) (500) — Basic

### lesson_04_ex1_traffic_light.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_04/ex1_traffic_light/main.py`

- on start — Basic
  - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
  - pause (ms) (1000) — Basic
  - set ambience light [1] to RGB (0, 0, 255) — robot PU › Actuators

### lesson_04_ex2_lights_off.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_04/ex2_lights_off/main.py`

- on start — Basic
  - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
  - pause (ms) (1000) — Basic
  - set ambience light [1] to RGB (0, 0, 255) — robot PU › Actuators

### lesson_04_ex3_wink.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_04/ex3_wink/main.py`

- on start — Basic
  - repeat (5) times — Loops
    - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
    - pause (ms) (500) — Basic
    - set ambience light [all] to RGB (0, 0, 255) — robot PU › Actuators
    - pause (ms) (500) — Basic

### lesson_04_ex4_fade.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_04/ex4_fade/main.py`

- on start — Basic
  - repeat (11) times — Loops
    - (leave empty: this is where the exercise adds blocks)

## Lesson 5: Built-in Modes

### lesson_05_greet.png

Example — code in `docs/examples/other/pu_robot/lesson_05/greet/main.py`

- on start — Basic
  - set mode [greet] — robot PU › Actions

### lesson_05_dance_and_stop.png

Example — code in `docs/examples/other/pu_robot/lesson_05/dance_and_stop/main.py`

- on start — Basic
  - set mode [dance] — robot PU › Actions
  - pause (ms) (10000) — Basic
  - stop action — robot PU › Actions

### lesson_05_ex1_test_modes.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_05/ex1_test_modes/main.py`

- on start — Basic
  - set mode [greet] — robot PU › Actions

### lesson_05_ex2_routine.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_05/ex2_routine/main.py`

- on start — Basic
  - set mode [dance] — robot PU › Actions
  - pause (ms) (10000) — Basic
  - stop action — robot PU › Actions

### lesson_05_ex3_change_mode.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_05/ex3_change_mode/main.py`

- on start — Basic
  - set mode [dance] — robot PU › Actions
  - pause (ms) (3000) — Basic
  - set mode [greet] — robot PU › Actions

## Lesson 6: Walking

### lesson_06_walk_steps.png

Example — code in `docs/examples/other/pu_robot/lesson_06/walk_steps/main.py`

- on start — Basic
  - walk [forward] for (5) steps at speed (5) — robot PU › Actions
  - pause (ms) (1000) — Basic
  - walk [right turn] for (4) steps at speed (5) — robot PU › Actions

### lesson_06_continuous_walk.png

Example — code in `docs/examples/other/pu_robot/lesson_06/continuous_walk/main.py`

- on start — Basic
  - set walk speed range forward (2) backward (2) — robot PU › Setup
  - set robot move direction [forward] — robot PU › Actions
  - pause (ms) (3000) — Basic
  - stop action — robot PU › Actions

### lesson_06_ex1_speed_test.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_06/ex1_speed_test/main.py`

- on start — Basic
  - walk [forward] for (5) steps at speed (2) — robot PU › Actions

### lesson_06_ex2_side_steps.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_06/ex2_side_steps/main.py`

- on start — Basic
  - walk [side left] for (5) steps at speed (5) — robot PU › Actions

### lesson_06_ex3_square.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_06/ex3_square/main.py`

- on start — Basic
  - repeat (4) times — Loops
    - (leave empty: this is where the exercise adds blocks)

### lesson_06_ex4_speed_range.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_06/ex4_speed_range/main.py`

- on start — Basic
  - set walk speed range forward (2) backward (2) — robot PU › Setup
  - set robot move direction [forward] — robot PU › Actions
  - pause (ms) (3000) — Basic
  - stop action — robot PU › Actions

## Lesson 7: Moving Joints

### lesson_07_set_servo.png

Example — code in `docs/examples/other/pu_robot/lesson_07/set_servo/main.py`

- on start — Basic
  - set [head pitch] servo to (70) — robot PU › Actions
  - pause (ms) (500) — Basic
  - set [head pitch] servo to (110) — robot PU › Actions
  - pause (ms) (500) — Basic
  - set [head pitch] servo to (90) — robot PU › Actions

### lesson_07_smooth_move.png

Example — code in `docs/examples/other/pu_robot/lesson_07/smooth_move/main.py`

- on start — Basic
  - smooth move [head offset] servo to (60) with step (2) — robot PU › Actions
  - pause (ms) (2000) — Basic
  - smooth move [head offset] servo to (120) with step (2) — robot PU › Actions
  - pause (ms) (2000) — Basic
  - smooth move [head offset] servo to (90) with step (2) — robot PU › Actions

### lesson_07_ex1_nod.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_07/ex1_nod/main.py`

- on start — Basic
  - set [head pitch] servo to (70) — robot PU › Actions
  - pause (ms) (500) — Basic
  - set [head pitch] servo to (110) — robot PU › Actions
  - pause (ms) (500) — Basic
  - set [head pitch] servo to (90) — robot PU › Actions

### lesson_07_ex2_shake.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_07/ex2_shake/main.py`

- on start — Basic
  - set [head pitch] servo to (70) — robot PU › Actions
  - pause (ms) (500) — Basic
  - set [head pitch] servo to (110) — robot PU › Actions
  - pause (ms) (500) — Basic
  - set [head pitch] servo to (90) — robot PU › Actions

### lesson_07_ex3_step_value.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_07/ex3_step_value/main.py`

- on start — Basic
  - smooth move [head offset] servo to (60) with step (2) — robot PU › Actions
  - pause (ms) (2000) — Basic
  - smooth move [head offset] servo to (120) with step (2) — robot PU › Actions
  - pause (ms) (2000) — Basic
  - smooth move [head offset] servo to (90) with step (2) — robot PU › Actions

### lesson_07_ex4_no_pauses.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_07/ex4_no_pauses/main.py`

- on start — Basic
  - smooth move [head offset] servo to (60) with step (2) — robot PU › Actions
  - pause (ms) (2000) — Basic
  - smooth move [head offset] servo to (120) with step (2) — robot PU › Actions
  - pause (ms) (2000) — Basic
  - smooth move [head offset] servo to (90) with step (2) — robot PU › Actions

## Lesson 8: Ultrasonic Sensor

### lesson_08_show_distance.png

Example — code in `docs/examples/other/pu_robot/lesson_08/show_distance/main.py`

- forever — Basic
  - show number (⟨ultrasonic sensor distance in [cm]⟩) — Basic

### lesson_08_hand_wave.png

Example — code in `docs/examples/other/pu_robot/lesson_08/hand_wave/main.py`

- forever — Basic
  - if ⟨⟨ultrasonic sensor distance in [cm]⟩ < 10⟩ then — Logic
    - set mode [greet] — robot PU › Actions
    - pause (ms) (1000) — Basic

### lesson_08_obstacle_alarm.png

Example — code in `docs/examples/other/pu_robot/lesson_08/obstacle_alarm/main.py`

- forever — Basic
  - if ⟨⟨ultrasonic sensor distance in [cm]⟩ < 15⟩ then — Logic
    - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
  - else
    - set ambience light [all] to RGB (0, 255, 0) — robot PU › Actuators

### lesson_08_ex1_accuracy.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_08/ex1_accuracy/main.py`

- forever — Basic
  - show number (⟨ultrasonic sensor distance in [cm]⟩) — Basic

### lesson_08_ex2_wave_nod.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_08/ex2_wave_nod/main.py`

- forever — Basic
  - if ⟨⟨ultrasonic sensor distance in [cm]⟩ < 10⟩ then — Logic
    - set mode [greet] — robot PU › Actions
    - pause (ms) (1000) — Basic

### lesson_08_ex3_three_colours.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_08/ex3_three_colours/main.py`

- forever — Basic
  - if ⟨⟨ultrasonic sensor distance in [cm]⟩ < 15⟩ then — Logic
    - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
  - else
    - set ambience light [all] to RGB (0, 255, 0) — robot PU › Actuators

### lesson_08_ex4_stop_at_wall.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_08/ex4_stop_at_wall/main.py`

- on start — Basic
  - set walk speed range forward (2) backward (2) — robot PU › Setup
- forever — Basic
  - (leave empty: this is where the exercise adds blocks)

## Lesson 9: Variables

### lesson_09_walk_settings.png

Example — code in `docs/examples/other/pu_robot/lesson_09/walk_settings/main.py`

- on start — Basic
  - set [steps] to (4) — Variables
  - set [speed] to (5) — Variables
  - walk [forward] for (steps) steps at speed (speed) — robot PU › Actions
  - pause (ms) (1000) — Basic
  - walk [backward] for (steps) steps at speed (speed) — robot PU › Actions

### lesson_09_count_waves.png

Example — code in `docs/examples/other/pu_robot/lesson_09/count_waves/main.py`

- on start — Basic
  - set [waves] to (0) — Variables
- forever — Basic
  - if ⟨⟨ultrasonic sensor distance in [cm]⟩ < 10⟩ then — Logic
    - change [waves] by (1) — Variables
    - show number (waves) — Basic
    - pause (ms) (1000) — Basic

### lesson_09_ex1_kicks.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_09/ex1_kicks/main.py`

- on start — Basic
  - set [kicks] to (3) — Variables

### lesson_09_ex2_settings.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_09/ex2_settings/main.py`

- on start — Basic
  - set [steps] to (4) — Variables
  - set [speed] to (5) — Variables
  - walk [forward] for (steps) steps at speed (speed) — robot PU › Actions
  - pause (ms) (1000) — Basic
  - walk [backward] for (steps) steps at speed (speed) — robot PU › Actions

### lesson_09_ex3_countdown.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_09/ex3_countdown/main.py`

- on start — Basic
  - set [waves] to (0) — Variables
- forever — Basic
  - if ⟨⟨ultrasonic sensor distance in [cm]⟩ < 10⟩ then — Logic
    - change [waves] by (1) — Variables
    - show number (waves) — Basic
    - pause (ms) (1000) — Basic

## Lesson 10: Shy PU

### lesson_10_shy_pu.png

Example — code in `docs/examples/other/pu_robot/lesson_10/shy_pu/main.py`

- on start — Basic
  - set [distance] to (0) — Variables
- forever — Basic
  - set [distance] to (⟨ultrasonic sensor distance in [cm]⟩) — Variables
  - if ⟨distance > 30⟩ then — Logic
    - set ambience light [all] to RGB (0, 255, 0) — robot PU › Actuators
    - walk [forward] for (1) steps at speed (5) — robot PU › Actions
  - else if ⟨distance > 10⟩ then
    - set ambience light [all] to RGB (255, 120, 0) — robot PU › Actuators
    - set [head offset] servo to (70) — robot PU › Actions
    - pause (ms) (300) — Basic
    - set [head offset] servo to (110) — robot PU › Actions
    - pause (ms) (300) — Basic
    - set [head offset] servo to (90) — robot PU › Actions
  - else
    - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
    - walk [backward] for (2) steps at speed (5) — robot PU › Actions

### lesson_10_ex1_zones.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_10/ex1_zones/main.py`

- on start — Basic
  - set [distance] to (0) — Variables
- forever — Basic
  - set [distance] to (⟨ultrasonic sensor distance in [cm]⟩) — Variables
  - if ⟨distance > 30⟩ then — Logic
    - set ambience light [all] to RGB (0, 255, 0) — robot PU › Actuators
    - walk [forward] for (1) steps at speed (5) — robot PU › Actions
  - else if ⟨distance > 10⟩ then
    - set ambience light [all] to RGB (255, 120, 0) — robot PU › Actuators
    - set [head offset] servo to (70) — robot PU › Actions
    - pause (ms) (300) — Basic
    - set [head offset] servo to (110) — robot PU › Actions
    - pause (ms) (300) — Basic
    - set [head offset] servo to (90) — robot PU › Actions
  - else
    - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
    - walk [backward] for (2) steps at speed (5) — robot PU › Actions

### lesson_10_ex2_eyes.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_10/ex2_eyes/main.py`

- on start — Basic
  - set [distance] to (0) — Variables
- forever — Basic
  - set [distance] to (⟨ultrasonic sensor distance in [cm]⟩) — Variables
  - if ⟨distance > 30⟩ then — Logic
    - set ambience light [all] to RGB (0, 255, 0) — robot PU › Actuators
    - walk [forward] for (1) steps at speed (5) — robot PU › Actions
  - else if ⟨distance > 10⟩ then
    - set ambience light [all] to RGB (255, 120, 0) — robot PU › Actuators
    - set [head offset] servo to (70) — robot PU › Actions
    - pause (ms) (300) — Basic
    - set [head offset] servo to (110) — robot PU › Actions
    - pause (ms) (300) — Basic
    - set [head offset] servo to (90) — robot PU › Actions
  - else
    - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
    - walk [backward] for (2) steps at speed (5) — robot PU › Actions

### lesson_10_ex3_four_zones.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_10/ex3_four_zones/main.py`

- on start — Basic
  - set [distance] to (0) — Variables
- forever — Basic
  - set [distance] to (⟨ultrasonic sensor distance in [cm]⟩) — Variables
  - if ⟨distance > 30⟩ then — Logic
    - set ambience light [all] to RGB (0, 255, 0) — robot PU › Actuators
    - walk [forward] for (1) steps at speed (5) — robot PU › Actions
  - else if ⟨distance > 10⟩ then
    - set ambience light [all] to RGB (255, 120, 0) — robot PU › Actuators
    - set [head offset] servo to (70) — robot PU › Actions
    - pause (ms) (300) — Basic
    - set [head offset] servo to (110) — robot PU › Actions
    - pause (ms) (300) — Basic
    - set [head offset] servo to (90) — robot PU › Actions
  - else
    - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
    - walk [backward] for (2) steps at speed (5) — robot PU › Actions

## Lesson 11: Balance and Sound

### lesson_11_body_pitch.png

Example — code in `docs/examples/other/pu_robot/lesson_11/body_pitch/main.py`

- forever — Basic
  - show number (⟨body pitch⟩) — Basic
  - pause (ms) (500) — Basic

### lesson_11_clap.png

Example — code in `docs/examples/other/pu_robot/lesson_11/clap/main.py`

- on [loud] sound — Input
  - set mode [jump] — robot PU › Actions

### lesson_11_music_tempo.png

Example — code in `docs/examples/other/pu_robot/lesson_11/music_tempo/main.py`

- forever — Basic
  - show number (⟨music tempo⟩) — Basic
  - pause (ms) (1000) — Basic

### lesson_11_ex1_body_roll.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_11/ex1_body_roll/main.py`

- forever — Basic
  - show number (⟨body pitch⟩) — Basic
  - pause (ms) (500) — Basic

### lesson_11_ex2_tilt_alarm.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_11/ex2_tilt_alarm/main.py`

- forever — Basic
  - show number (⟨body pitch⟩) — Basic
  - pause (ms) (500) — Basic

### lesson_11_ex3_wave_and_clap.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_11/ex3_wave_and_clap/main.py`

- on [loud] sound — Input
  - set mode [jump] — robot PU › Actions

### lesson_11_ex4_tempo_test.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_11/ex4_tempo_test/main.py`

- forever — Basic
  - show number (⟨music tempo⟩) — Basic
  - pause (ms) (1000) — Basic

## Lesson 12: Dance to the Beat

### lesson_12_beat_nod.png

Example — code in `docs/examples/other/pu_robot/lesson_12/beat_nod/main.py`

- on start — Basic
  - set tempo to (bpm) (120) — Music
  - repeat (8) times — Loops
    - set [head pitch] servo to (70) — robot PU › Actions
    - pause (ms) (⟨[1/2] beat⟩) — Basic
    - set [head pitch] servo to (110) — robot PU › Actions
    - pause (ms) (⟨[1/2] beat⟩) — Basic
  - set [head pitch] servo to (90) — robot PU › Actions

### lesson_12_dance_with_music.png

Example — code in `docs/examples/other/pu_robot/lesson_12/dance_with_music/main.py`

- on start — Basic
  - set tempo to (bpm) (120) — Music
- forever — Basic
  - if ⟨⟨ultrasonic sensor distance in [cm]⟩ < 10⟩ then — Logic
    - play ⟨melody [entertainer]⟩ [in background] — Music
    - repeat (4) times — Loops
      - set [head offset] servo to (60) — robot PU › Actions
      - pause (ms) (⟨[1] beat⟩) — Basic
      - set [head offset] servo to (120) — robot PU › Actions
      - pause (ms) (⟨[1] beat⟩) — Basic
    - set [head offset] servo to (90) — robot PU › Actions

### lesson_12_ex1_tempo.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_12/ex1_tempo/main.py`

- on start — Basic
  - set tempo to (bpm) (120) — Music
- forever — Basic
  - if ⟨⟨ultrasonic sensor distance in [cm]⟩ < 10⟩ then — Logic
    - play ⟨melody [entertainer]⟩ [in background] — Music
    - repeat (4) times — Loops
      - set [head offset] servo to (60) — robot PU › Actions
      - pause (ms) (⟨[1] beat⟩) — Basic
      - set [head offset] servo to (120) — robot PU › Actions
      - pause (ms) (⟨[1] beat⟩) — Basic
    - set [head offset] servo to (90) — robot PU › Actions

### lesson_12_ex2_beat_chart.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_12/ex2_beat_chart/main.py`

- on start — Basic
  - set tempo to (bpm) (120) — Music
  - repeat (8) times — Loops
    - set [head pitch] servo to (70) — robot PU › Actions
    - pause (ms) (⟨[1/2] beat⟩) — Basic
    - set [head pitch] servo to (110) — robot PU › Actions
    - pause (ms) (⟨[1/2] beat⟩) — Basic
  - set [head pitch] servo to (90) — robot PU › Actions

### lesson_12_ex3_my_dance.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_12/ex3_my_dance/main.py`

- on start — Basic
  - set tempo to (bpm) (120) — Music
- forever — Basic
  - if ⟨⟨ultrasonic sensor distance in [cm]⟩ < 10⟩ then — Logic
    - play ⟨melody [entertainer]⟩ [in background] — Music
    - repeat (4) times — Loops
      - set [head offset] servo to (60) — robot PU › Actions
      - pause (ms) (⟨[1] beat⟩) — Basic
      - set [head offset] servo to (120) — robot PU › Actions
      - pause (ms) (⟨[1] beat⟩) — Basic
    - set [head offset] servo to (90) — robot PU › Actions

## Lesson 13: Moods

### lesson_13_moods.png

Example — code in `docs/examples/other/pu_robot/lesson_13/moods/main.py`

- on start — Basic
  - set [mood] to (1) — Variables
  - show number (mood) — Basic
- on [loud] sound — Input
  - change [mood] by (1) — Variables
  - if ⟨mood > 3⟩ then — Logic
    - set [mood] to (1) — Variables
  - show number (mood) — Basic
- forever — Basic
  - if ⟨mood = 1⟩ then — Logic
    - set ambience light [all] to RGB (255, 200, 0) — robot PU › Actuators
    - set left eye [on] right eye [on] — robot PU › Actuators
    - set [head pitch] servo to (110) — robot PU › Actions
  - else if ⟨mood = 2⟩ then
    - set ambience light [all] to RGB (0, 0, 255) — robot PU › Actuators
    - set left eye brightness (10) — robot PU › Actuators
    - set right eye brightness (10) — robot PU › Actuators
    - set [head pitch] servo to (70) — robot PU › Actions
  - else
    - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
    - set [head offset] servo to (70) — robot PU › Actions
    - pause (ms) (150) — Basic
    - set [head offset] servo to (110) — robot PU › Actions
    - pause (ms) (150) — Basic
    - set [head offset] servo to (90) — robot PU › Actions
  - pause (ms) (500) — Basic

### lesson_13_ex1_fourth_mood.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_13/ex1_fourth_mood/main.py`

- on start — Basic
  - set [mood] to (1) — Variables
  - show number (mood) — Basic
- on [loud] sound — Input
  - change [mood] by (1) — Variables
  - if ⟨mood > 3⟩ then — Logic
    - set [mood] to (1) — Variables
  - show number (mood) — Basic
- forever — Basic
  - if ⟨mood = 1⟩ then — Logic
    - set ambience light [all] to RGB (255, 200, 0) — robot PU › Actuators
    - set left eye [on] right eye [on] — robot PU › Actuators
    - set [head pitch] servo to (110) — robot PU › Actions
  - else if ⟨mood = 2⟩ then
    - set ambience light [all] to RGB (0, 0, 255) — robot PU › Actuators
    - set left eye brightness (10) — robot PU › Actuators
    - set right eye brightness (10) — robot PU › Actuators
    - set [head pitch] servo to (70) — robot PU › Actions
  - else
    - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
    - set [head offset] servo to (70) — robot PU › Actions
    - pause (ms) (150) — Basic
    - set [head offset] servo to (110) — robot PU › Actions
    - pause (ms) (150) — Basic
    - set [head offset] servo to (90) — robot PU › Actions
  - pause (ms) (500) — Basic

### lesson_13_ex2_wave_switch.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_13/ex2_wave_switch/main.py`

- on start — Basic
  - set [mood] to (1) — Variables
  - show number (mood) — Basic
- on [loud] sound — Input
  - change [mood] by (1) — Variables
  - if ⟨mood > 3⟩ then — Logic
    - set [mood] to (1) — Variables
  - show number (mood) — Basic
- forever — Basic
  - if ⟨mood = 1⟩ then — Logic
    - set ambience light [all] to RGB (255, 200, 0) — robot PU › Actuators
    - set left eye [on] right eye [on] — robot PU › Actuators
    - set [head pitch] servo to (110) — robot PU › Actions
  - else if ⟨mood = 2⟩ then
    - set ambience light [all] to RGB (0, 0, 255) — robot PU › Actuators
    - set left eye brightness (10) — robot PU › Actuators
    - set right eye brightness (10) — robot PU › Actuators
    - set [head pitch] servo to (70) — robot PU › Actions
  - else
    - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
    - set [head offset] servo to (70) — robot PU › Actions
    - pause (ms) (150) — Basic
    - set [head offset] servo to (110) — robot PU › Actions
    - pause (ms) (150) — Basic
    - set [head offset] servo to (90) — robot PU › Actions
  - pause (ms) (500) — Basic

### lesson_13_ex3_mood_sounds.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_13/ex3_mood_sounds/main.py`

- on start — Basic
  - set [mood] to (1) — Variables
  - show number (mood) — Basic
- on [loud] sound — Input
  - change [mood] by (1) — Variables
  - if ⟨mood > 3⟩ then — Logic
    - set [mood] to (1) — Variables
  - show number (mood) — Basic
- forever — Basic
  - if ⟨mood = 1⟩ then — Logic
    - set ambience light [all] to RGB (255, 200, 0) — robot PU › Actuators
    - set left eye [on] right eye [on] — robot PU › Actuators
    - set [head pitch] servo to (110) — robot PU › Actions
  - else if ⟨mood = 2⟩ then
    - set ambience light [all] to RGB (0, 0, 255) — robot PU › Actuators
    - set left eye brightness (10) — robot PU › Actuators
    - set right eye brightness (10) — robot PU › Actuators
    - set [head pitch] servo to (70) — robot PU › Actions
  - else
    - set ambience light [all] to RGB (255, 0, 0) — robot PU › Actuators
    - set [head offset] servo to (70) — robot PU › Actions
    - pause (ms) (150) — Basic
    - set [head offset] servo to (110) — robot PU › Actions
    - pause (ms) (150) — Basic
    - set [head offset] servo to (90) — robot PU › Actions
  - pause (ms) (500) — Basic

## Lesson 14: Radio Remote

### lesson_14_controller.png

Example — code in `docs/examples/other/pu_robot/lesson_14/controller/main.py`

- on start — Basic
  - set controller radio group (160) — robot PU › Controller
- forever — Basic
  - send [speed] value (⟨read joystick value [speed]⟩) — robot PU › Controller
  - pause (ms) (50) — Basic

### lesson_14_robot.png

Example — code in `docs/examples/other/pu_robot/lesson_14/robot/main.py`

- on start — Basic
  - enable remote control on group (160) — robot PU › Receiver
- on [speed] value received (value) — robot PU › Receiver
  - if ⟨value > 0.5⟩ then — Logic
    - set robot move direction [forward] — robot PU › Actions
  - else
    - stop action — robot PU › Actions

### lesson_14_ex1_group.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_14/ex1_group/main.py`

- on start — Basic
  - enable remote control on group (160) — robot PU › Receiver
- on [speed] value received (value) — robot PU › Receiver
  - if ⟨value > 0.5⟩ then — Logic
    - set robot move direction [forward] — robot PU › Actions
  - else
    - stop action — robot PU › Actions

### lesson_14_ex2_reverse.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_14/ex2_reverse/main.py`

- on start — Basic
  - enable remote control on group (160) — robot PU › Receiver
- on [speed] value received (value) — robot PU › Receiver
  - if ⟨value > 0.5⟩ then — Logic
    - set robot move direction [forward] — robot PU › Actions
  - else
    - stop action — robot PU › Actions

### lesson_14_ex3_full_control.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_14/ex3_full_control/main.py`

- on start — Basic
  - enable remote control on group (160) — robot PU › Receiver
- on [speed] value received (value) — robot PU › Receiver
  - if ⟨value > 0.5⟩ then — Logic
    - set robot move direction [forward] — robot PU › Actions
  - else
    - stop action — robot PU › Actions

### lesson_14_ex4_buttons.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_14/ex4_buttons/main.py`

- on start — Basic
  - set controller radio group (160) — robot PU › Controller
- forever — Basic
  - send [speed] value (⟨read joystick value [speed]⟩) — robot PU › Controller
  - pause (ms) (50) — Basic

## Lesson 15: Parking Challenge

### lesson_15_park.png

Example — code in `docs/examples/other/pu_robot/lesson_15/park/main.py`

- on start — Basic
  - set [stop_distance] to (15) — Variables
- forever — Basic
  - if ⟨⟨ultrasonic sensor distance in [cm]⟩ > stop_distance⟩ then — Logic
    - walk [forward] for (1) steps at speed (4) — robot PU › Actions
  - else
    - show icon [yes] — Basic

### lesson_15_slow_down.png

Example — code in `docs/examples/other/pu_robot/lesson_15/slow_down/main.py`

- on start — Basic
  - set [distance] to (0) — Variables
  - set [slow_distance] to (30) — Variables
  - set [stop_distance] to (8) — Variables
- forever — Basic
  - set [distance] to (⟨ultrasonic sensor distance in [cm]⟩) — Variables
  - if ⟨distance > slow_distance⟩ then — Logic
    - walk [forward] for (1) steps at speed (6) — robot PU › Actions
  - else if ⟨distance > stop_distance⟩ then
    - walk [forward] for (1) steps at speed (2) — robot PU › Actions
  - else
    - show icon [yes] — Basic

### lesson_15_ex1_tune.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_15/ex1_tune/main.py`

- on start — Basic
  - set [distance] to (0) — Variables
  - set [slow_distance] to (30) — Variables
  - set [stop_distance] to (8) — Variables
- forever — Basic
  - set [distance] to (⟨ultrasonic sensor distance in [cm]⟩) — Variables
  - if ⟨distance > slow_distance⟩ then — Logic
    - walk [forward] for (1) steps at speed (6) — robot PU › Actions
  - else if ⟨distance > stop_distance⟩ then
    - walk [forward] for (1) steps at speed (2) — robot PU › Actions
  - else
    - show icon [yes] — Basic

### lesson_15_ex2_lights.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_15/ex2_lights/main.py`

- on start — Basic
  - set [distance] to (0) — Variables
  - set [slow_distance] to (30) — Variables
  - set [stop_distance] to (8) — Variables
- forever — Basic
  - set [distance] to (⟨ultrasonic sensor distance in [cm]⟩) — Variables
  - if ⟨distance > slow_distance⟩ then — Logic
    - walk [forward] for (1) steps at speed (6) — robot PU › Actions
  - else if ⟨distance > stop_distance⟩ then
    - walk [forward] for (1) steps at speed (2) — robot PU › Actions
  - else
    - show icon [yes] — Basic

### lesson_15_ex3_reverse.png

Exercise starter — code in `docs/examples/other/pu_robot/lesson_15/ex3_reverse/main.py`

- on start — Basic
  - set [distance] to (0) — Variables
  - set [slow_distance] to (30) — Variables
  - set [stop_distance] to (8) — Variables
- forever — Basic
  - set [distance] to (⟨ultrasonic sensor distance in [cm]⟩) — Variables
  - if ⟨distance > slow_distance⟩ then — Logic
    - walk [forward] for (1) steps at speed (6) — robot PU › Actions
  - else if ⟨distance > stop_distance⟩ then
    - walk [forward] for (1) steps at speed (2) — robot PU › Actions
  - else
    - show icon [yes] — Basic

## Lesson 16: Final Project

### lesson_16_step1.png

Example — code in `docs/examples/other/pu_robot/lesson_16/step1/main.py`

- forever — Basic
  - if ⟨⟨ultrasonic sensor distance in [cm]⟩ < 20⟩ then — Logic
    - set ambience light [all] to RGB (0, 0, 255) — robot PU › Actuators
    - set mode [greet] — robot PU › Actions
    - pause (ms) (3000) — Basic
  - else
    - set ambience light [all] to RGB (0, 255, 0) — robot PU › Actuators

### lesson_16_step2.png

Example — code in `docs/examples/other/pu_robot/lesson_16/step2/main.py`

- on start — Basic
  - set [visitors] to (0) — Variables
- forever — Basic
  - if ⟨⟨ultrasonic sensor distance in [cm]⟩ < 20⟩ then — Logic
    - set ambience light [all] to RGB (0, 0, 255) — robot PU › Actuators
    - set mode [greet] — robot PU › Actions
    - change [visitors] by (1) — Variables
    - show number (visitors) — Basic
    - pause (ms) (3000) — Basic
  - else
    - set ambience light [all] to RGB (0, 255, 0) — robot PU › Actuators
