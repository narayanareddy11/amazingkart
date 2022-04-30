from csv import writer
from re import T
import sqlite3
import json
import pandas as pd

# file = open('result.json', 'w')
# file.write(' ')
# file.close()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# connect to the SQlite databases
def openConnection(pathToSqliteDb):
    connection = sqlite3.connect(pathToSqliteDb)
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    return connection, cursor


def getAllRecordsInTable(table_name, pathToSqliteDb):
    conn, curs = openConnection(pathToSqliteDb)
    conn.row_factory = dict_factory
    curs.execute("SELECT * FROM '{}' ".format(table_name))
    # fetchall as result
    results = curs.fetchall()
    # close connection
    conn.close()
    return json.dumps(results)


def sqliteToJson(pathToSqliteDb):
    connection, cursor = openConnection(pathToSqliteDb)
    # select all the tables from the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
   # print (tables)
    # for each of the tables , select all the records from the table
    with pd.ExcelWriter('analyser/output/output.xlsx') as writer:
        for table_name in tables:
            # Get the records in table
        #  print(table_name['name'], "kkkkkkk \n")
            results = getAllRecordsInTable(table_name['name'], pathToSqliteDb)


            # generate and save JSON files with the table name for each of the database tables and save in results folder

            
            with open(str('analyser/output/'+ table_name['name'])+'.json', 'w') as the_file:
                the_file.write(results)
            
                        
            df = pd.read_json('analyser/output/'+table_name['name']+ '.json')
            print(df)
            # print(type(results) )
            # with pd.ExcelFile("output.xlsx") as reader:
            #   pd.read_json(table_name['name']+".json").to_excelreader(sheet_name=table_name['name'] )
            

            

    
            df.to_excel(writer, sheet_name=table_name['name'])
         #   results.to_excel(writer, sheet_name='Sheet_name_2_2_2')
    
    # close connection
    connection.close()


if __name__ == '__main__':
    # modify path to sqlite db
    pathToSqliteDb = 'db.sqlite3'
    sqliteToJson(pathToSqliteDb)

