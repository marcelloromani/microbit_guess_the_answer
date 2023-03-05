# microbit_guess_the_answer

micro:bit group game to experiment with the micro:bit radio stack

# How to play

One person plays the "Quiz master" and sets the question.

The others have to guess the answer by tapping "A" or "B".

The first to send the correct answer wins.

# Code configuration

Each participant gets a micro:bit and needs to customize the code for their role.

## Quiz master

Set the device name to your nickname:

```python
DEVICE_NAME = "alice"
```

Set the application role to `Q` (Question)

```python
APP_ROLE = "Q"
```

Set the challenge, answers and correct answers.

Example:

```python
CHALLENGE = "27 + 6"
ANSWER_A = "30"
ANSWER_B = "33"
CORRECT_ANSWER = "B"
```

Flash the code onto the micro:bit

## Quiz participants

Set the device name to your nickname:

```python
DEVICE_NAME = "bob"
```

Set the application role to `A` (Answer)

```python
APP_ROLE = "A"
```

Flash the code onto the micro:bit

# Gameplay

* Quiz Master: press button "A" to send the challenge and the two response options to the participants

* Participants: Read the challenge and the two possible answers.

  Press "A" or "B" depending on which one you think is correct.

  A "tick" or "X" icon will appear on your microbit

* Quiz Master: press B to reveal the name (device id) of the fastest participant to answer correctly.

  Press the reset button on the back of the microbit board to clear the winner name.
