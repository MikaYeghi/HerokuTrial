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
	bot.send_message(chat_id=message.chat.id, text='Hello world!')

print('Bot instance started running.')

bot.polling()