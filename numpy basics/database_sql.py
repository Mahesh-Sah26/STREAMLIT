import psycopg2
db_config={
    "host":"localhost",
    "dbname":"demo_db",
    "user":"postgres",
    "password":"TELIVAI!1@2#3"
}

conn=psycopg2.connect(**db_config)
cursor=conn.cursor()
sql="select * from employee;"
cursor.execute(sql)
result=cursor.fetchall()
#conn.commit()
print(result)
# cursor.close()
# conn.close()