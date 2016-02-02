import sqlalchemy
from sqlalchemy import create_engine
import psycopg2
import pandas as pd

def query_results(city,specialty):
    """
    Given a city and specialty, returns a sorted
    list of the top 10 pharmaceutical classes.
    """
    dbname = 'medicare_data'; username = 'postgres'; mypassword = 'postgres123'; myhost='localhost';

#Grab the data from our database
    engine = create_engine('postgres://%s:%s@%s/%s'%(username,mypassword,myhost,dbname))
    con = psycopg2.connect(database = dbname, host=myhost, user = username, password=mypassword)
    cur = con.cursor()
    drug_query = """
    SELECT
        fulldatabatchsummed.pharmclass,
        fulldatabatchsummed.scaledbatch
    FROM
        fulldatabatchsummed
    WHERE
        fulldatabatchsummed.city = %s and fulldatabatchsummed.specialty = %s
    ORDER BY
        fulldatabatchsummed.scaledbatch desc
    limit 8;
    """
    cur.execute(drug_query,(city,specialty))
    results = []
    results = cur.fetchall()

#Construct the pharmclass data
    class_list = []
    for result in results:
        results_dict = {}
        class_dict = {}
        class_dict['pharmclass'] = str(result[0]).encode('utf-8')
        class_dict['scaledbatch'] = str(result[1]).encode('utf-8')
        class_list.append(class_dict)
    results_dict['class_list'] = class_list
    cur.close()
    return results_dict
