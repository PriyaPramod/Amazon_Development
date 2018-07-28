import pandas as pd

def get_sheet(file_path, sheetname):
    sheet = pd.read_excel(file_path, sheet_name=sheetname)
    return sheet
    
def get_row_num(file_path, sheetname):
    sheet = get_sheet(file_path, sheetname)
    row = sheet.shape[0]
    return row

def get_cell_value(file_path, sheetname, row_number, column_name):
    sheet = get_sheet(file_path, sheetname)
    value = sheet.loc[row_number][column_name]
    return str(value)
