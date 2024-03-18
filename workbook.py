from openpyxl import load_workbook
from datetime import datetime, date


wb = load_workbook('Trash.Pandas_ofNYC.xlsx')
grand_totals = wb['GRAND TOTALS']
grand_total = grand_totals['X4'].value

Bath_and_Body_Works = wb['Bath and Body Works']
Key_Foods = wb['Key Foods']
CVS = wb['CVS']
Walgreens = wb['Duane Reade']
Pet_Smart = wb['PetSmart']
Pet_Co = wb['PetCo']
Michaels = wb['Michaels']
Party_City = wb['Party City']
Lush = wb['Lush']
Barnes_and_Noble = wb['Barnes and Noble']
Western_Beef = wb['Western Beef']
Rite_Aid = wb['Rite Aid']
Target = wb['Target']
Marshalls = wb['Marshalls']
Aldi = wb['ALDI']
Big_Lots = wb['Big Lots']
Five_Below = wb['Five Below']
Face_Values = wb['Face Values']
Seven_Eleven = wb['Seven Eleven']
Residential_Trash_Finds = wb['Residential Trash Finds']
Lot_Less = wb['Lot Less']
Dollar_Tree = wb['Dollar Tree']
corporate_sheets = [Bath_and_Body_Works, Key_Foods, CVS, Walgreens, Pet_Smart, Pet_Co, Michaels, Party_City, Lush, Barnes_and_Noble, Western_Beef, Rite_Aid, Target, Marshalls, Aldi, Big_Lots, Five_Below, Face_Values, Seven_Eleven, Residential_Trash_Finds, Lot_Less, Dollar_Tree]
corporate_dicts = []

class Corporation:
    def __init__(self, name):
        self.name = name
        self.items = []
    def add_item(self, item):
        self.items.append(item)

class Item:
    def __init__(self, date, name, defects, units, unit_price):
        self.date = date
        self.name = name
        self.defects = defects
        self.units = units
        self.unit_price = unit_price
        self.total = units * unit_price

def extract_data():
    for corporation in corporate_sheets:
        corporate_sheet = Corporation(corporation.title.replace(' ', '_'))
        row = 2
        date_column = 'A'
        items_column = 'B'
        defects_column = 'C'
        units_column = 'D'
        unit_price_column = 'E'
        this_date = datetime.today().date()
        while True:
            item_value = corporation[items_column + str(row)].value
            if item_value is None: 
                break ## Test if there is a value to input, else break the loop.
            
            date_value = corporation[date_column + str(row)].value
            if date_value is not None:
                this_date = date_value 
            # if isinstance(this_date, str) and this_date.strip():
            if this_date == '':
                this_date = date(2020, 7, 7)

            
            defects_value = corporation[defects_column + str(row)].value
            if defects_value is None: 
                defects_value = ''
            
            units_value = corporation[units_column + str(row)].value
            if units_value is None: 
                units_value = 0
            
            unit_price_value = corporation[unit_price_column + str(row)].value
            if unit_price_value is None or isinstance(unit_price_value, str): 
                unit_price_value = 1
            
            item = Item(this_date, item_value, defects_value, units_value, unit_price_value)
            corporate_sheet.add_item(item)
            row += 1
        corporate_dicts.append(corporate_sheet)
    return corporate_dicts