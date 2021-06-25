""""
Setup.py: Only thing this is here for currently is to ensure that the correct path to the executable
is set within the workflow. Should catch most deep folder paths that should crop up.
"""
import os

FILE_CONVERTER_PATH = 'Convert_Toolpath.workflow/Contents/document.wflow'
SAVE_CONVERTER_PATH = 'Save_Convert_Toolpath.workflow/Contents/document.wflow'

PATH_TO_EXE = "/".join(os.getcwd().split('/')[3::])

CLI_CMD = {FILE_CONVERTER_PATH: f"./{PATH_TO_EXE}/dist/converter --ACT_FILE $@",
           SAVE_CONVERTER_PATH: f"./{PATH_TO_EXE}/dist/converter --CLIPBOARD $@"}

WORKFLOW_LIST = [FILE_CONVERTER_PATH, SAVE_CONVERTER_PATH]

STR_TO_REPLACE = "INSERT_CMD_STR"


def set_command_string_in_workflow():
    """ Searches for STR_TO_REPLACE and writes the correct path to the file """
    for workflow in WORKFLOW_LIST:
        with open(workflow, "r") as workflow_file:
            loaded_workflow = workflow_file.readlines()
            workflow_file.close()

        for n_line, file_contents in enumerate(loaded_workflow):
            if STR_TO_REPLACE in file_contents:
                loaded_workflow[n_line] = file_contents.replace(STR_TO_REPLACE, CLI_CMD[workflow])

        with open(workflow, "w") as workflow_file:
            workflow_file.writelines(loaded_workflow)
            workflow_file.close()


if __name__ == '__main__':
    set_command_string_in_workflow()
