import telebot
from telebot import types

bot = telebot.TeleBot('5359221630:AAGb2SpYwd2TjBUKQPO7mXdTpYnS0bgyeTs')
messOne = f"Choose the language.\nВыбирите язык.\nTilni tanlang.\n/english - English language\n/russian -Русский язык\n/uzbek - O'zbek tili"


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Choose the language.\nВыбирите язык.\nTilni tanlang.\n/english - English language\n/russian -Русский язык\n/uzbek - O'zbek tili"
    bot.send_message(message.chat.id, messOne, parse_mode='html')


@bot.message_handler(commands=['english'])
def english(message):
    if message.text == '/english':
        mess = f"Hi, <b>{message.from_user.first_name}</b> Do you want to be aware of all the events on the Atom channel?\nAnswer <b>Yes</b> or <b>No</b>"
        bot.send_message(message.chat.id, mess, parse_mode='html')

        @bot.message_handler(commands=["channels"])
        def podpiska(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Are you subscribed to YouTube channel?",
                                                  url="https://youtube.com/channel/UC7Ro8hfryNPVgXAJzroP17w"))
            markup.add(types.InlineKeyboardButton("Are you subscribed to Telegramm channel?",
                                                  url="https://t.me/Atom_Youtube_novosti"))
            button3 = types.InlineKeyboardButton('I subscribed', callback_data="user")
            markup.add(button3)
            bot.send_message(message.chat.id, "Channels:", reply_markup=markup)

        @bot.message_handler(commands=['programmer'])
        def programmer(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton("I want to order my bot.",
                                           url="https://t.me/Diyorbekdavronov07072007"))
            bot.send_message(message.chat.id, 'Creator:', reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.data == "user":
                try:
                    abcd = False
                    a = bot.get_chat_member(chat_id='@Atom_Youtube_novosti',
                                            user_id=call.from_user.id)
                    if not a.status == 'left':
                        bot.answer_callback_query(call.id, text="You passed the test",
                                                  show_alert=True)
                        abcd = True
                    else:
                        bot.answer_callback_query(call.id, text="Goog job!", show_alert=True)
                except:
                    bot.answer_callback_query(call.id, text="Well done!", show_alert=True)

        @bot.message_handler(commands=['social'])
        def social_media(message):
            markup = types.InlineKeyboardMarkup(row_width=1)
            sayti = types.InlineKeyboardButton('My website with information about my channel',
                                               url="https://sites.google.com/view/atom-ytb-sayt/%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
            viber = types.InlineKeyboardButton('My channel in viber',
                                               url='https://invite.viber.com/?g2=AQAeSkWE%2B9Mg4E8p92MytlKXQRx2raUfRsuYddYgeVpXROvQf74G4k2YlHWZ5hYP&lang=ru')
            pochta = types.InlineKeyboardButton('My e-mail', url='atomytbvoprosi@gmail.com')
            discord = types.InlineKeyboardButton('Discord server',
                                                 url='https://discord.gg/JK9RrDAaDC')
            markup.add(sayti, viber, pochta, discord)
            bot.send_message(message.chat.id, "My social networks:", reply_markup=markup)

        @bot.message_handler(commands=["menu"])
        def butons(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            youtube = types.KeyboardButton(
                'YouTube channel')  # , url='https://youtube.com/channel/UC7Ro8hfryNPVgXAJzroP17w')
            telegram = types.KeyboardButton(
                'Telegram channel')  # , url='https://t.me/Atom_Youtube_novosti')
            infa = types.KeyboardButton(
                'Information about Atom')  # ,callback_data="info_about_atom")
            markup.add(youtube, telegram, infa)
            bot.send_message(message.chat.id, "Menu:", reply_markup=markup)

        @bot.message_handler(commands=["new"])
        def butons(message):
            a = "https://youtube.com/shorts/9gI9TlHcbR4?feature=share"
            bot.send_message(message.chat.id, "New video:")
            bot.send_message(message.chat.id, a)

        @bot.message_handler()
        def text_from_user(message):
            if message.text == 'Yes' or 'YES' or 'yes' or 'YEs':
                men = 'Well done! You are a loyal subscriber because you found my bot.\nAll available commands are in the menu.'
                bot.send_message(message.chat.id, men, )
            elif message.text == 'YouTube channel':
                g = 'Subscribe to YouTube channel:'
                yt = 'https://youtube.com/channel/UC7Ro8hfryNPVgXAJzroP17w '
                bot.send_message(message.chat.id, g)
                bot.send_message(message.chat.id, yt)
            elif message.text == 'No' and 'no' and 'nO' and 'NO':
                g = "So, then you don't need this bot! Bye!"
                bot.send_message(message.chat.id, g)
            elif message.text == 'Telegram channel':
                b = 'Subscribe to Telegram channel:'
                y = 'https://t.me/Atom_Youtube_novosti'
                bot.send_message(message.chat.id, b)
                bot.send_message(message.chat.id, y)
            elif message.text == 'Information about Atom':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                decription = types.KeyboardButton('About channel Atom')
                photo_atom = types.KeyboardButton('Photo of Atom')
                soci = types.KeyboardButton('Social networks')
                minecraft = types.KeyboardButton('Minecraft server')
                video = types.KeyboardButton('Most Viewed Atom Video')
                shorts = types.KeyboardButton("Atom's most popular shorts")
                markup.add(decription, photo_atom, soci, minecraft, video, shorts)
                bot.send_message(message.chat.id, "Information about the Atom:",
                                 reply_markup=markup)
            elif message.text == 'About channel Atom':
                desc = 'Description of the Atom channel:'
                desc2 = "Hi all! My name is Atom. I shoot completely different content. And of course, I have different chips, but you will learn the rest in my videos. Subscribe!"
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
            elif message.text == 'Photo of Atom':
                photo = open('C:/Users/Diyorbek/PycharmProjects/Atom/venv/title.png', 'rb')
                photo2 = open('C:/Users/Diyorbek/PycharmProjects/Atom/venv/icon.png', 'rb')
                bot.send_photo(message.chat.id, photo=photo)
                bot.send_photo(message.chat.id, photo=photo2)
            elif message.text == 'Social networks':
                markup = types.InlineKeyboardMarkup(row_width=1)
                sayti = types.InlineKeyboardButton('My website with information about my channel',
                                                   url="https://sites.google.com/view/atom-ytb-sayt/%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
                viber = types.InlineKeyboardButton('My Viber channel',
                                                   url='https://invite.viber.com/?g2=AQAeSkWE%2B9Mg4E8p92MytlKXQRx2raUfRsuYddYgeVpXROvQf74G4k2YlHWZ5hYP&lang=ru')
                pochta = types.InlineKeyboardButton('My e-mail', url='atomytbvoprosi@gmail.com')
                discord = types.InlineKeyboardButton('Discord server',
                                                     url='https://discord.gg/JK9RrDAaDC')
                markup.add(sayti, viber, pochta, discord)
                bot.send_message(message.chat.id, "My social networks:", reply_markup=markup)
            elif message.text == 'Minecraft server':
                desc = 'Minecraft Atom Server.\nIp address:'
                desc2 = 'Atom_Games.aternos.me'
                mesu = 'Log in from your computer and play with the Atom'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'Most Viewed Atom Video':
                desc = "Here is his most popular video (It's about minecraft):"
                desc2 = 'https://youtu.be/4bOp621eZEo'
                mesu = 'Be sure to check it out too, keep up with the trend!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
                bot.send_message(message.chat.id, mesu)
            elif message.text == "Atom's most popular shorts":
                desc = 'Here are his most popular shorts:'
                desc2 = 'https://youtube.com/shorts/bRGz9XFwrmo?feature=share'
                mesu = 'Be sure to check it out too, keep up with the trend!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
                bot.send_message(message.chat.id, mesu)
    else:
        bot.send_message(message.chat.id, messOne)


@bot.message_handler(commands=['russian'])
def english(message):
    if message.text == '/russian':
        mess = f"Привет, <b>{message.from_user.first_name}</b> хочешь быть в курсе всех событий на канале Атом?\nОтвечай <b>Да</b> или <b>Нет</b>"
        bot.send_message(message.chat.id, mess, parse_mode='html')

        @bot.message_handler(commands=["channels"])
        def podpiska(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Ты подписан на YouTube канал?",
                                                  url="https://youtube.com/channel/UC7Ro8hfryNPVgXAJzroP17w"))
            markup.add(
                types.InlineKeyboardButton("Ты подписан на телеграм канал?",
                                           url="https://t.me/Atom_Youtube_novosti"))
            button3 = types.InlineKeyboardButton('Я подписался', callback_data="user")
            markup.add(button3)
            bot.send_message(message.chat.id, "Каналы:", reply_markup=markup)

        @bot.message_handler(commands=['programmer'])
        def programmer(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Хочу заказать своего бота. Платно?",
                                                  url="https://t.me/Diyorbekdavronov07072007"))
            bot.send_message(message.chat.id, 'Создатель бота:', reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.data == "user":
                try:
                    abcd = False
                    a = bot.get_chat_member(chat_id='@Atom_Youtube_novosti',
                                            user_id=call.from_user.id)
                    if not a.status == 'left':
                        bot.answer_callback_query(call.id, text="Ты прошёл проверку",
                                                  show_alert=True)
                        abcd = True
                    else:
                        bot.answer_callback_query(call.id, text="Отлично!", show_alert=True)
                except:
                    bot.answer_callback_query(call.id, text="Молодец!", show_alert=True)

        @bot.message_handler(commands=['social'])
        def social_media(message):
            markup = types.InlineKeyboardMarkup(row_width=1)
            sayti = types.InlineKeyboardButton('Мой сайт с информацией о моём канале',
                                               url="https://sites.google.com/view/atom-ytb-sayt/%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
            viber = types.InlineKeyboardButton('Мой канал в Viber',
                                               url='https://invite.viber.com/?g2=AQAeSkWE%2B9Mg4E8p92MytlKXQRx2raUfRsuYddYgeVpXROvQf74G4k2YlHWZ5hYP&lang=ru')
            pochta = types.InlineKeyboardButton('Моя почта', url='atomytbvoprosi@gmail.com')
            discord = types.InlineKeyboardButton('Дискорд сервер',
                                                 url='https://discord.gg/JK9RrDAaDC')
            markup.add(sayti, viber, pochta, discord)
            bot.send_message(message.chat.id, "Мои социальные сети:", reply_markup=markup)

        @bot.message_handler(commands=["menu"])
        def butons(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            youtube = types.KeyboardButton(
                'YouTube канал')  # , url='https://youtube.com/channel/UC7Ro8hfryNPVgXAJzroP17w')
            telegram = types.KeyboardButton(
                'Телеграмм канал')  # , url='https://t.me/Atom_Youtube_novosti')
            infa = types.KeyboardButton('Информация об Атоме')  # ,callback_data="info_about_atom")
            markup.add(youtube, telegram, infa)
            bot.send_message(message.chat.id, "Меню:", reply_markup=markup)

        @bot.message_handler(commands=["new"])
        def butons(message):
            a = "https://youtube.com/shorts/9gI9TlHcbR4?feature=share"
            bot.send_message(message.chat.id, "Новое видео:")
            bot.send_message(message.chat.id, a)

        @bot.message_handler()
        def text_from_user(message):
            if message.text == 'Да' or 'ДА' or 'да' or 'дА':
                men = 'Молодец! Ты преданый подписчик, потому что ты нашёл моего бота.\nВсе доступные команды в меню.'
                bot.send_message(message.chat.id, men, )
            elif message.text == 'YouTube канал':
                g = 'Подпишись на YouTube канал:'
                yt = 'https://youtube.com/channel/UC7Ro8hfryNPVgXAJzroP17w '
                bot.send_message(message.chat.id, g)
                bot.send_message(message.chat.id, yt)
            elif message.text == 'Нет' and 'НЕт' and 'нет' and 'нЕт':
                g = 'Так, тогда тебе не нужен этот бот!Пока!'
                bot.send_message(message.chat.id, g)
            elif message.text == 'Телеграмм канал':
                b = 'Подпишись на Телеграмм канал:'
                y = 'https://t.me/Atom_Youtube_novosti'
                bot.send_message(message.chat.id, b)
                bot.send_message(message.chat.id, y)
            elif message.text == 'Информация об Атоме':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                decription = types.KeyboardButton('О канале Атом')
                photo_atom = types.KeyboardButton('Фото Атома')
                soci = types.KeyboardButton('Социальные сети')
                minecraft = types.KeyboardButton('Minecraft Сервер')
                video = types.KeyboardButton('Самое популярное видео Атома')
                shorts = types.KeyboardButton('Самое популярный shorts Атома')
                markup.add(decription, photo_atom, soci, minecraft, video, shorts)
                bot.send_message(message.chat.id, "Информация об Атоме:", reply_markup=markup)
            elif message.text == 'О канале Атом':
                desc = 'Описание канала Атом:'
                desc2 = 'Всем привет! Меня зовут Атом. Я снимаю абсолютно разный контент. Ну и конечно же у меня есть разные фишки, ну а остальное ты узнаешь в моих роликах. Подпишись!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
            elif message.text == 'Фото Атома':
                photo = open('C:/Users/Diyorbek/PycharmProjects/Atom/venv/title.png', 'rb')
                photo2 = open('C:/Users/Diyorbek/PycharmProjects/Atom/venv/icon.png', 'rb')
                bot.send_photo(message.chat.id, photo=photo)
                bot.send_photo(message.chat.id, photo=photo2)
            elif message.text == 'Социальные сети':
                markup = types.InlineKeyboardMarkup(row_width=1)
                sayti = types.InlineKeyboardButton('Мой сайт с информацией о моём канале',
                                                   url="https://sites.google.com/view/atom-ytb-sayt/%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
                viber = types.InlineKeyboardButton('Мой канал в Viber',
                                                   url='https://invite.viber.com/?g2=AQAeSkWE%2B9Mg4E8p92MytlKXQRx2raUfRsuYddYgeVpXROvQf74G4k2YlHWZ5hYP&lang=ru')
                pochta = types.InlineKeyboardButton('Моя почта', url='atomytbvoprosi@gmail.com')
                discord = types.InlineKeyboardButton('Дискорд сервер',
                                                     url='https://discord.gg/JK9RrDAaDC')
                markup.add(sayti, viber, pochta, discord)
                bot.send_message(message.chat.id, "Мои социальные сети:", reply_markup=markup)
            elif message.text == 'Minecraft Сервер':
                desc = 'Minecraft Сервер Атома.\nIp адрес:'
                desc2 = 'Atom_Games.aternos.me'
                mesu = 'Заходи с компьютера и играй вместе с Атомом'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'Самое популярное видео Атома':
                desc = 'Вот его самое популярное видео(Оно про майнкрафт):'
                desc2 = 'https://youtu.be/4bOp621eZEo'
                mesu = 'Ты тоже обязательно посмотри его,не отставай от тренда!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'Самое популярный shorts Атома':
                desc = 'Вот его самый популярный shorts:'
                desc2 = 'https://youtube.com/shorts/bRGz9XFwrmo?feature=share'
                mesu = 'Ты тоже обязательно посмотри его,не отставай от тренда!'
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
                bot.send_message(message.chat.id, mesu)


@bot.message_handler(commands=['uzbek'])
def english(message):
    if message.text == '/uzbek':
        mess = f"Salom, <b>{message.from_user.first_name}</b> Atom kanalidagi barcha voqealardan xabardor bo'lishni xohlaysizmi?\nJavob bering <b>Ha</b> yoki <b>Yoq</b>"
        bot.send_message(message.chat.id, mess, parse_mode='html')

        @bot.message_handler(commands=["channels"])
        def podpiska(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("YouTube kanaliga obuna bo'ldingizmi?",
                                                  url="https://youtube.com/channel/UC7Ro8hfryNPVgXAJzroP17w"))
            markup.add(types.InlineKeyboardButton("Siz Telegram kanaliga obuna bo'ldingizmi?",
                                                  url="https://t.me/Atom_Youtube_novosti"))
            button3 = types.InlineKeyboardButton("Obuna bo'ldim", callback_data="user")
            markup.add(button3)
            bot.send_message(message.chat.id, "Kanallar:", reply_markup=markup)

        @bot.message_handler(commands=['programmer'])
        def programmer(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Men botimga buyurtma bermoqchiman.",
                                                  url="https://t.me/Diyorbekdavronov07072007"))
            bot.send_message(message.chat.id, 'Bot yaratuvchisi:', reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.data == "user":
                try:
                    abcd = False
                    a = bot.get_chat_member(chat_id='@Atom_Youtube_novosti',
                                            user_id=call.from_user.id)
                    if not a.status == 'left':
                        bot.answer_callback_query(call.id, text="Siz sinovdan o'tdingiz",
                                                  show_alert=True)
                        abcd = True
                    else:
                        bot.answer_callback_query(call.id, text="Ajoyib!", show_alert=True)
                except:
                    bot.answer_callback_query(call.id, text="Barakalla!", show_alert=True)

        @bot.message_handler(commands=['social'])
        def social_media(message):
            markup = types.InlineKeyboardMarkup(row_width=1)
            sayti = types.InlineKeyboardButton(
                "Mening kanalim haqidagi ma'lumotlarga ega veb-saytim",
                url="https://sites.google.com/view/atom-ytb-sayt/%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
            viber = types.InlineKeyboardButton('Mening Viber kanalim',
                                               url='https://invite.viber.com/?g2=AQAeSkWE%2B9Mg4E8p92MytlKXQRx2raUfRsuYddYgeVpXROvQf74G4k2YlHWZ5hYP&lang=ru')
            pochta = types.InlineKeyboardButton('Mening elektron pochtam',
                                                url='atomytbvoprosi@gmail.com')
            discord = types.InlineKeyboardButton('Discord serveri',
                                                 url='https://discord.gg/JK9RrDAaDC')
            markup.add(sayti, viber, pochta, discord)
            bot.send_message(message.chat.id, "Mening ijtimoiy tarmoqlarim:", reply_markup=markup)

        @bot.message_handler(commands=["menu"])
        def butons(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            youtube = types.KeyboardButton(
                'YouTube kanali')  # , url='https://youtube.com/channel/UC7Ro8hfryNPVgXAJzroP17w')
            telegram = types.KeyboardButton(
                'Telegram kanali')  # , url='https://t.me/Atom_Youtube_novosti')
            infa = types.KeyboardButton("Atom haqida ma'lumot")  # ,callback_data="info_about_atom")
            markup.add(youtube, telegram, infa)
            bot.send_message(message.chat.id, "Menyu:", reply_markup=markup)

        @bot.message_handler(commands=["new"])
        def butons(message):
            a = "https://youtube.com/shorts/9gI9TlHcbR4?feature=share"
            bot.send_message(message.chat.id, "Yangi video:")
            bot.send_message(message.chat.id, a)

        @bot.message_handler()
        def text_from_user(message):
            if message.text == 'Ha' or 'HA' or 'ha' or 'hA':
                men = 'Barakalla! Siz sodiq obunachisiz, chunki siz mening botimni topdingiz.\nBarcha mavjud buyruqlar menyuda.'
                bot.send_message(message.chat.id, men, )
            elif message.text == 'YouTube kanali':
                g = "YouTube kanaliga obuna bo'ling:"
                yt = 'https://youtube.com/channel/UC7Ro8hfryNPVgXAJzroP17w '
                bot.send_message(message.chat.id, g)
                bot.send_message(message.chat.id, yt)
            elif message.text == 'Yoq' and 'YOq' and 'yoq' and 'yOq':
                g = 'Demak, sizga bu bot kerak emas!Hayer!'
                bot.send_message(message.chat.id, g)
            elif message.text == 'Telegram kanali':
                b = "Telegram kanaliga obuna bo'ling:"
                y = 'https://t.me/Atom_Youtube_novosti'
                bot.send_message(message.chat.id, b)
                bot.send_message(message.chat.id, y)
            elif message.text == "Atom haqida ma'lumot:":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                decription = types.KeyboardButton('Atom kanali haqida')
                photo_atom = types.KeyboardButton('Atom rasmlari')
                soci = types.KeyboardButton('Ijtimoiy tarmoqlar')
                minecraft = types.KeyboardButton('Minecraft server')
                video = types.KeyboardButton("Eng ko'p ko'rilgan Atom videosi")
                shorts = types.KeyboardButton("Atomning eng mashhur short videosi")
                markup.add(decription, photo_atom, soci, minecraft, video, shorts)
                bot.send_message(message.chat.id, "Atom haqida ma'lumot:", reply_markup=markup)
            elif message.text == 'Atom kanali haqida':
                desc = 'Atom kanalining tavsifi:'
                desc2 = "Hammaga salom! Mening ismim Atom. Men butunlay boshqacha tarkibni video olaman. Va, albatta, menda turli xil chiplar bor, ammo qolganlarini videolarimdan bilib olasiz. Obuna bo'ling!"
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
            elif message.text == 'Atom rasmlari':
                photo = open('C:/Users/Diyorbek/PycharmProjects/Atom/venv/title.png', 'rb')
                photo2 = open('C:/Users/Diyorbek/PycharmProjects/Atom/venv/icon.png', 'rb')
                bot.send_photo(message.chat.id, photo=photo)
                bot.send_photo(message.chat.id, photo=photo2)
            elif message.text == 'Ijtimoiy tarmoqlar':
                markup = types.InlineKeyboardMarkup(row_width=1)
                sayti = types.InlineKeyboardButton(
                    "Mening kanalim haqidagi ma'lumotlarga ega veb-saytim",
                    url="https://sites.google.com/view/atom-ytb-sayt/%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
                viber = types.InlineKeyboardButton('Mening Viber kanalim',
                                                   url='https://invite.viber.com/?g2=AQAeSkWE%2B9Mg4E8p92MytlKXQRx2raUfRsuYddYgeVpXROvQf74G4k2YlHWZ5hYP&lang=ru')
                pochta = types.InlineKeyboardButton('Mening elektron pochtam',
                                                    url='atomytbvoprosi@gmail.com')
                discord = types.InlineKeyboardButton('Discord serveri',
                                                     url='https://discord.gg/JK9RrDAaDC')
                markup.add(sayti, viber, pochta, discord)
                bot.send_message(message.chat.id, " Mening ijtimoiy tarmoqlarim:",
                                 reply_markup=markup)
            elif message.text == 'Minecraft server':
                desc = 'Minecraft atom serveri.\nIp manzil:'
                desc2 = 'Atom_Games.aternos.me'
                mesu = "Kompyuteringizdan tizimga kiring va Atom bilan o'ynang"
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
                bot.send_message(message.chat.id, mesu)
            elif message.text == "Eng ko'p ko'rilgan Atom videosi":
                desc = 'Mana uning eng mashhur videosi (bu minecraft haqida):'
                desc2 = 'https://youtu.be/4bOp621eZEo'
                mesu = "Buni ham tekshirib ko'ring, trendni kuzatib boring!"
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
                bot.send_message(message.chat.id, mesu)
            elif message.text == 'Atomning eng mashhur short videosi':
                desc = 'Mana uning eng mashhur short vidoisi:'
                desc2 = 'https://youtube.com/shorts/bRGz9XFwrmo?feature=share'
                mesu = "Buni ham tekshirib ko'ring, trendni kuzatib boring!"
                bot.send_message(message.chat.id, desc)
                bot.send_message(message.chat.id, desc2)
                bot.send_message(message.chat.id, mesu)


bot.polling(none_stop=True)
