import base64
import json
import os
from sys import argv
import PySimpleGUI


def logger(msg):
    logfile = open("log.txt", 'a+')
    logfile.write(msg + "\n")
    logfile.close()


def error_popup(error_title, error_msg):
    logger(error_msg)
    PySimpleGUI.Popup(error_title, error_msg)
    raise SystemExit


class ToolpathConverter:
    def __init__(self, abs_filepath):
        self.abs_filepath = open(abs_filepath, 'r').read()
        self.converted_toolpath = None
        self.pretty_json = None
        self.filepath, self.filename = os.path.split(abs_filepath)
        self.new_filename = f"{str(os.path.split(abs_filepath)[1]).rsplit('.', 1)[0]}.json"

    def save_pretty_toolpath(self):
        """ Takes the converted toolpath and saves it in pretty JSON format to a new .json file. """
        self.pretty_json = json.dumps(self.converted_toolpath, indent=4, sort_keys=True)
        f = open(os.path.join(self.filepath, self.new_filename), 'w')
        f.write(self.pretty_json)
        f.close()

    def convert_toolpath(self):
        """ Converts from base64 to plaintext. """
        try:
            self.converted_toolpath = base64.b64decode(self.abs_filepath)
        except TypeError as e:
            error_popup("ERROR CONVERTING B64", e)

    def valid_json(self):
        """ Checks that the converted toolpath is a valid JSON """
        try:
            self.converted_toolpath = json.loads(self.converted_toolpath)
        except (ValueError, TypeError) as e:
            error_popup("ERROR - NOT A VALID JSON", e)

    def main(self):
        """ Main running block """
        self.convert_toolpath()
        self.valid_json()
        self.save_pretty_toolpath()


if __name__ == '__main__':
    if not len(argv) > 1:
        error_popup("No file specified", "No args passed to executable")
        quit()
    logger(str(argv))
    convert_file = ToolpathConverter(argv[1])
    convert_file.main()
