# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:27:47 2026

@author: jburj
"""


import pymysql.cursors

# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="JapanTokyoSpain2025!",
    database="r6impact",
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `killer`, `victim`, `match_id` FROM `kill_events` WHERE `killer_side` = `victim_side`;"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)

# =============================================================================
# import mysql.connector
# from mysql.connector import Error
# 
# try:
#     # Establish the connection
#     connection = mysql.connector.connect(
#         host="localhost",        # Use an IP address or domain if connecting remotely
#         user="root",    # Often "root" for local setups
#         password="JapanTokyoSpain2025!",
#         database="r6impact" # Optional if you want to create a database first
#     )
# 
#     if connection.is_connected():
#         print("Successfully connected to MySQL!")
# 
#         # Create a cursor object to execute SQL queries
#         cursor = connection.cursor()
#         cursor.execute("SELECT DATABASE();")
#         record = cursor.fetchone()
#         print("Connected to database:", record)
# 
# except Error as e:
#     print(f"Error while connecting to MySQL: {e}")
# 
# finally:
#     # Always close the cursor and connection when done
#     if 'connection' in locals() and connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection closed.")
# =============================================================================
