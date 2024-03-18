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

## QUERY TABLES
def create_tables():
    for corporation in corporate_sheets:
        # cursor.execute('CREATE TABLE IF NOT EXISTS ', corporation.name, '(id SERIAL PRIMARY KEY, date varchar(10), name varchar(45), defects VARCHAR(45), units INTEGER, price INTEGER, total INTEGER)')
        cursor.execute('CREATE TABLE IF NOT EXISTS {} (id SERIAL PRIMARY KEY, date varchar(10), name varchar(45), defects VARCHAR(45), units INTEGER, price INTEGER, total INTEGER)'.format(corporation.name))

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
            '''.format(corporation.name, corporation.name), (item.date, item.name, item.defects, item.units, item.unit_price, item.total, item.date, item.name, item.unit_price))
        conn.commit()
create_tables()




cursor.close()
conn.close()



