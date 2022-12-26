from typing import Tuple
from vkbottle.api import API
import requests
from datetime import datetime
from bs4 import BeautifulSoup as BS
from vkbottle.user import User,	Message
from vkbottle.dispatch.rules.base import CommandRule

def days():
	date1 = datetime.now()
	date2 = datetime(day=2, month=6, year=2022)
	countdown = date2 - date1
	n = countdown.days
	days = ['день', 'дня', 'дней']
	if n % 10 == 1 and n % 100 != 11:
		p = 0
	elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
		p = 1
	else:
		p = 2
	return str(n) + ' ' + days[p]
ds = 'https://discord.com/invite/HXzE6x4rXN'
token = 'f4a902d8cb04a20a260f6de52c004b3bfba5bbb894062f696eb7ab18ef9328c006a861dc7bd99093f5a7b'

user = User(token)

@user.on.message(CommandRule("stats", ["/", "?"], 1))
async def handler(message: Message, args: Tuple[str]):
	if message.from_id == 183416928:
		await message.answer('poshel naxyi', reply_to=message.id)
	else:
		nick = args[0]
		url = f'https://iccup.com/ru/dota/gamingprofile/{nick}'
		response = requests.get(url)
		Gamingprofile = BS(response.text, 'html.parser')
		text = Gamingprofile.find('div', id = 'main-stata-5x5')
		if text != None:
			Statistics = text.text.replace('\n', '  ').split()
			try:
				main = f"🔮 РЕЙТИНГ аккаунта\n\n 🔰 Логин: {nick}\n 🔝 Положение в рейтинге: {Statistics[21]}\n 🏆 Ранк (pts): {Statistics[0]}\n " \
					   f"⚔️ K/D/A: {Statistics[3]} / {Statistics[5]} / {Statistics[7]}   K {Statistics[9]}\n ❇ Win/Lose/Leave: {Statistics[27]} / {Statistics[29]} / {Statistics[31]}\n " \
					   f"🐊 Нейтралов убито: {Statistics[37]}\n 🐔 Курьеров убито: {Statistics[34]}\n ⏰ Налётанные часы: {Statistics[40]}\n " \
					   f"👑 Победы: {Statistics[42]}\n 💤 Кол-во ливов: {Statistics[45]}\n 📊 Лучший счёт: {Statistics[48]} - {Statistics[50]} - {Statistics[52]}\n " \
					   f"🔱 Макс. стрик побед: {Statistics[56]}\n ⚜ Текущий стрик: {Statistics[59]}\n " \
					   f"🔵 Дискорд: {ds}\n\n ⏳ Конец сезона через: {days()}\n\n"
			except IndexError:
				main = f"🔮 **РЕЙТИНГ аккаунта\n\n 🔰 Логин: {nick}\n 🔝 Положение в рейтинге: {Statistics[21]}\n 🏆 Ранк (pts): {Statistics[0]}\n " \
					   f"⚔️ K/D/A: {Statistics[3]} / {Statistics[5]} / {Statistics[7]}   K {Statistics[9]}\n ❇ Win/Lose/Leave: {Statistics[27]} / {Statistics[29]} / {Statistics[31]}\n " \
					   f"🐊 Нейтралов убито: {Statistics[37]}\n 🐔 Курьеров убито: {Statistics[34]}\n ⏰ Налётанные часы: 0\n " \
					   f"👑 Победы: {Statistics[43]}\n 💤 Кол-во ливов: {Statistics[46]}\n 📊 Лучший счёт: {Statistics[49]}\n " \
					   f"🔱 Макс. стрик побед: {Statistics[53]}\n ⚜ Текущий стрик: {Statistics[56]}\n " \
					   f"🔵 Дискорд: {ds}\n\n ⏳ Конец сезона через: {days()}\n\n"
			await message.answer(main, reply_to=message.id)
		else:
			await message.answer('Такого аккаунта не существует.', reply_to=message.id)

@user.on.message(CommandRule("last", ["/", "?"], 1))
async def lastgame(message: Message, args: Tuple[str]):
	if message.from_id == 183416928:
		await message.answer('poshel naxyi', reply_to=message.id)
	else:
		try:
			nick = args[0]
			url = f'https://iccup.com/ru/dota/gamingprofile/{nick}'
			response = requests.get(url)
			soup = BS(response.text, 'html.parser')
			games = soup.find('tbody', id = 'result-table').find_all('td', limit=5)
			alls = 'ПОСЛЕДНЯЯ ИГРА\n\n👨‍💻 Логин: {0}\n🧜 Герой: {1}\n👟 Мод: {2}\n⏰ Время: {3}\n⚔️ K/D/A: {4}\n🔥 Очки: {5} PTS\n\n⏳ Конец сезона через: {6}'.format(nick, games[0].text.replace('\n', ''), games[1].text.replace('\n', ''), games[2].text.replace('\n', ''), games[3].text.replace('\n', ''), games[4].text.replace('\n', ''), days())
			await message.answer(alls, reply_to=message.id)
		except IndexError:
			await message.answer('Игрок ещё не играл', reply_to=message.id)

