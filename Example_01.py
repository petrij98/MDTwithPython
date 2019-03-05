#!/usr/bin/env python3

import os

import openpyxl
import PyPDF2

#needs logic
def menu(tuple_list, message):
    tuple_selected = (None,None)
    return tuple_selected

#needs logic
def check_for_files():
    return [(None,None),(None,None)]

#needs logic 
def parse(file, option):
    if file[-4] == ".pdf":
        return parse_pdf(file,option)
    if file[-5] == ".xlsx":
        return parse_excel(file,option)

#needs logic 
def parse_pdf(file,option):
    return None

#needs logic 
def parse_excel(file,option):
    return None

#More or less the main function of the program
if __name__ == '__main__':
    file_list = check_for_files()
    file_target = menu(file_list,"What file do you want to operate on")
    operation_list = [(None,None),(None,None)]
    operation = menu(operation_list,"What operation would you proform on the file") 
    parse_result = parse(file_target, operation)
    print(parse_result)