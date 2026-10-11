# To do

## Hardware testing

### PU Robot
- [ ] Check the micro:bit display can be seen through the head cover (Lessons 2, 7, 8 show icons and numbers).
- [ ] Lesson 4: check what each mode does and how it stops, and what happens when a new mode starts while another is running (Exercise 3).
- [ ] Lesson 5: check **stop action** stops walking started with **set robot move direction**.
- [ ] Lesson 6: check 60–120 is a safe range for head pitch and head offset.
- [ ] Lesson 8: check the body pitch and roll units and range, and whether a clap is heard with the head cover on (and isn't set off by servo noise).
- [ ] Lesson 9: check which way the joystick speed value goes (forwards positive or negative), and that two pairs on different radio groups don't interfere.

### XGO Robot Dog
- [ ] Check buttons A and B and the touch logo can be reached with the micro:bit in the head slot.
- [ ] Check whether the USB port can be reached with the micro:bit in its slot (Lesson 1).
- [ ] Lesson 5: check that a body tilt holds until the next command, and what happens past ±20 degrees.
- [ ] Lesson 6: find which clamp values open and close the gripper, and check clampX and clampZ directions.
- [ ] Lesson 8: check recording and replaying pose 1 with an unloaded leg, and whether poses survive switching off.

### WuKong Manipulator
- [ ] Check 150 degrees is a safe "fully curled" angle for a typical build.
- [ ] Lesson 9: check tilt control isn't too jittery at a 50 ms pause.

## Images
- [ ] Replace every Blocks screenshot placeholder in `docs/assets/blocks/` (each placeholder names its program).
- [ ] Replace the three WuKong build photo placeholders in `docs/assets/wukong/`.

## Decisions
- [ ] Licence: MIT (current `LICENSE`) or GPLv3 code plus CC BY-NC-SA 4.0 content (current footer).
- [ ] Terminology definitions written new or adapted for this site: calibration, event, event handler, port, random number, threshold, radio group.
- [ ] The cyan banner is close to the light-blue tip callout colour. Keep it, or darken the banner?
