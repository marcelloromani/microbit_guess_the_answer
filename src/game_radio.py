import radio

#
# Wire protocol
#

# character used to separate fields in radio messages
MSG_SEPARATOR = "|"

# a question sent to all participant that they must solve
MSG_TYPE_CHALLENGE = "Q"

# the answer that a single participant sends back to the coordinator device
MSG_TYPE_ANSWER = "A"

# the coordinator tells each individual participant if the answer was correct or not
MSG_TYPE_RESULT = "R"


def radio_setup(group_id: int):
    """
    Configure microbit to be part of the specified radio group

    :param group_id: Radio group
    """
    radio.config(group=group_id, queue=20)
    radio.on()


# format:
# device name | message type | the message
# whether the device name represents the sender or the target
# depends on the message type
# challenge => we don't really care as it's broadcasted
# answer => the sender device id
# response => the target device id to which the response is directed
def create_radio_msg(src_or_dst_device, msg_type: str, msg: str) -> str:
    return MSG_SEPARATOR.join([src_or_dst_device, msg_type, msg])


def parse_radio_msg(msg: str) -> (str, str, str):
    device_name, msg_type, msg_content = msg.split(MSG_SEPARATOR)
    return device_name, msg_type, msg_content


def send_challenge(challenge: str, answer_a: str, answer_b: str):
    """send the challenge to all participants"""
    msg = "{} A={} B={}".format(challenge, answer_a, answer_b)
    radio.send(create_radio_msg(config.DEVICE_NAME, MSG_TYPE_CHALLENGE, msg))


def send_result(device_name: str, yes_or_no: str):
    """tell a participant if their answer was correct (Y) or not (N)"""
    radio.send(create_radio_msg(device_name, MSG_TYPE_RESULT, yes_or_no))
