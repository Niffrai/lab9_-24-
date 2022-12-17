import psycopg2
con = psycopg2.connect("dbname = lab09 user=user9 password=1234 host=192.168.1.145 port=5432")

cur = con.cursor()
cur.execute("SELECT x, y FROM fn ORDER BY x;")

arr = cur.fetchall()
cur.close()
con.close()

f = open("sine.csv", "w")

for row in arr:
    f.write(f"{row[0]},{row[1]}\n")

f.close()
