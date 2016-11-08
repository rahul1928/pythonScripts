#!/usr/bin/python

import sys
import MySQLdb


host = str(sys.argv[1])
user = str(sys.argv[2])
passwd = str(sys.argv[3])
db_name = str(sys.argv[4])


def create_db ():

# Open database connection
  db = MySQLdb.connect( host,user,passwd )

# prepare a cursor object using cursor() method
  cursor = db.cursor()

# create database
  sql = 'CREATE DATABASE ' + db_name

  try:

   # Execute the SQL command
   cursor.execute(sql)

   # Commit your changes in the database
   db.commit()

  except:

   # Rollback in case there is any error
   db.rollback()

# disconnect from server
  db.close()

create_db ()

