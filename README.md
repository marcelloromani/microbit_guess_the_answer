# microbit_guess_the_answer

micro:bit group game to experiment with the micro:bit radio stack

# How to play

One person plays the "Quiz master" and sets the question.

The others have to guess the answer by tapping "A" or "B".

The first to send the correct ansewr wins.

# Code setup

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

* Quiz Master: press button "A" to send the challenge and the responses to the participants

* Participants: Read the challenge and the two answers. Press "A" or "B" depending on which one you think is the correct one.

  A "tick" or "X" icon will appear if you guessed the correct answer or not.
