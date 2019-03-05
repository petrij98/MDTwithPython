import os

def menu(tuple_list, message):
    """Returns second part of the tuple of the option that the user selects
    takes a list of tuples the first element in each tuple is shown as an option   
    the user is precented with all options and then the selection message
    """
    print("--------------------")
    for i in range(0, len(tuple_list)):
        print("[" + str(i+1) + "] " + str(tuple_list[i][0]))
    userSelection = input(message)
    if userSelection.isdigit():
        if int(userSelection) <= len(tuple_list) and int(userSelection) > 0:
            return tuple_list[int(userSelection)-1][1]
    print("Improper input!!")
    menu(tuple_list, message)

def check_for_files(filetype_list, directory_path = '.'):
    """Returns a list of filenames
    Takes a list of strings that are file endings to look for
    optional third argument for path to directory to search default is running director 
    """
    file_list = []
    for file_name in os.listdir(directory_path):
        for filetype in filetype_list:
            if file_name.endswith(filetype):
                file_list.append((file_name,file_name))
    return file_list