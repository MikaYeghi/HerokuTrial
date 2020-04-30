import sqlite3
import time
import telebot

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
	
	if type(new_pet[1]) != int:
		try:
			new_pet[1] = int(new_pet[1])
			cur.execute("INSERT INTO pet VALUES(?, ?)", new_pet)
		except:
			print('Not a number!')
	else:
		cur.execute("INSERT INTO pet VALUES(?, ?)", new_pet)
	
	con.commit()
	con.close()
	
createDB()

pet = ['Мурка', 9]
addPet(pet)
k = 0

token = '962593819:AAHwAEPjq_Q8PQFAv_KgUOEYF97_sgkb8Rw'
bot = telebot.TeleBot(token)

@bot.message_handler()
def handleMessage(message):
	if message.text.split()[0] == 'add_pet':
		new_pet = message.text.split()
		del new_pet[0]
		if len(new_pet) == 2:
			addPet(new_pet)
			bot.send_message(chat_id=message.chat.id, text='Питомец был добавлен!')
		else:
			bot.send_message(chat_id=message.chat.id, text='Введите имя и возраст.')
	else:
		bot.send_message(chat_id=message.chat.id, text='Hello world!')

print('Bot instance started running.')

bot.polling()