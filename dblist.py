#!/usr/bin/python

import sys
import MySQLdb


def db_list ():

#create the connection
   connection = MySQLdb.connect(
                host = 'localhost',
                user = 'root',
                passwd = 'rahul123')


# get the cursor
   cursor = connection.cursor()


# execute SQL query using execute() method.
   cursor.execute("SHOW DATABASES")

# fetch all databases name
   data = cursor.fetchall ()

   for db in data:

# print the databases name
     print str(db[0])
      
   return


db_list()

