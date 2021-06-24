import base64
import binascii
import json
import os
from sys import argv
from converter_utils import check_if_file, decode_b64, save_original_string, good_bad_toolpath_rename


class ToolpathConverter:
    def __init__(self, abs_filepath):
        self.abs_filepath = abs_filepath
        self.abs_filepath_contents = open(abs_filepath, 'r').read()
        self.converted_toolpath = None
        self.pretty_json = None
        self.filepath, self.filename = os.path.split(abs_filepath)
        self.new_filename = f"{str(os.path.split(abs_filepath)[1]).rsplit('.', 1)[0]}.json"
        self.clipboard = False

    def save_pretty_toolpath(self):
        """ Takes the converted toolpath and saves it in pretty JSON format to a new .json file. """
        f = open(os.path.join(self.filepath, self.new_filename), 'w')
        self.pretty_json = json.dumps(self.converted_toolpath, indent=4, sort_keys=True)
        f.write(self.pretty_json)
        f.close()
        good_bad_toolpath_rename(os.path.join(self.filepath, self.new_filename), good_bad=True,
                                 formatted=self.clipboard)

    def b64_text(self):
        """ Converts from base64 to plaintext. """
        try:
            self.converted_toolpath = base64.b64decode(self.abs_filepath_contents)
        except (TypeError, binascii.Error):
            raise RuntimeError("ERROR CONVERTING B64: CORRUPTED")

    def valid_json(self):
        """ Checks that the converted toolpath is a valid JSON """
        try:
            self.converted_toolpath = json.loads(self.converted_toolpath)
        except (UnicodeDecodeError, TypeError, json.decoder.JSONDecodeError):
            good_bad_toolpath_rename(self.abs_filepath, good_bad=False, formatted=self.clipboard)
            raise RuntimeError("ERROR - NOT A VALID JSON")

    def from_file(self):
        """ Main running block if it's a file toolpath """
        self.b64_text()
        self.valid_json()
        self.save_pretty_toolpath()

    def from_clipboard(self):
        """ Main running block if you've highlighted a toolpath """
        self.clipboard = True
        self.b64_text()
        self.valid_json()
        self.save_pretty_toolpath()


if __name__ == '__main__':
    if not len(argv) > 1:
        raise RuntimeError("No argument passed!")
    cli_argv = argv[1]
    if decode_b64(cli_argv):
        cli_argv = save_original_string(cli_argv)
        convert_toolpath = ToolpathConverter(cli_argv)
        convert_toolpath.from_clipboard()
    elif check_if_file(cli_argv):
        convert_file = ToolpathConverter(cli_argv)
        convert_file.from_file()
    else:
        raise RuntimeError("UNEXPECTED INPUT")
