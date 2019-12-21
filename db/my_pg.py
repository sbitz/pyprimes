
import psycopg2

conn = psycopg2.connect(host='localhost', 
                        database='example_db', 
                        port='25432', 
                        user='example_user', 
                        password='example')



