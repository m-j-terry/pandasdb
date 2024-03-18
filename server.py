from dotenv import load_dotenv
import os
import psycopg2
from workbook import extract_data

## SET UP CONNECTION
load_dotenv()
connection_string = os.getenv("CONNECTION_STRING")
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()

## LOAD DATA INTO A LIST OF CLASS OBJECTS
corporate_sheets = extract_data()

## QUERY TOTALS TABLE
def create_totals_table():
    totals_sheet = "Grand Totals"
    cursor.execute('CREATE TABLE IF NOT EXISTS {} (id SERIAL PRIMARY KEY, name VARCHAR(30), total INTEGER)'.format(totals_sheet))
    for corporation in corporate_sheets:
        ## Add each corporation and sum total waste to Grand Totals table
        cursor.execute('SELECT SUM(total) AS total_price FROM {}'.format(corporation.name))
        total_price = cursor.fetchone()[0]
        cursor.execute('''
            INSERT INTO {} (name, total) 
            SELECT ?, ? 
            WHERE NOT EXISTS (
                SELECT 1 FROM {} 
                WHERE name = ? AND total = ?
            )
        '''.format(corporation.name, corporation.name), 
        (corporation.name, total_price, corporation.name, total_price)
        )
    ## After adding corporations to Grand Totals, calculate grand total of these.
    cursor.execute('SELECT SUM(total) AS total_price FROM {}'.format(totals_sheet))
    total_price = cursor.fetchone()[0]
    cursor.execute('''
        INSERT INTO {} (name, total) 
        SELECT ?, ? 
        WHERE  NOT EXISTS ( 
            SELECT 1 FROM {} 
            WHERE name = ? and total = ?
        )
    '''.format(totals_sheet, totals_sheet), 
    ('Grand Total', total_price))
    conn.commit()

## QUERY TABLES
def create_tables():
    for corporation in corporate_sheets:
        # cursor.execute('CREATE TABLE IF NOT EXISTS ', corporation.name, '(id SERIAL PRIMARY KEY, date VARCHAR(10), name VARCHAR(45), defects VARCHAR(45), units INTEGER, price INTEGER, total INTEGER)')
        cursor.execute('CREATE TABLE IF NOT EXISTS {} (id SERIAL PRIMARY KEY, date VARCHAR(10), name VARCHAR(45), defects VARCHAR(45), units INTEGER, price INTEGER, total INTEGER)'.format(corporation.name))

        items = corporation.items
        for item in items:
            # cursor.execute('INSERT INTO ', corporation, '(date, name, defects, units, price, total) SELECT ?, ?, ?, ?, ?, ? WHERE NOT EXISTS ( SELECT 1 FROM, ', corporation.name, ' where date = ? AND name = ? AND price = ? ), (', item.date, ', ', item.name, ', ', item.defects, ', ', item.units, ', ', item.unit_price, ', ', item.total, ')')
            cursor.execute('''
                INSERT INTO {} (date, name, defects, units, price, total) 
                SELECT ?, ?, ?, ?, ?, ? 
                WHERE NOT EXISTS (
                    SELECT 1 FROM {} 
                    WHERE date = ? AND name = ? AND price = ?
                )
            '''.format(corporation.name, corporation.name), 
            (item.date, item.name, item.defects, item.units, item.unit_price, item.total, item.date, item.name, item.unit_price))
        conn.commit()
        create_totals_table()
    
create_tables()



cursor.close()
conn.close()



