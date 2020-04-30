import sqlite3

def createDB():
	con = sqlite3.connect('mydb.db')
	cur = con.cursor()
	
	cur.execute("CREATE TABLE IF NOT EXISTS pet(name TEXT, age INT)")
	
	#cur.execute("INSERT INTO pet")
	
	con.commit()
	con.close()
	
def addPet(new_pet):
	con = sqlite3.connect('mydb.db')
	cur = con.cursor()
	
	cur.execute("INSERT INTO pet VALUES(?, ?)", new_pet)
	
	con.commit()
	con.close()
	
createDB()

pet = ['Мурка', 9]
addPet(pet)