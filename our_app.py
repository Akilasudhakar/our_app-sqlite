import database

#add a record to database
#database.add_one("Laura","Smith","laura@smith.com")
#Delete Record use rowid as string
#database.delete_one('7')

#Lookup Email Address Record
database.email_lookup("john@codemy.com")

#Add Many Records
# stuff = [
# 	('Brenda','Smitherton','brenda@smitherthon.com'),
# 	('Joshua','Raintree','josh@raintree.com')
# 	]
# database.add_many(stuff)


#show all the records
#database.show_all()

