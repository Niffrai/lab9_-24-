import psycopg2
import numpy as np
import matplotlib.pyplot as mp

con = psycopg2.connect("dbname = lab09 user=user9 password=1234 host=192.168.1.145 port=5432")

cur = con.cursor()
cur.execute("SELECT x, y FROM fn_view ORDER BY x;")

arr = cur.fetchall()
cur.close()
con.close()

x, y = np.array(arr).T
mp.plot(x, y)

mp.title('sine wave')
mp.xlabel('x')
mp.ylabel('y = sin(x)')

mp.grid(True, which='both')
mp.axhline(y=0, color='k')

mp.show()
print("form created")
