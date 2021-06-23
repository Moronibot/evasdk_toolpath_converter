import base64
import binascii
import os
import time


def check_if_b64(input_string):
    """ True if the inputted string is a valid base64. """
    try:
        if base64.b64decode(input_string):
            return True
    except binascii.Error:
        return False


def check_if_file(filepath):
    """ Makes sure that the file exists. """
    return True if os.path.isfile(filepath) else False


def timestamp():
    """ Simple timestamp to reduce the likelihood of duplicate files. """
    return time.strftime("%H%M_%d%b%y")


def save_original_string(encoded_b64):
    """
    Saves the text passed to it providing it's a valid base64 string.
    Returns the filename only as the default folder is set via setup.py
    """
    return True
