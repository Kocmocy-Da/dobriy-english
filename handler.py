from bot_config import bot
from telebot import types
from messages_keeper import answers


def show_main_menu(chat_id = None):
    markup = types.ReplyKeyboardMarkup()
    buttonClubInfo = types.KeyboardButton("Расскажи про клуб (что? где? когда?)")
    buttonClubSignUp = types.KeyboardButton("Хочу записаться в клуб!")
    buttonFreeContent = types.KeyboardButton("Мне нужны бесплатные материалы!")
    buttonAdults = types.KeyboardButton("Ты сказал 18+? А что там?")
    markup.add(buttonClubInfo, buttonClubSignUp, buttonFreeContent, buttonAdults)
    if chat_id is None:
        return markup
    else:
        bot.send_message(chat_id, answers['helper'], reply_markup=markup)
        return

class MessageHandlers:
    @staticmethod
    def helper(message):
        helper_markup = show_main_menu()
        bot.send_message(message.from_user.id, answers['helper'], reply_markup=helper_markup)

    @staticmethod
    def no_com(message):
        no_com_markup = show_main_menu()
        bot.send_message(message.from_user.id, answers['no_com'], reply_markup=no_com_markup)

    @staticmethod
    def in_work(message):
        in_work_markup = show_main_menu()
        bot.send_message(message.from_user.id, answers['in_work'], reply_markup=in_work_markup)

    @staticmethod
    def club_info(message):
        inline_club_info_markup = types.InlineKeyboardMarkup()
        buttonOnlineClub = types.InlineKeyboardButton(text='Который онлайн!', callback_data='online_club_button')
        buttonOfflineClub = types.InlineKeyboardButton(text='Хочу ходить лично!', callback_data='offline_club_button')
        inline_club_info_markup.add(buttonOnlineClub, buttonOfflineClub)
        bot.send_message(message.from_user.id, answers['club_info'], reply_markup=inline_club_info_markup)

    @staticmethod
    def show_video(message):
        inline_club_video_markup = types.InlineKeyboardMarkup()
        buttonOnlineVideo = types.InlineKeyboardButton(text='Видео клуба онлайн', callback_data='online_club_video')
        buttonOfflineVideo = types.InlineKeyboardButton(text='Видео клуба оффлайн', callback_data='offline_club_video')
        inline_club_video_markup.add(buttonOnlineVideo, buttonOfflineVideo)
        bot.send_message(message.from_user.id, answers['club_info'], reply_markup=inline_club_video_markup)


class CommandsHandlers:
    @staticmethod
    def show_club_info(chat_id):
        show_club_info_markup = types.ReplyKeyboardMarkup()
        buttonVideoClub = types.KeyboardButton(text='Хочу посмотреть видео, как проходит клуб!')
        buttonPayment = types.KeyboardButton(text='Покупаю! Куда платить?')
        buttonToMenu = types.KeyboardButton(text='Обратно в меню')
        show_club_info_markup.add(buttonVideoClub, buttonPayment, buttonToMenu)
        bot.send_message(chat_id, answers['pre_payment'], reply_markup=show_club_info_markup)

    @staticmethod
    def payment(chat_id):
        payment_markup = MessageHandlers.show_main_menu()
        bot.send_message(chat_id, answers['payment'], reply_markup=payment_markup)
