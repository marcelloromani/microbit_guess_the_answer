import radio
from microbit import *

import config
import game_radio

RADIO_GROUP = 1


#
# methods for coordinator / question role
#

def main_for_role_question():
    # first device to send a correct answer
    # if empty, no correct answer received yet
    device_first_correct = ""

    while True:
        message = radio.receive()
        if message:
            device_name, msg_type, msg_content = game_radio.parse_radio_msg(message)

            if msg_type == game_radio.MSG_TYPE_CHALLENGE:
                # ignore, we only care about responses
                pass

            elif msg_type == game_radio.MSG_TYPE_RESULT:
                # ignore, we are the ones sending results
                pass

            elif msg_type == game_radio.MSG_TYPE_ANSWER:
                # we received an answer from a participant
                # notify them of the resoult
                if msg_content == config.CORRECT_ANSWER:
                    is_correct = "Y"
                else:
                    is_correct = "N"
                game_radio.send_result(device_name, is_correct)
                # briefly show the response on the coordinator node
                if is_correct == "Y":
                    display.show(Image.YES, delay=100, clear=True)
                    if not device_first_correct:
                        device_first_correct = device_name
                elif is_correct == "N":
                    display.show(Image.NO, delay=100, clear=True)

        # button A sends the challenge
        if button_a.was_pressed():
            display.scroll(config.CHALLENGE)
            game_radio.send_challenge(config.CHALLENGE, config.ANSWER_A, config.ANSWER_B)

        # button B shows the winner, or flashes an icon if we don't have one yet
        if button_b.was_pressed():
            if device_first_correct:
                display.scroll("WINNER {}".format(device_first_correct))
            else:
                display.show(Image.ASLEEP, delay=10, clear=True)


#
# methods for participant role
#

def send_answer(answer: str):
    """send the user guess"""
    radio.send(game_radio.create_radio_msg(config.DEVICE_NAME, game_radio.MSG_TYPE_ANSWER, answer))


def main_for_role_answer():
    while True:
        # clear data from parsing of previous message
        device_name = ""
        msg_type = ""
        msg_content = ""

        message = radio.receive()
        if message:
            device_name, msg_type, msg_content = game_radio.parse_radio_msg(message)

            if msg_type == game_radio.MSG_TYPE_CHALLENGE:
                # show the challenge sent by the coordinator
                display.scroll(msg_content)

            elif msg_type == game_radio.MSG_TYPE_ANSWER:
                # ignore answers broadcasted by other participants
                pass

            elif msg_type == game_radio.MSG_TYPE_RESULT:
                # only process the message if it was directed at us
                if device_name == config.DEVICE_NAME:
                    if msg_content == "Y":
                        display.show(Image.YES)
                    elif msg_content == "N":
                        display.show(Image.NO)
                    else:
                        display.scroll("ERR: response")

            else:
                display.scroll("ERR: msg_type")

        if button_a.was_pressed():
            display.scroll("A")
            send_answer("A")

        if button_b.was_pressed():
            display.scroll("B")
            send_answer("B")


def main():
    game_radio.radio_setup(RADIO_GROUP)
    display.scroll(config.APP_ROLE)
    display.scroll(config.DEVICE_NAME)

    if config.APP_ROLE == "Q":
        main_for_role_question()
    elif config.APP_ROLE == "A":
        main_for_role_answer()
    else:
        print("ERROR APP_ROLE")


if __name__ == "__main__":
    main()
