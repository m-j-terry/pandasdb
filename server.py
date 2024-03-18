from dotenv import load_dotenv
import os
import psycopg2



load_dotenv()

connection_string = os.getenv("CONNECTION_STRING")

conn = psycopg2.connect(connection_string)

cur = conn.cursor()

cur.execute('SELECT NOW();')
time = cur.fetchone()[0]

cur.execute('SELECT VERSION();')
version = cur.fetchone()[0]

cur.close()
conn.close()

print('current time: ', time)
print('PostgreSQL version: ', version)

