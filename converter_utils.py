import base64
import binascii
import os
import time


def timestamp():
    """ Simple timestamp to reduce the likelihood of duplicate files. """
    return time.strftime("%H%M%S_%d%b%y")


def generate_filename():
    """ Yes. Timestamp_toolpath.act """
    return f"{timestamp()}_toolpath.act"


def save_original_string(str_to_save, save_filepath="Toolpaths"):
    """
    Saves the text passed to it providing it's a valid base64 string.
    Returns the filename only as the default folder is set via setup.py
    """
    joined_filepath = os.path.join(save_filepath, generate_filename())
    if decode_b64(str_to_save):
        file = open(joined_filepath, 'w')
        file.write(str_to_save)
        file.close()
        return joined_filepath
    else:
        return False
