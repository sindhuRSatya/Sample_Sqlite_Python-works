

import sqlite3

import csv


def insert_orders_def():

	f = open('orders.csv', 'r')

	next(f, None)

	reader = csv.reader(f, delimiter=',')



sql = sqlite3.connect("db_customer.db")

cur = sql.cursor()




for row in reader:

	cur.execute("INSERT INTO order_tab VALUES(?,?,?,?,?,?)", row)
 	

f.close()
sql.commit()



#for row in cur.execute('SELECT * FROM employee'):

#		print(row)




	