import os
import sys
import mysql.connector
import psycopg2
from pprint import pprint
import MySQLdb

# ------------------------------
# Import internal snippets     |
# ------------------------------
#
#from include.db_config import *
#from include.MySQLCursorDict import *

# ------------------------------
# Open database connections    |
# ------------------------------
#
# Mysql connection
try:
  cnx_msql = mysql.connector.connect(host='localhost', user='root', passwd='Kymtai96!', db='trial')
except mysql.connector.Error as e:
  print ("MYSQL: Unable to connect!"), e.msg
  sys.exit(1)

# Postgresql connection
try:
  cnx_psql = psycopg2.connect(user='postgres', password='passw0rd!', host='localhost', port='5432', database='mydb')
except psycopg2.Error as e:
  print('PSQL: Unable to connect!\n{0}').format(e)
  sys.exit(1)

# Cursors initializations
cur_msql = cnx_msql.cursor(dictionary=True)
cur_psql = cnx_psql.cursor()

# ---------------------------------
# kim.msql-table > test.psql-table |
# ---------------------------------
#
cur_msql.execute("SELECT name, gender, age, location, FROM kim");

for row in cur_msql:

  ### trasformation/ conversion of mysql data OR in other cases type casting
  if row['user_id'] == 0:
    row['user_id'] = row['group_id']
  else:
    pass

  try:
    cur_psql.execute("INSERT INTO test (name, gender, age, location) \
                      VALUES (%(name)s, %(gender)s, %(age)s, %(location)s)", row)
  except psycopg2.Error as e:
    print ("cannot execute that query!!"), e.pgerror
    sys.exit("Some problem occured with that query! leaving early this lollapalooza script")

## Closing cursors
cur_msql.close()
cur_psql.close()

## Committing 
cnx_psql.commit()

## Closing database connections
cnx_msql.close()
cnx_psql.close()
