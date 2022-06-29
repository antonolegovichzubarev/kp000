def give_answer(s):
    try:
        tip, nomer = [i for i in s.split()]
        tip_list = ['0', '1', '2', '3', '4', '5', '6', '7', '7-2', '7-v', '8', '9', '9-2', '10', '11', '12', '13', '14',
                    '15',
                    '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']
        tip_n = tip_list.index(tip)
        answer = answers[int(nomer)][tip_n]
        return answer
    except:
        return 'Нет такого задания'


import telebot
import csv

bot = telebot.TeleBot('5583501026:AAEBtuivsPD-HoPxkWfSIEHiV42P5NXh4IY')
answers = []
with open('answers.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        answers.append(line)


@bot.message_handler()
def start(message):
    t = message.text
    tasks = t.split('\n')
    answers_txt = ''
    for i in range(len(tasks)):
        task = tasks[i]
        answer = give_answer(task)
        answer_text = f'ответ на задачу <b>{task}</b>: {answer}'
        answers_txt += answer_text + '\n'
    bot.send_message(message.chat.id, answers_txt, parse_mode='html')


bot.polling(none_stop=True)
