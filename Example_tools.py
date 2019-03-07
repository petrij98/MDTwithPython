import os

def menu(option_list, message):
    """Takes a list and a message
    returns the index of the option in list the user selects 
    shows message to user and prompts to select option
    """
    print("--------------------")
    for i in range(0,len(option_list)):
        print("[%d] %s"  % (i+1, option_list[i]))
    userSelection = input(message)
    if userSelection.isdigit():
        if int(userSelection) <= len(option_list) and int(userSelection) > 0:
            return int(userSelection)-1
    print("Improper input!!")
    menu(option_list, message)

def check_for_files(filetype_list, directory_path = '.'):
    """Returns a list of filenames
    Takes a list of strings that are file endings to look for
    optional third argument for path to directory to search default is running director 
    """
    file_list = []
    for file_name in os.listdir(directory_path):
        for filetype in filetype_list:
            if file_name.endswith(filetype):
                file_list.append(file_name)
    return file_list