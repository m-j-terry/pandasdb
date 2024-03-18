from openpyxl import load_workbook
from datetime import datetime


wb = load_workbook('Trash.Pandas_ofNYC.xlsx')
grand_totals = wb['GRAND TOTALS']
grand_total = grand_totals['X4'].value

bath_and_bodyworks = wb['Bath and Body Works']
key_foods = wb['Key Foods']
cvs = wb['CVS']
walgreens = wb['Duane Reade']
pet_smart = wb['PetSmart']
pet_co = wb['PetCo']
michaels = wb['Michaels']
party_city = wb['Party City']
lush = wb['Lush']
barnes_and_noble = wb['Barnes and Noble']
western_beef = wb['Western Beef']
rite_aid = wb['Rite Aid']
target = wb['Target']
marshalls = wb['Marshalls']
aldi = wb['ALDI']
big_lots = wb['Big Lots']
five_below = wb['Five Below']
face_values = wb['Face Values']
seven_eleven = wb['Seven Eleven']
residential_trash_finds = wb['Residential Trash Finds']
lot_less = wb['Lot Less']
dollar_tree = wb['Dollar Tree']
corporate_sheets = [bath_and_bodyworks, key_foods, cvs, walgreens, pet_smart, pet_co, michaels, party_city, lush, barnes_and_noble, western_beef, rite_aid, target, marshalls, aldi, big_lots, five_below, face_values, seven_eleven, residential_trash_finds, lot_less, dollar_tree]
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
        corporate_sheet = Corporation(corporation.title)
        row = 2
        date_column = 'A'
        items_column = 'B'
        defects_column = 'C'
        units_column = 'D'
        unit_price_column = 'E'
        date = datetime.today().date()
        while True:
            item_value = corporation[items_column + str(row)].value
            if item_value is None: 
                break ## Test if there is a value to input, else break the loop.
            date_value = corporation[date_column + str(row)].value
            if date_value is not None:
                date = date_value 
            defects_value = corporation[defects_column + str(row)].value
            units_value = corporation[units_column + str(row)].value
            if units_value is None: 
                units_value = 0
            unit_price_value = corporation[unit_price_column + str(row)].value
            if unit_price_value is None: 
                unit_price_value = 0
            item = Item(date, item_value, defects_value, units_value, unit_price_value)
            corporate_sheet.add_item(item)
            row += 1
        corporate_dicts.append(corporate_sheet)
    return corporate_dicts