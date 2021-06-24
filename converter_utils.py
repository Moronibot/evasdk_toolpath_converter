import base64
import binascii
import os
import time


def decode_b64(input_string):
    """ True if the inputted string is a valid base64. """
    try:
        if base64.b64decode(input_string):
            return True
    except binascii.Error:
        return False


def check_if_file(filepath):
    """ Makes sure that the file exists. """
    return True if os.path.isfile(filepath) else False


def good_bad_toolpath_rename(filepath, good_bad):
    sep = "_"
    dir_path, filename = os.path.split(filepath)
    split_filename = filename.split(sep)
    if good_bad:
        split_filename.insert(2, "GOOD")
    if not good_bad:
        split_filename.insert(2, "BAD")
    joined_filename = sep.join(split_filename)
    os.rename(os.path.join(dir_path,filename), joined_filename)

def timestamp():
    """ Simple timestamp to reduce the likelihood of duplicate files. """
    return time.strftime("%H%M%S_%d%b%y")


def generate_filename():
    """ Yes. Timestamp_toolpath.act """
    return f"{timestamp()}_toolpath.act"


def save_original_string(str_to_save, save_filepath=None):
    """
    Saves the text passed to it providing it's a valid base64 string.
    Returns the filename only as the default folder is set via setup.py
    """
    if save_filepath is None:
        save_filepath = os.getcwd()
    joined_filepath = os.path.join(save_filepath, generate_filename())
    if decode_b64(str_to_save):
        file = open(joined_filepath, 'w')
        file.write(str_to_save)
        file.close()
        return joined_filepath
    else:
        return False
