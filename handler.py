from bot_config import bot
from telebot import types


answers = {
    'helper': "Сюда можно вставить любое приветственное сообщение с описанием возможностей бота",
    'no_com': "Я не знаю такой команды... Попробуй одну из этих!",
    'in_work': "Эта команда находится в разработке",
    'check_price': "За 70-90 минут активной практики в парах и все вместе можно заплатить 800 рублей.\n\nЕщё можно приобрести абонемент на 4 занятия. Он активен в течение 2 месяцев и стоит 2200. Это меньше 600 рублей за 1 посещение!",
    'payment': "Ура, деньги!",
}


def show_main_menu(chat_id = None):
    markup = types.ReplyKeyboardMarkup()
    buttonPrice = types.KeyboardButton("Хочу знать цену")
    buttonNextDate = types.KeyboardButton("Когда следующий клуб?")
    buttonSignUp = types.KeyboardButton("Как записаться на занятия?")
    buttonGuide = types.KeyboardButton("Гайд по релокации")
    buttonSummerImprove = types.KeyboardButton("Гайд «Как улучшить английский летом»")
    markup.add(buttonPrice, buttonNextDate, buttonSignUp, buttonGuide, buttonSummerImprove)
    if chat_id is None:
        return markup
    else:
        bot.send_message(chat_id, answers['helper'], reply_markup=markup)
        return


def helper(message):
    helper_markup = show_main_menu()
    bot.send_message(message.from_user.id, answers['helper'], reply_markup=helper_markup)


def no_com(message):
    no_com_markup = show_main_menu()
    bot.send_message(message.from_user.id, answers['no_com'], reply_markup=no_com_markup)


def in_work(message):
    in_work_markup = show_main_menu()
    bot.send_message(message.from_user.id, answers['in_work'], reply_markup=in_work_markup)


def check_price(message):
    inline_price_markup = types.InlineKeyboardMarkup()
    buttonPayment = types.InlineKeyboardButton(text='Оплатить', callback_data='pay_button')
    buttonCancel = types.InlineKeyboardButton(text='Отмена', callback_data='cancel_button')
    inline_price_markup.add(buttonPayment, buttonCancel)
    bot.send_message(message.from_user.id, answers['check_price'], reply_markup=inline_price_markup)


def payment(chat_id):
    payment_markup = show_main_menu()
    bot.send_message(chat_id, answers['payment'], reply_markup=payment_markup)
