#! /usr/bin/python
# -*- coding: utf-8 -*- 
import telebot
import random
import urllib
import re
import json
import random
from datetime import datetime
import pytz

bot = telebot.TeleBot("key")
char_id = 0

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

	try:
		if "porno365" in call.data and "page=" in call.data:
			page = int(call.data.replace("porno365 page=", ""))

			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
			req = urllib.request.Request("http://porno365.me/models", headers=headers)
			content = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
			models = re.findall(r"<a href=\"(.+?)\">.*an class=\"model_rus_name\">(.+?)</span>", content)
			keyboard = telebot.types.InlineKeyboardMarkup()
			for i in range(page, page + 5):
				keyboard.add(telebot.types.InlineKeyboardButton(text=models[i][1], callback_data="porno365 url=" + models[i][0].replace("http://porno365.me", "")))
			if page + 5 < len(models) - 1:
				keyboard.add(telebot.types.InlineKeyboardButton(text="< Следующая страница >", callback_data="porno365 page=" + str(page + 5)))
			bot.edit_message_text(
				"<b>Porno365</b> Выбери порно актрису\nМодель с "+str(page)+" по "+str(page + 5), 
				chat_id=call.message.chat.id, 
				message_id=call.message.message_id,
				reply_markup=keyboard ,
				parse_mode="html"
			)

		if "porno365" in call.data and "url=" in call.data:
			url = call.data.replace("porno365 url=", "")
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
			req = urllib.request.Request("http://porno365.me" + url, headers=headers)
			content = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
			videos = re.findall(r"<a class=\"image\" href=\"(.+?)\">.*alt=\"(.+?)\"", content)
			keyboard = telebot.types.InlineKeyboardMarkup()
			for i in range(0, 8):
				keyboard.add(telebot.types.InlineKeyboardButton(text=videos[i][1], callback_data="porno365 video=" + videos[i][0].replace("http://porno365.me", "")))
			bot.edit_message_text(
				"<b>Porno365</b> Выбери порно ролик", 
				chat_id=call.message.chat.id, 
				message_id=call.message.message_id,
				reply_markup=keyboard ,
				parse_mode="html"
			)

		if "porno365" in call.data and "video=" in call.data:
			video = call.data.replace("porno365 video=", "")
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
			req = urllib.request.Request("http://porno365.me" + video, headers=headers)
			content = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
			videos = re.findall(r"<meta property=\"og:video\" content=\"(.+?)\"", content)
			bot.edit_message_text(
				"<b>Porno365</b> Выбранный ролик <a href=\"" + videos[0] + "\">по ссылке</a>.", 
				chat_id=call.message.chat.id, 
				message_id=call.message.message_id,
				parse_mode="html"
			)
	except:
		pass


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):

	try: 
		if "чня" in message.text or "енские" in message.text or "чню" in message.text:
			bot.send_message(message.chat.id, "Нахуй чечню.")

		if "/go" in message.text:
			try:
				nick = message.text.replace("/go ", "")
				bot.send_message(message.chat.id, nick + ", иди нахуй!")
			except:
				bot.send_message(message.chat.id, "Нехватает параметра, по этому сам иди нахуй. /go Имя")

		if "/whoami" in message.text:
			array = {
				0 : " Натурал (C, C++)",
				1 : " Отсталый (C#)",
				2 : " Полупокер (Python, PHP)",
				3 : " Хуйпойминахуйнужен (bash)",
				4 : " Ебучий дед (Pascal, Delphi)",
				5 : " Повелитель машин (Asm)"
			}

			name = ""
			try:
				name = message.from_user.first_name + " " + message.from_user.last_name
			except:
				name = message.from_user.first_name

			bot.send_message(message.chat.id, "Твое имя: " + name + "\n" + "Логин: " + message.from_user.username + "\nID профиля: " + str(message.from_user.id) + "\nОриентация:" + array[random.randint(0,5)])

		if "/photo" in message.text:
			photo = open('./logo.png', 'rb')
			bot.send_photo(message.chat.id, photo)

		if "/opennet" in message.text:
			content = tmp1 = tmp2 = ""
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Content-type': 'text/html; charset=utf-8'}
			req = urllib.request.Request("http://www.opennet.ru/", headers=headers)
			content = urllib.request.urlopen(req).read()
			newsarr = re.findall(b"<td class=tnews><a href=\"(.*)\">(.*)</a>", content) #str(bytes_string,'utf-8')
			content = ""
			for i in range(0, 6):
				tmp1 = newsarr[i][0].decode("koi8-r", "ignore")
				tmp2 = newsarr[i][1].decode("koi8-r", "ignore")
				content += str(i + 1) + ") <a href=\"http://www.opennet.ru" + tmp1 + "\">" + tmp2 + "</a>\n\n"
			bot.send_message(message.chat.id, "<b>Последние новости OpenNet:</b>\n" + content, parse_mode="html")

		if "/en" in message.text:
			try:
				words = message.text.replace('/en ', '')
				headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
				req = urllib.request.Request("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170722T083707Z.7a142cb8736b4685.b90438644d5615afe82cfef66459c7001d21bc0b&text=" + 
					urllib.parse.quote_plus(words) + "&lang=ru", headers=headers)
				content = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
				content = json.loads(content)
				if words == message.text:
					bot.send_message(message.chat.id, "Нехватает параметра. /en фраза")
				else:
					bot.send_message(message.chat.id, content['text'][0])
			except:
				bot.send_message(message.chat.id, "Нехватает параметра. /en фраза")

		if "/ru" in message.text:
			try:
				words = message.text.replace('/ru ', '')
				headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
				req = urllib.request.Request("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170722T083707Z.7a142cb8736b4685.b90438644d5615afe82cfef66459c7001d21bc0b&text=" + 
					urllib.parse.quote_plus(words) + "&lang=en", headers=headers)
				content = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
				content = json.loads(content)
				if words == message.text:
					bot.send_message(message.chat.id, "Нехватает параметра. /ru фраза")
				else:
					bot.send_message(message.chat.id, content['text'][0])
			except:
				bot.send_message(message.chat.id, "Нехватает параметра. /ru фраза")

		if "/php" in message.text:
			try:
				function = message.text.replace('/php ', '').replace("_", "-")
				headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
				req = urllib.request.Request("http://php.net/manual/ru/function." + function + ".php", headers=headers)
				content = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
				about = re.findall(r"<p class=\"para rdfs-comment\">(.+?)</p>", content.replace("\n", "").replace("\r", ""))
				if function == message.text:
					bot.send_message(message.chat.id, "Некорректный параметр. /php название функции")
				else:
					bot.send_message(message.chat.id, re.sub(r'\<[^>]*\>', '', about[0]))
			except:
				bot.send_message(message.chat.id, "Вы ввели несуществующую функцию. /php название функции")

		if "/porno365" in message.text:
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
			req = urllib.request.Request("http://porno365.me/models", headers=headers)
			content = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
			models = re.findall(r"<a href=\"(.+?)\">.*an class=\"model_rus_name\">(.+?)</span>", content)
			keyboard = telebot.types.InlineKeyboardMarkup()
			for i in range(0, 4):
				keyboard.add(telebot.types.InlineKeyboardButton(text=models[i][1], callback_data="porno365 url=" + models[i][0].replace("http://porno365.me", "")))
			keyboard.add(telebot.types.InlineKeyboardButton(text="< Следующая страница >", callback_data="porno365 page=5"))
			bot.send_message(message.chat.id, "<b>Porno365</b> Выбери порно актрису\nМодель с 1 по 5", reply_markup=keyboard, parse_mode="html")

		if "/help" in message.text:
			content = "<b>Справочник по доступным функциям бота</b>\n\n"
			content += "1) /go- Функция посылающая нахуй человека, [Пример: /go Крупский]\n\n"
			content += "2) /opennet - Выводит последние 6 новостей с сайта opennet.ru\n\n"
			content += "3) /en - Переводит фразу с английского на русский [Пример: /en hello]\n\n"
			content += "4) /ru - Переводит фразу с русского на английский [Пример: /ru привет]\n\n"
			content += "5) /php - Справочник по функциям PHP [Пример: /php file_get_contents]\n\n"
			content += "6) /whoami - Предоставляет информацию о пользователе\n\n" 
			content += "7) /porno365 - Порно-каталог актрист и их видео\n\n" 
			content += "8) /pasts - Рандомная цитата\n\n" 
			content += "9) /time - Время МСК и ХБК\n\n" 
			bot.send_message(message.chat.id, content, parse_mode="html")

		if "/time" in message.text:
			current_time = 'Время в Москве - ' + datetime.now(pytz.timezone('Europe/Moscow')).strftime('%H:%M') + '\nВремя в Хабаровске - ' \
			+ datetime.now(pytz.timezone('Etc/GMT-10')).strftime('%H:%M')
			bot.send_message(message.chat.id, current_time, parse_mode="html")

		if "/pasta" in message.text:
			rand_fr = ['ФРАЕМВОРК', 'ЛЕНУПС', 'ЛИНУКС', 'ПЕХАПЭ', 
					'СИ ШУРУП', 'СИ СВАСТОН', 
					'ИМПЕРСКИЙ ФЛАГ ИЗ КИТАЯ НЕ ПОРВЕТСЯ', 'СВЕРХЧЕЛОВЕК', 
					'ТАДЖ МАХАЛ', 'XCLOUD', 'LITECLOUD', 'СКИММЕР', 'МОЙ ДЕД', 
					'КРЫMСКИЙ ПОЛУОСТРОВ', 
					'ПЕНТАГОН', 'ХАБАРОВСК', 'САЙМОН СИМУЛЯТОР', 'ЖС', 'МОЙ ЧЛЕН', 
					'ТРЕТИЙ РЕЙХ', 'НОВОСТИ 4PDA', 
					'ГАРВАРД', 'БОТ', 'АНДРОИД', 'ШИНДОУС', 
					'АЙФОН', 'УКРАИНСКИЙ ГИМН', 'ОСВЕНЦИМ', 'TCP/IP', 'СССР', 
					'НАСВАЙ', 'СНЮС', 'ГОСБЮДЖЕТ', 
					'ФОНД БОРЬБЫ С КОРРУПЦИЕЙ', 'МАЙДАН', 'ТЕТРАДЬ СМЕРТИ', 
					'КОДЗИМА', 'МЭДДИСОН', 'ТЕЛЕГРАМ', 
					'SYSTEMD', 'DEBIAN', 'ARCH LINUX', 'АНИМЕ', 'ВОЙНА И МИР', 
					'БИБОРАН', ' СТРУКТУРА ШАУРМЫ НЕ РАЗВАЛИТСЯ', 
					'КАДЫРОВ', 'ПАКЕТ ЯРОВОЙ', 'МИНЕТ', 'ДОНАЛЬД ТРАМП', 'ТРАП', 
					'СЛАДКИЙ ХЛЕБ', 
					'ГАНДОН НЕ ПОРВЕТСЯ', 'КУРГИНЯН', 'УЕБЕР МАРГИНАЛ', 'РАВЕН', 
					'НЛО', 'МОЙ НОСОК', 'ДОКАЗАТЕЛЬСТВО ТЕОРИЕМЫ ПУКАНКАРЕ', 
					'УКРАИНСКИЙ ЯЗЫК', 'АДРОННЫЙ КОЛЛАЙДЕР', 
					'МОИСЕЕВ КОВЧЕГ', 'НАВАЛЬНЫЙ', 'АТЛАС МОЗГА', 'ЧЛЕН НЕ УПАДЕТ', 
					'РУБЛЬ НЕ РУХНЕТ', 'НАВАЛЬНОГО НЕ ВЫБЕРУТ', 'ГАРБИДЖ КОЛЛЕКТОР', 
					'ООП', 'GOOOOGLE', 'RAVEN FM', 'ФЕМИНИЗМ', 'BASH', '']

			shit = ['', '', ' УФ УФ', '', '', '!!111', '!', '!!', '', '', 
					'', '', ' ААААА!!1', '', ' жопа', '', '!111', '', ' ПШ', '', 
					' ЛОЛ', '', '', '', '', '', '', '', '', '', '', '', '!11', '', 
					'', '', '', '', '', '', '', '', '', '', '', '', '', '', 
					' УФ УФ!', '', '', '', '', '']

			work = ['ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ПИЗДИЛИ', 
					'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 
					'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 
					'ДЕЛАЛИ', 'ХУЯЧИЛИ', 'ПИЛИЛИ', 'ХУЯРИЛИ', 
					'ЗАЕБЕНИЛИ', 'ДЕЕЛАЛИ', 'ДЕЛАДИ', 'ДЕЛАЛИ', 'МАСТЕРИЛИ', 
					'ИЗГОТАВЛИВАЛИ', 'ИЗОБРЕТАЛИ', 'НАХУЕВЕРТИЛИ', 
					'ВЫСРАЛИ', 'НАБЫДЛОКОДИЛИ', 'НАЕБАЛИ', 'НАКОСТЫЛЯЛИ', 
					'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 
					'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 
					'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'ДЕЛАЛИ', 'УВЕКОВЕЧИЛИ' ]

			ukr = ['i', 'и', 'и', 'и', 'и', 'и', 'и', 'и', 'и', 'и', 
					'и', 'и', 'и', 'и', 'и', 'и', 'и', 'и', 'и', 'и']

			make = ['ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 
					'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 
					'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 
					'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 
					'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 
					'ГЕНИИ', 'ГЕНИИ', 'ГЕНИИ', 'РУССКИЕ', 
					'ПЕНДОСЫ', 'НАРКОМАНЫ', 'УЗБЕКИ', 'ТАТАРЫ', 'ДЕТИ ИНДИГО', 
					'МОИ СЛУШАТЕЛИ', 'ЛОШАДИ НЕВЗОРОВА', 
					'КУРГИНОИДЫ', 'ФАШИСТЫ', 'ПИДОРЫ', 'РЕПТИЛОИДЫ', 
					'УЧЕНЫЕ', 'ЖИТЕЛИ ХАБАРОВСКА', 'ВЕСЕЛЫЕ САДОВОДЫ', 
					'УНЫЛЫЕ ГОВНОВОЗЫ', 'ДЕДЫ', 'ВЕТЕРАНЫ', 'КОММУНИСТЫ']

			pasta = '<b>mr. Green</b>\nда бля все просто думают т' + \
					random.choice(ukr) + 'па ВОО ' + \
					random.choice(rand_fr) + \
					random.choice(shit) + \
					', ЕБАТЬ...ЕГО ' + \
					random.choice(work) + \
					' БЛЯТЬ ' + random.choice(make) + random.choice(shit) \
					+ '...да блять, все хуйня короче на эф' \
					+ random.choice(ukr) + 'ре раскажу'
			bot.send_message(message.chat.id, pasta, parse_mode="html")
	except:
		pass

if __name__ == '__main__':
	bot.polling(none_stop=True)
