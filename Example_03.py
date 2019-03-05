#!/usr/bin/env python3

import os

import openpyxl

def user_select(option_list, selection_message):
    """Returns !index! of the option from the option_list the user selects  
    the user is precented with all options and then the selection message
    """
    print("--------------------")
    for i in range(0, len(option_list)):
        print("[" + str(i+1) + "] " + str(option_list[i]))
    userSelection = raw_input(selection_message)
    if userSelection.isdigit():
        if int(userSelection) <= len(option_list) and int(userSelection) > 0:
            return int(userSelection)-1
    print("Improper input!!")
    user_select(option_list, selection_message)

def munch(xlrd_workbook, key, munch_column, first_row = 4):
    """Returns a list of tuples sorted by their second element
    There first element of the tuple is a row name 
    The second element is the number of hits 
    """
    fieldValueSum = {}
    for i in range(0, xlrd_workbook.nsheets):
        sheet = xlrd_workbook.sheet_by_index(i)
        if ((key[0] == None or key[0] == sheet.cell_value(0, 1)) and \
            (key[1] == None or key[1] == sheet.cell_value(1, 1))):
            for j in range(first_row, sheet.nrows):
                if(sheet.cell_value(j,munch_column) != ""):
                    field = str(sheet.cell_value(j,munch_column))
                    try:
                        #numbers like 2 in the xlsx file will be read in as 2.0 
                        #this will make sure they are read in as 2
                        field = str(int(float(field))) 
                    except:
                        pass
                    if field not in fieldValueSum:
                        fieldValueSum[field] = int(sheet.cell_value(j,munch_column+1))
                    else:
                        fieldValueSum[field] += int(sheet.cell_value(j,munch_column+1))

    fieldValueSum_sorted = sorted(fieldValueSum.items(), key=lambda x: x[1], reverse = True)
    return fieldValueSum_sorted

if __name__ == '__main__':
    fileList = []
    for fileName in os.listdir('.'):
        if fileName.endswith(".xlsx") and not fileName.startswith("Output"):
            fileList.append(fileName)

    workbookFile = fileList[user_select(fileList, "Select a file: ")]
    print("--------------------")
    print("Reading from file: " + workbookFile)
    try:
        workbook = xlrd.open_workbook(workbookFile)
    except:
        print("Failed to load file, check integrity of file")
        quit()

    try:
        aircrafts = [] 
        customers = [] 
        for i in range(0, workbook.nsheets):
            sheet = workbook.sheet_by_index(i)
            if str(sheet.cell_value(0,1)) != "Select... ":
                if sheet.cell_value(0,1) not in aircrafts:
                    aircrafts.append(int(sheet.cell_value(0,1)))
            if str(sheet.cell_value(1,1)) != "Select...":
                if str(sheet.cell_value(1,1)) not in customers:
                    customers.append(str(sheet.cell_value(1,1))) 
    except:
        print(".xlsx file formating error, check customer and aircraft fields")
        quit()

    inputSearchType = user_select(["Aircrafts","Customers","Both"], "Query by: ")
    if inputSearchType == 0:
        searchKeys = (aircrafts,None)
    elif inputSearchType == 1:
        searchKeys = (None,customers)
    elif inputSearchType == 2:
        searchKeys = (aircrafts,customers)

    key = [None,None]

    if searchKeys[0]:
        key[0] = searchKeys[0][user_select(searchKeys[0],"Select a Aircrafts: ")]
    if searchKeys[1]:
        key[1] = searchKeys[1][user_select(searchKeys[1],"Select a Customer: ")]

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

    sumColumn = columnNames[user_select(columnNames,"What field do you want to munch: ")]

    sumSortedFields = {}
    try:
        if sumColumn == "All":
            for i in columnNamesIndex:
                sumSortedFields[i] = munch(workbook, key, columnNamesIndex[i])
        else:
            sumSortedFields[sumColumn] = munch(workbook, key, columnNamesIndex[sumColumn])
    except:
        print(".xlsx file formating error, check all hit field only have int")
        quit()    

    fieldTotalHits = {}
    for i in sumSortedFields:
        totalHits = 0
        for j in range(0, len(sumSortedFields[i])):
            totalHits += sumSortedFields[i][j][1]
        fieldTotalHits[i] = totalHits
    
    if key[0] and key[1]:
        keyPrint = str(key[0]) + " + " + str(key[1])
    elif key[0]:
        keyPrint = str(key[0])
    elif key[1]:
        keyPrint = str(key[1])
    print("--------------------")
    print(keyPrint + " traffic looks like:")
    
    for i in sumSortedFields:
        if sumSortedFields[i]:
            print("--------------------")
        for j in range(0,len(sumSortedFields[i])):
            hitPercentage = ( float(sumSortedFields[i][j][1]) / float(fieldTotalHits[i]) )*100.0
            print(i + " " + \
                    str(sumSortedFields[i][j][0]) + " had " + \
                    str(sumSortedFields[i][j][1]) + " hits ~" + \
                    str(round(hitPercentage, 2)) + "% of traffic")

    print("--------------------")  
    inputKey = raw_input("[1] Save to Output#.Xlsx (Eny other key to exit) ")
    if inputKey == "1":
        n = 1
        while os.path.exists("Output%s.xlsx" % n):
            n += 1
        outputWorkbook = xlsxwriter.Workbook("Output%s.xlsx" % n)
        worksheet = outputWorkbook.add_worksheet()
        c = 0
        for i in sumSortedFields:
            if sumSortedFields[i]:
                worksheet.write(0, 0, keyPrint)
                worksheet.write(1, c+0, i)
                worksheet.write(1, c+1, "Hits")
                worksheet.write(1, c+2, "%")
                for j in range(0,len(sumSortedFields[i])):
                    hitPercentage = ( float(sumSortedFields[i][j][1]) / float(fieldTotalHits[i]) )*100.0
                    worksheet.write(j+2, c+0, sumSortedFields[i][j][0])
                    worksheet.write(j+2, c+1, sumSortedFields[i][j][1])
                    worksheet.write(j+2, c+2, round(hitPercentage,2))
                c += 3
        
        outputWorkbook.close()
        print("Output%s.xlsx Genarated" % n)
