""""
Setup.py: Only thing this is here for currently is to ensure that the correct path to the executable
is set within the workflow. Should catch most deep folder paths that should crop up.
"""
import os

WORKFLOW_PATH = 'Convert_Toolpath.workflow/Contents/document.wflow'

PATH_TO_EXE = "/".join(os.getcwd().split('/')[3::])
REPO_FOLDER = "/".join(os.getcwd().split('/')[-1::])
CMD_PATH = f"./{PATH_TO_EXE}/{REPO_FOLDER}/dist/converter $@"
STR_TO_REPLACE = "INSERT_CMD_STR"

def set_command_string_in_workflow():
    """ Searches for STR_TO_REPLACE and writes the correct path to the file """
    with open(WORKFLOW_PATH, "r") as workflow_file:
        loaded_workflow = workflow_file.readlines()
        workflow_file.close()

    for n_line, file_contents in enumerate(loaded_workflow):
        if STR_TO_REPLACE in file_contents:
            loaded_workflow[n_line] = file_contents.replace(STR_TO_REPLACE, CMD_PATH)

    with open(WORKFLOW_PATH, "w") as workflow_file:
        workflow_file.writelines(loaded_workflow)
        workflow_file.close()


if __name__ == '__main__':
    set_command_string_in_workflow()
