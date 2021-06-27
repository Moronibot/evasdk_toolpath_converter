"""
Converter.py: This is the main block of code for handling both workflow commands via a CLI argument.
"""
import base64
import binascii
import json
import os
from sys import argv
from converter_utils import save_original_string


class ToolpathConverter:
    """ Fuck docstrings, this is trashy anyway. """
    def __init__(self, abs_filepath):
        self.abs_filepath = abs_filepath
        self.abs_filepath_contents = open(abs_filepath, 'r').read()
        self.converted_toolpath = None
        self.pretty_json = None
        self.filepath, self.filename = os.path.split(abs_filepath)
        self.new_filename = f"{str(os.path.split(abs_filepath)[1]).rsplit('.', 1)[0]}.json"

    def save_pretty_toolpath(self):
        """ Takes the converted toolpath and saves it in pretty JSON format to a new .json file. """
        with open(os.path.join(self.filepath, self.new_filename), 'w') as file:
            self.pretty_json = json.dumps(self.converted_toolpath, indent=4, sort_keys=True)
            file.write(self.pretty_json)
            file.close()

    def b64_text(self):
        """ Converts from base64 to plaintext. """
        try:
            self.converted_toolpath = base64.b64decode(self.abs_filepath_contents)
        except (TypeError, binascii.Error) as b64_convert_err:
            raise RuntimeError("ERROR CONVERTING B64: CORRUPTED") from b64_convert_err

    def valid_json(self):
        """ Checks that the converted toolpath is a valid JSON """
        try:
            self.converted_toolpath = json.loads(self.converted_toolpath)
        except (UnicodeDecodeError, TypeError, json.decoder.JSONDecodeError) as invalid_json:
            raise RuntimeError("ERROR - NOT A VALID JSON") from invalid_json

    def main(self):
        """ Main running block """
        self.b64_text()
        self.valid_json()
        self.save_pretty_toolpath()


if __name__ == '__main__':
    if len(argv) <= 2:
        raise RuntimeError("No argument passed!")
    cli_argv = argv[2]
    if argv[1] == "--CLIPBOARD":
        cli_argv = save_original_string(cli_argv)
        convert_toolpath = ToolpathConverter(cli_argv)
        convert_toolpath.main()
    elif argv[1] == "--ACT_FILE":
        convert_file = ToolpathConverter(cli_argv)
        convert_file.main()
    else:
        raise RuntimeError("UNEXPECTED INPUT")