@user.on.message(CommandRule("top", ["/", "?"]))
async def top(message: Message):
	if message.from_id == 183416928:
		await message.answer('poshel naxyi', reply_to=message.id)
	else:
		url = 'https://iccup.com/dota/ladder'
		response = requests.get(url)
		soup = BS(response.text, 'html.parser')
		find_pts_players = soup.find_all('div', class_ ="field2 width70p10", limit=5)
		find_stats_players = soup.find_all('div', class_ ="field2 width80c", limit=5)
		find_wrl_players = soup.find_all('div', class_ ="field2 width80r", limit=5)
		find_players = soup.find_all('div', class_ = 'field2 width210 ladder-flag', limit=5)
		toplist = []
		for i in range(0, 5):
			a = f'#{i+1} ', find_players[i].text.replace('\n', ''), find_pts_players[i].text, find_stats_players[i].text, find_wrl_players[i].text
			a = ' '.join(a)
			toplist.append(a)
		out = f'№ | Игрок | Очки | Стата | Победа\n{toplist[0]}\n{toplist[1]}\n{toplist[2]}\n{toplist[3]}\n{toplist[4]}'
		await message.answer(out, reply_to=message.id)

@user.on.message(CommandRule("ladder", ["/", "?"]))
async def ladder(message: Message):
	if message.from_id == 183416928:
		await message.answer('poshel naxyi', reply_to=message.id)
	else:
		url = 'https://iccup.com/dota/teams.html'
		response = requests.get(url)
		GamingProfile = BS(response.text, 'html.parser')
		find_pts_teams = GamingProfile.find_all('div', class_ ="field2 width70", limit=10)
		find_stats_teams = GamingProfile.find_all('div', class_ ="field2 width70c", limit=10)
		find_wrl_teams = GamingProfile.find_all('div', class_ ="field2 width90c", limit=5)
		find_teams = GamingProfile.find_all('div', class_ = 'field2 width200', limit=5)
		toplist = []
		com = [find_stats_teams[n].text + '  '+ find_stats_teams[n+1].text for n in range(0, 10, 2)]
		com2 = [find_pts_teams[j].text for j in range(0,10)]
		del com2[:-1:2]
		for i in range(0, 5):
			a = f'#{i+1} ', find_teams[i].text.replace('\n', ''), ' ', find_wrl_teams[i].text, ' ', com2[i], ' ',com[i]
			a = ' '.join(a)
			toplist.append(a)
		out = f'№ | Команда | Игроки | Стата | Победа\n{toplist[0]}\n{toplist[1]}\n{toplist[2]}\n{toplist[3]}\n{toplist[4]}'
		await message.answer(out, reply_to=message.id)

@user.on.message(CommandRule("profile", ["/", "?"], 1))
async def profile(message: Message, args: Tuple[str]):
	if message.from_id == 183416928:
		await message.answer('poshel naxyi', reply_to=message.id)
	else:
		try:
			nick = args[0]
			url = f'https://iccup.com/ru/profile/view/{nick}'
			response = requests.get(url)
			Profile = BS(response.text, 'html.parser')
			text = Profile.find('div', class_ = 'allinfo width395')
			mesto = text.find('span', class_="user-flag").find('a').attrs['title']
			p1 = text.find('div', class_ ='infoblock-tbl')
			p3 = p1.find_all(class_ = 'nth-2')
			key = [h.text for h in p3]
			profile = f'🔮 ПРОФИЛЬ аккаунта\n\n 👨‍💻 Логин: {nick}\n 🗣 Настоящее имя: {key[0]}\n 🌍 Местоположение: {mesto} ({key[1]})\n ' \
			  f'💬 Скайп: {key[2]}\n 🟣 Дискорд: {key[3]}\n 🔵 ВКонтакте: {key[4]}\n 👀 Возраст: {key[5]}\n ' \
			  f'🖱 Мышка: {key[6]}\n ⌨️ Клавиатура: {key[7]}\n 🎧 Наушники: {key[8]}\n 🌫️ Коврик: {key[9]}\n\n⏳ Конец сезона через: {days()}'
			await message.answer(profile, reply_to=message.id)
		except AttributeError:
			await message.answer('Такого аккаунта не существует.', reply_to=message.id)

@user.on.message(CommandRule("last5", ["/", "?"], 1))
async def lastgames(message: Message, args: Tuple[str]):
	if message.from_id == 183416928:
		await message.answer('poshel naxyi', reply_to=message.id)
	else:
		try:
			nick = args[0]
			url = f'https://iccup.com/ru/dota/gamingprofile/{nick}'
			response = requests.get(url)
			Gamingprofile = BS(response.text, 'html.parser')
			games = Gamingprofile.find('tbody', id = 'result-table')
			array2 = [i.text.replace('\n', '  ') for i in games]
			out = f'№  |  Герой  |  Мод  |  K/D/A  |  Очки\n\n1. {array2[1].strip()}\n\n2. {array2[3].strip()}\n\n3. {array2[5].strip()}\n\n4. {array2[7].strip()}\n\n5. {array2[9].strip()}'
			await message.answer(out, reply_to=message.id)
		except IndexError:
			await message.answer('Игрок ещё не играл.', reply_to=message.id)

user.run_forever()