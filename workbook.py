from openpyxl import load_workbook

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
barnes_and_noble = wb['Barnes & Noble']
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
corporation_objects = []

def etract_data():
