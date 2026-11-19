# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:27:47 2026

@author: jburj
"""


import pymysql.cursors



def run_all():
    calc_kill_totals()
    calc_total_deaths()
    calc_num_entries()
    calc_headshot()
    
    
def calc_kill_totals():
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
            sql = "SELECT `killer`, COUNT(*) AS `kill_count` FROM `kill_events` WHERE NOT (`killer_side` = `victim_side`) GROUP BY `killer`;"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)


def calc_total_deaths():
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
            sql = "SELECT `victim`, COUNT(*) AS `death_count` FROM `kill_events` WHERE NOT (`killer_side` = `victim_side`) GROUP BY `victim`;"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)


# def calc_kd(connection):
#     with connection:
#         with connection.cursor() as cursor:
#             # Read a single record
#             sql = "SELECT `victim`, COUNT(*) AS `death_count` FROM `kill_events` WHERE NOT (`killer_side = victim_side`) GROUP BY `victim`;"
#             cursor.execute(sql)
#             result = cursor.fetchone()
#             print(result)


def calc_num_entries():
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
            sql = "SELECT `killer` AS `player`, `killer_team` AS `team`, COUNT(*) AS `opening_kills` FROM `kill_events` WHERE `is_first_kill` = 1 GROUP BY `killer`, `killer_team` ORDER BY `opening_kills` DESC;"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)


def calc_headshot():
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
            sql = "SELECT `killer` AS `player`, `killer_team` AS `team`, SUM(headshot) AS `headshots`, COUNT(*) AS `kills`, ROUND(100.0 * SUM(`headshot`) / COUNT(*), 2) AS `headshot_percentage` FROM `kill_events` GROUP BY `killer`, `killer_team`;"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
run_all()
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
