import telebot
from telebot import types
import psycopg2
from week import weeker

token = "wow that's private"
bot = telebot.TeleBot(token)
conn = psycopg2.connect(database="schedule_db",
                        user="postgres",
                        password="123456",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

c = int(weeker())

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Выберите то что вас интересует',
    reply_markup=keyboard3())

def keyboard():

    button1 = types.KeyboardButton('Понедельник')
    button2 = types.KeyboardButton('Вторник')
    button3 = types.KeyboardButton('Среда')
    button4 = types.KeyboardButton('Четверг')
    button5 = types.KeyboardButton('Пятница')
    button6 = types.KeyboardButton('Расписание на текущую неделю')
    button7 = types.KeyboardButton('Расписание на следуюущую неделю')
    button8 = types.KeyboardButton('Вернуться в начало')
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(button1).add(button2).add(button3).add(button4).add(button5).add(button6).add(button7).add(button8)
    return (markup)

def keyboard2():

    button1 = types.KeyboardButton('/week')
    button2 = types.KeyboardButton('/mtuci')
    button3 = types.KeyboardButton('/help')
    button4 = types.KeyboardButton('Вернуться в начало')

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(button1).add(button2).add(button3).add(button4)
    return (markup)

def keyboard3():

    button1 = types.KeyboardButton('Расписание')
    button2 = types.KeyboardButton('Команды')
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(button1).add(button2)
    return (markup)


