#!/usr/bin/env python3

import os

from openpyxl import load_workbook

from mdt_tools import mdt_tools

# def munch(xlrd_workbook, key, munch_column, first_row = 4):
#     """Returns a list of tuples sorted by their second element
#     There first element of the tuple is a row name 
#     The second element is the number of hits 
#     """
#     fieldValueSum = {}
#     for i in range(0, xlrd_workbook.nsheets):
#         sheet = xlrd_workbook.sheet_by_index(i)
#         if ((key[0] == None or key[0] == sheet.cell_value(0, 1)) and \
#             (key[1] == None or key[1] == sheet.cell_value(1, 1))):
#             for j in range(first_row, sheet.nrows):
#                 if(sheet.cell_value(j,munch_column) != ""):
#                     field = str(sheet.cell_value(j,munch_column))
#                     try:
#                         #numbers like 2 in the xlsx file will be read in as 2.0 
#                         #this will make sure they are read in as 2
#                         field = str(int(float(field))) 
#                     except:
#                         pass
#                     if field not in fieldValueSum:
#                         fieldValueSum[field] = int(sheet.cell_value(j,munch_column+1))
#                     else:
#                         fieldValueSum[field] += int(sheet.cell_value(j,munch_column+1))

#     fieldValueSum_sorted = sorted(fieldValueSum.items(), key=lambda x: x[1], reverse = True)
#     return fieldValueSum_sorted


    # try:
    #     aircrafts = [] 
    #     customers = [] 
    #     for i in range(0, workbook):
    #         sheet = workbook.sheet_by_index(i)
    #         if str(sheet.cell_value(0,1)) != "Select... ":
    #             if sheet.cell_value(0,1) not in aircrafts:
    #                 aircrafts.append(int(sheet.cell_value(0,1)))
    #         if str(sheet.cell_value(1,1)) != "Select...":
    #             if str(sheet.cell_value(1,1)) not in customers:
    #                 customers.append(str(sheet.cell_value(1,1))) 
    # except:
    #     print(".xlsx file formating error, check customer and aircraft fields")
    #     quit()


def get_aircrafts(xlsx_workbook):
    return 0

def get_customers(xlsx_workbook):
    return 0

if __name__ == '__main__':
    file_list = mdt_tools.check_for_files([".xlsx"])
    workbook_filename = file_list[mdt_tools.menu(file_list, "Select a file: ")]
    print("--------------------")
    print("Reading from file: " + workbook_filename)
    try:
        wb = load_workbook(workbook_filename)
    except:
        print("Failed to load file, check integrity of file")
        quit()
    
    aircraft_list = get_aircrafts(wb)
    customer_list = get_customers(wb)
    key_select = mdt_tools.menu(["Aircrafts","Customers","Both"], "Query by: ")
    if key_select == 0:
        search_keys = (aircraft_list,None)
    elif key_select == 1:
        search_keys = (None,customer_list)
    elif key_select == 2:
        search_keys = (aircraft_list,customer_list)

    key = [None,None]
    if search_keys[0]:
        key[0] = search_keys[0][\
            mdt_tools.menu(search_keys[0],"Select a Aircrafts: ")]
    if search_keys[1]:
        key[1] = search_keys[1][\
            mdt_tools.menu(search_keys[1],"Select a Customer: ")]

    try:
        testSheet = workbook.sheet_by_index(0)
        columnNames = ["All"]
        columnNamesIndex = {}
        for i in range(0, testSheet.ncols):
            if testSheet.cell_value(3,i) == "Hits":
                columnNames.append(str(testSheet.cell_value(3,i-1)))
                columnNamesIndex[str(testSheet.cell_value(3,i-1))] = i-1
    except:
        print(".xlsx file formating error, check column headers")
        quit()

    # sumColumn = columnNames[user_select(columnNames,"What field do you want to munch: ")]

    # sumSortedFields = {}
    # try:
    #     if sumColumn == "All":
    #         for i in columnNamesIndex:
    #             sumSortedFields[i] = munch(workbook, key, columnNamesIndex[i])
    #     else:
    #         sumSortedFields[sumColumn] = munch(workbook, key, columnNamesIndex[sumColumn])
    # except:
    #     print(".xlsx file formating error, check all hit field only have int")
    #     quit()    

    # fieldTotalHits = {}
    # for i in sumSortedFields:
    #     totalHits = 0
    #     for j in range(0, len(sumSortedFields[i])):
    #         totalHits += sumSortedFields[i][j][1]
    #     fieldTotalHits[i] = totalHits
    
    # if key[0] and key[1]:
    #     keyPrint = str(key[0]) + " + " + str(key[1])
    # elif key[0]:
    #     keyPrint = str(key[0])
    # elif key[1]:
    #     keyPrint = str(key[1])
    # print("--------------------")
    # print(keyPrint + " traffic looks like:")
    
    # for i in sumSortedFields:
    #     if sumSortedFields[i]:
    #         print("--------------------")
    #     for j in range(0,len(sumSortedFields[i])):
    #         hitPercentage = ( float(sumSortedFields[i][j][1]) / float(fieldTotalHits[i]) )*100.0
    #         print(i + " " + \
    #                 str(sumSortedFields[i][j][0]) + " had " + \
    #                 str(sumSortedFields[i][j][1]) + " hits ~" + \
    #                 str(round(hitPercentage, 2)) + "% of traffic")

    # print("--------------------")  
    # inputKey = raw_input("[1] Save to Output#.Xlsx (Eny other key to exit) ")
    # if inputKey == "1":
    #     n = 1
    #     while os.path.exists("Output%s.xlsx" % n):
    #         n += 1
    #     outputWorkbook = xlsxwriter.Workbook("Output%s.xlsx" % n)
    #     worksheet = outputWorkbook.add_worksheet()
    #     c = 0
    #     for i in sumSortedFields:
    #         if sumSortedFields[i]:
    #             worksheet.write(0, 0, keyPrint)
    #             worksheet.write(1, c+0, i)
    #             worksheet.write(1, c+1, "Hits")
    #             worksheet.write(1, c+2, "%")
    #             for j in range(0,len(sumSortedFields[i])):
    #                 hitPercentage = ( float(sumSortedFields[i][j][1]) / float(fieldTotalHits[i]) )*100.0
    #                 worksheet.write(j+2, c+0, sumSortedFields[i][j][0])
    #                 worksheet.write(j+2, c+1, sumSortedFields[i][j][1])
    #                 worksheet.write(j+2, c+2, round(hitPercentage,2))
    #             c += 3
        
    #     outputWorkbook.close()
    #     print("Output%s.xlsx Genarated" % n)
