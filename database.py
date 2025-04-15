import sqlite3

#conn = sqlite3.connect(':memory:')

#query the DB and Return all Records
 
def show_all():

	#connect to database and create a c->cursor

	conn = sqlite3.connect('customer.db')

	c = conn.cursor()


	#Query the Database -AND / OR
	c.execute("SELECT rowid, * FROM customers ")

	items = c.fetchall()

	for items in items:
		print(items)

	#commiting to the database 
	conn.commit()

	#close our connection
	conn.close()


#Add many record to the table
def add_many(list):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.executemany("INSERT INTO customers VALUES (?,?,?)",(list))
	#commiting to the database 
	conn.commit()

	#close our connection
	conn.close()

#Delete Record from table

def delete_one(id):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("DELETE FROM customers WHERE rowid = (?)",id)



	#commiting to the database 
	conn.commit()

	#close our connection
	conn.close()

#Lookup with WHERE
def email_lookup(email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("SELECT rowid , * FROM customers WHERE email = (?)",(email,))

	items = c.fetchall()

	for items in items:
		print(items)

	#commiting to the database 
	conn.commit()

	#close our connection
	conn.close()







