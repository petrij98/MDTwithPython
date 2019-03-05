#!/usr/bin/env python3

import os

import PyPDF2
import docx

#User terminal menu for user selection
def menu(tuple_list, message):
    """Returns second part of the tuple of the option from the tuple_list the user selects  
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

#Checks for files of given types in directory 
def check_for_files(filetype_list, directory_path = '.'):
    file_list = []
    for file_name in os.listdir(directory_path):
        for filetype in filetype_list:
            if file_name.endswith(filetype):
                file_list.append((file_name,file_name))
    return file_list

#Calls the right parser function based on file type
def parse(file_target, option):
    if file_target.endswith(".pdf"):
        return parse_pdf(file_target,option)
    if file_target.endswith(".docx"):
        return parse_excel(file_target,option)

#needs logic 
def parse_pdf(file_target,option):
    return None

#needs logic 
def parse_excel(file_target,option):
    return None

#More or less the main function of the program
if __name__ == '__main__':
    file_list = check_for_files([".docx",".pdf"])
    file_target = menu(file_list,"What file do you want to operate on? ")
    operation_list = [(None,None),(None,None)]
    operation = menu(operation_list,"What operation would you proform on the file? ") 
    parse_result = parse(file_target, operation)
    print(parse_result)