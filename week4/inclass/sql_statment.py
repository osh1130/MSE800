from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv() 

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    #database=os.getenv("DB_NAME")
)

print("connect success")

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")