@bot.message_handler(content_types=['text'])
def manipulator(message):
    global c
    if message.text == 'Понедельник' and c==0:
        cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                       "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                       "teacher_id WHERE day='Понедельник' and weektype=0")
        x = cursor.fetchall()
        x1 = str("Понедельник,чётная неделя\n\n\n")
        for row in x:
            for i in range(4):
                x1+=str(row[i]) + '   '
            x1+='\n\n'
        bot.send_message(message.chat.id, x1)
    elif message.text == 'Вторник' and c==0:
        cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                       "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                       "teacher_id WHERE day='Вторник' and weektype=0")
        x = cursor.fetchall()
        x1 = str("Вторник,чётная неделя\n\n\n")
        for row in x:
            for i in range(4):
                x1+=str(row[i]) + '   '
            x1+='\n\n'
        bot.send_message(message.chat.id, x1)
    elif message.text == 'Среда' and c==0:
        cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                       "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                       "teacher_id WHERE day='Среда' and weektype=0")
        x = cursor.fetchall()
        x1 = str("Среда,чётная неделя\n\n\n")
        for row in x:
            for i in range(4):
                x1+=str(row[i]) + '   '
            x1+='\n\n'
        bot.send_message(message.chat.id, x1)
    elif message.text == 'Четверг' and c==0:
        cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                       "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                       "teacher_id WHERE day='Четверг' and weektype=0")
        x = cursor.fetchall()
        x1 = str("Четверг,чётная неделя\n\n\n")
        for row in x:
            for i in range(4):
                x1+=str(row[i]) + '   '
            x1+='\n\n'
        bot.send_message(message.chat.id, x1)
    elif message.text == 'Пятница' and c==0:
        cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                       "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                       "teacher_id WHERE day='Пятница' and weektype=0")
        x = cursor.fetchall()
        x1 = str("Пятница,чётная неделя\n\n\n")
        for row in x:
            for i in range(4):
                x1+=str(row[i]) + '   '
            x1+='\n\n'
        bot.send_message(message.chat.id, x1)
    elif message.text == 'Понедельник' and c==1:
        cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                       "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                       "teacher_id WHERE day='Понедельник' and weektype=1")
        x = cursor.fetchall()
        x1 = str("Понедельник,нечётная неделя\n\n\n")
        for row in x:
            for i in range(4):
                x1+=str(row[i]) + '   '
            x1+='\n\n'
        bot.send_message(message.chat.id, x1)
    elif message.text == 'Вторник' and c==1:
        cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                       "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                       "teacher_id WHERE day='Вторник' and weektype=1")
        x = cursor.fetchall()
        x1 = str("Вторник,нечётная неделя\n\n\n")
        for row in x:
            for i in range(4):
                x1+=str(row[i]) + '   '
            x1+='\n\n'
        bot.send_message(message.chat.id, x1)
    elif message.text == 'Среда' and c==1:
        cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                       "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                       "teacher_id WHERE day='Среда' and weektype=1")
        x = cursor.fetchall()
        x1 = str("Среда,нечётная неделя\n\n\n")
        for row in x:
            for i in range(4):
                x1+=str(row[i]) + '   '
            x1+='\n\n'
        bot.send_message(message.chat.id, x1)
    elif message.text == 'Четверг' and c==1:
        cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                       "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                       "teacher_id WHERE day='Четверг' and weektype=1")
        x = cursor.fetchall()
        x1 = str("Четверг,нечётная неделя\n\n\n")
        for row in x:
            for i in range(4):
                x1+=str(row[i]) + '   '
            x1+='\n\n'
        bot.send_message(message.chat.id, x1)
    elif message.text == 'Пятница' and c==1:
        cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                       "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                       "teacher_id WHERE day='Пятница' and weektype=1")
        x = cursor.fetchall()
        x1 = str("Пятница,нечётная неделя\n\n\n")
        for row in x:
            for i in range(4):
                x1+=str(row[i]) + '   '
            x1+='\n\n'
        bot.send_message(message.chat.id, x1)
    elif message.text == 'Расписание на текущую неделю':

            cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                           "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                           "teacher_id WHERE day='Понедельник' and weektype=0")
            x = cursor.fetchall()
            x1 = str("Понедельник,чётная неделя\n\n\n")
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '   '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)

            cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                           "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                           "teacher_id WHERE day='Вторник' and weektype=0")
            x = cursor.fetchall()
            x1 = str("Вторник,чётная неделя\n\n\n")
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '   '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)

            cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                           "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                           "teacher_id WHERE day='Среда' and weektype=0")
            x = cursor.fetchall()
            x1 = str("Среда,чётная неделя\n\n\n")
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '   '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)

            cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                           "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                           "teacher_id WHERE day='Четверг' and weektype=0")
            x = cursor.fetchall()
            x1 = str("Четверг,чётная неделя\n\n\n")
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '   '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)

            cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                           "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                           "teacher_id WHERE day='Пятница' and weektype=0")
            x = cursor.fetchall()
            x1 = str("Пятница,чётная неделя\n\n\n")
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '   '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
    elif message.text == 'Расписание на следуюущую неделю':

            cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                           "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                           "teacher_id WHERE day='Понедельник' and weektype=1")
            x = cursor.fetchall()
            x1 = str("Понедельник,нечётная неделя\n\n\n")
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '   '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)

            cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                           "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                           "teacher_id WHERE day='Вторник' and weektype=1")
            x = cursor.fetchall()
            x1 = str("Вторник,нечётная неделя\n\n\n")
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '   '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)

            cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                           "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                           "teacher_id WHERE day='Среда' and weektype=1")
            x = cursor.fetchall()
            x1 = str("Среда,нечётная неделя\n\n\n")
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '   '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)

            cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                           "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                           "teacher_id WHERE day='Четверг' and weektype=1")
            x = cursor.fetchall()
            x1 = str("Четверг,нечётная неделя\n\n\n")
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '   '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)

            cursor.execute("SELECT timetable.subject,timetable.room_numb,timetable.start_time,"
                           "teacher.full_name FROM timetable INNER JOIN teacher ON timetable.teacher="
                           "teacher_id WHERE day='Пятница' and weektype=1")
            x = cursor.fetchall()
            x1 = str("Пятница,нечётная неделя\n\n\n")
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '   '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
    elif message.text == 'Расписание':
        bot.send_message(message.chat.id,'Выберите интересующий вас день или неделю',    reply_markup=keyboard())
    elif message.text == 'Команды':
        bot.send_message(message.chat.id,'Выберите интересующую вас команду',    reply_markup=keyboard2())
    elif message.text == '/week':
        if c == 0:
            bot.send_message(message.chat.id, 'Сейчас идет четная неделя')
        elif c == 1:
            bot.send_message(message.chat.id, 'Сейчас идет нечетная неделя')
    elif message.text == '/help':
        bot.send_message(message.chat.id,
                         'Чтобы использовать функционал бота, напишите /start. Вы можете узнать расписание на определенный день или неделю, также вы можете узнать какая сейчас неделя.')
    elif message.text == '/mtuci':
        bot.send_message(message.chat.id,'https://mtuci.ru/')
    elif message.text == 'Вернуться в начало':
        bot.send_message(message.chat.id,'Что вас интересует?',reply_markup=keyboard3())


    else:
        bot.send_message(message.chat.id, 'Команда прописана непрвильно или не предусмотрена')





bot.infinity_polling()