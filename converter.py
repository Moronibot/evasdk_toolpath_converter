import base64
import json
import os
from sys import argv

class ToolpathConverter:
    def __init__(self, abs_filepath):
        self.abs_filepath = open(abs_filepath, 'r').read()
        self.converted_toolpath = None
        self.pretty_json = None
        self.new_filename = f"{str(os.path.split(abs_filepath)[1]).rsplit('.', 1)[0]}.json"

    def save_pretty_toolpath(self):
        self.pretty_json = json.dumps(self.converted_toolpath, indent=4, sort_keys=True)
        print(self.new_filename)
        f = open(self.new_filename, 'w')
        f.write(self.pretty_json)
        f.close()

    def convert_toolpath(self):
        try:
            self.converted_toolpath = base64.b64decode(self.abs_filepath)
        except TypeError:
            print("ERROR CONVERTING B64")

    def valid_json(self):
        try:
            self.converted_toolpath = json.loads(self.converted_toolpath)
        except ValueError or TypeError:
            print("ERROR")
            return False
        print("Valid JSON")
        return True

    def run(self):
        self.convert_toolpath()
        self.valid_json()
        self.save_pretty_toolpath()

if __name__ == '__main__':
    convert_file = ToolpathConverter(argv[1])
    convert_file.run()
