"""
Just a script that returns a random MAC address, nothin major
"""


import random


def generate_mac():
    """
    return a random MAC address
    """
    first_byte = random.randint(0x00, 0xFF) & 0xFE
    mac = [first_byte]

    # Generate the remaining five bytes randomly
    for _ in range(5):
        byte = random.randint(0x00, 0xFF)
        mac.append(byte)

    # Format the MAC address
    mac_address = ":".join(f"{byte:02x}" for byte in mac)

    return mac_address
