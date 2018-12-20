



import sqlite3

import insert_orders






def get_connection(db_file):

	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)

	return None


	


def insert_cust_def(cur):

'''FUNCTION TO POPULATE CUSTOMER TABLE THROUGH PYTHON CODE'''

	data = [
	(1001, 'sagar', 99447324023, 'whitefield', 'bangalore',560067, 'india'),
	(1002, 'dinshu', 99447826783, 'malleswaram','bangalore',520055, 'india'),
	(1003, 'kousalya',9968454023, 'AECS Layout', 'mysore',550477, 'india'),
	(1004, 'prakash',8805675423, 'whitefield', 'mangalore',560067, 'india')
	]

	sql = '''insert into cust_tab(cust_id,cust_name,phone,address,city,postalcode,country) 
			VALUES(?,?,?,?,?,?,?)'''

	cur.executemany(sql,data)




# FEW FUNCTIONS BELOW : TASKS OF DATA RETEIEVING FROM MULTIPLE TABLES


	def task1_def(cur):


		'''AN EXAMOPLE INNERJOIN'''


		sql = ''' SELECT CUST_TAB.CUST_ID,CUST_TAB.CUST_NAME, \
				ORDER_TAB.ORDER_ID, ORDER_TAB.ORTDER_DATE FROM CUST_TAB \
			     INNER JOIN ORDER_TAB\
				  ON CUST_TAB.CUST_ID = ORDER_TAB.CUST_NUM '''


		cur.execute(sql)

		



	def main():
		
		# GETTING CONNECTION


		conn = get_connection("db_customer.db")

		print("connection is successful")
		
		cursor = conn.cursor();


		#  FUNCTIONS TO INSERT VALUES INTO TABLES



		insert_cust_def()

		#THE FOLLWING FUNCTION INSERTS VALUES INTO TABLES FROM READING A CSV FILE WHICH IS IN ANOTHER MODULE..IMPORTED 

		insert_orders.insert_order_def()

		

		insert_products_def()

		insert_orderdetails_def()

		insert_payments_def()



		print("	NUMBER OF ORDERS PLACED BY PARTICULAR CUSTOMER:")


		task1_def(conn,cursor)

		print("Status of the Order:")

		task2_def(cursor)

		print("The products orderd and payments made by each customer:")


		task3_def(cursor)

		
		if __name__ == '__main__':
			main()