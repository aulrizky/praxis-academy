import psycopg2
conn = psycopg2.connect(
    database='postgres', 
    user='john', 
    host='localhost',
    password='1234',
)

conn.autocommit = True
cursor = conn.cursor()

cursor.execute('''INSERT INTO playground(type, color, location) VALUES ('wallspider','red','north')''')

conn.commit()
print('recorded')

conn.close()