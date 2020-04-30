import sqlite3
import time
import telebot
import os
import psycopg2

#DATABASE_URL = 'sqlite:///mydb.db'
DATABASE_URL = os.environ.get('DATABASE_URL')

def createDB():
	con = psycopg2.connect(DATABASE_URL, sslmode='require')
	cur = con.cursor()
	
	cur.execute("CREATE TABLE IF NOT EXISTS pet(id serial PRIMARY KEY, name TEXT, age INT)")
	
	con.commit()
	con.close()
	
def addPet(new_pet, chat_id, bot):
	con = psycopg2.connect(DATABASE_URL, sslmode='require')
	cur = con.cursor()
	
	if type(new_pet[1]) != int:
		new_pet[1] = int(new_pet[1])
		cur.execute("INSERT INTO pet(name TEXT, age INT) VALUES('" + new_pet[0] + "', '" + str(new_pet[1]))
		bot.send_message(chat_id=chat_id, text='Питомец был добавлен!')
	else:
		cur.execute("INSERT INTO pet(name TEXT, age INT) VALUES('" + new_pet[0] + "', '" + str(new_pet[1]))
		bot.send_message(chat_id=chat_id, text='Питомец был добавлен!')
	
	con.commit()
	con.close()
	
def getPets():
	con = psycopg2.connect(DATABASE_URL, sslmode='require')
	cur = con.cursor()
	cur.execute("SELECT * FROM pet")
	data = cur.fetchall()
	pets = ''
	for pet in data:
		pets += pet[0] + ', ' + str(pet[1]) + '\n'
		
	if pets=='':
		pets = 'Пока что нет питомцев.'
	
	return pets
	
createDB()

pet = ['Мурка', 9]
k = 0

token = '962593819:AAHwAEPjq_Q8PQFAv_KgUOEYF97_sgkb8Rw'
bot = telebot.TeleBot(token)

@bot.message_handler()
def handleMessage(message):
	if message.text.split()[0] == 'add_pet':
		new_pet = message.text.split()
		del new_pet[0]
		if len(new_pet) == 2:
			chat_id = message.chat.id
			addPet(new_pet, chat_id, bot)
		else:
			bot.send_message(chat_id=message.chat.id, text='Введите имя и возраст.')
	elif message.text.split()[0] == 'get_pets':
		text = getPets()
		bot.send_message(chat_id=message.chat.id, text=text)
	else:
		bot.send_message(chat_id=message.chat.id, text='Hello world!')

print('Bot instance started running.')

bot.polling(none_stop=True)