#!/usr/bin/env python3

import os

import PyPDF2
import docx

from Example_tools import menu, check_for_files

#Calls the right parser function based on file type
def parse(file_target, option):
    if file_target.endswith(".pdf"):
        return parse_pdf(file_target,option)
    if file_target.endswith(".docx"):
        return parse_docx(file_target,option)

#needs logic 
def parse_pdf(file_target,option):
    return None

#needs logic 
def parse_docx(file_target,option):
    return None

#More or less the main function of the program
if __name__ == '__main__':
    file_list = check_for_files([".docx",".pdf"])
    file_target = menu(file_list,"What file do you want to operate on? ")
    operation_list = {"Find pages with IPs":0}
    operation = menu(operation_list,"What operation would you proform on the file? ") 
    parse_result = parse(file_target, operation)
    print(parse_result)