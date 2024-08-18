from bot_config import bot
from telebot import types
from messages_keeper import answers


def show_main_menu(chat_id = None):
    main_menu_markup = types.ReplyKeyboardMarkup()
    buttonClubInfo = types.KeyboardButton("Расскажи про клуб (что? где? когда?)")
    buttonClubSignUp = types.KeyboardButton("Хочу записаться в клуб!")
    buttonFreeContent = types.KeyboardButton("Мне нужны бесплатные материалы!")
    buttonAdults = types.KeyboardButton("Ты сказал 18+? А что там?")
    main_menu_markup.add(buttonClubInfo, buttonClubSignUp, buttonFreeContent, buttonAdults)
    if chat_id is None:
        return main_menu_markup
    else:
        bot.send_message(chat_id, answers['helper'], reply_markup=main_menu_markup)
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

    @staticmethod
    def free_materials(message):
        free_markup = show_main_menu()
        bot.send_message(message.from_user.id, answers['free_materials'], reply_markup=free_markup)

    @staticmethod
    def for_adults(message):
        adults_markup = show_main_menu()
        bot.send_message(message.from_user.id, answers['for_adults'], reply_markup=adults_markup)

    @staticmethod
    def ready_pay(message):
        ready_pay_markup = types.ReplyKeyboardMarkup()
        buttonPayment = types.KeyboardButton("Всё, оплачиваю!")
        buttonBack = types.KeyboardButton("Обратно в меню")
        ready_pay_markup.add(buttonPayment, buttonBack)
        bot.send_message(message.from_user.id, answers['ready_pay'], reply_markup=ready_pay_markup)


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
    def show_club_video(chat_id, mode):
        if mode == 'online':
            answer = 'Тут будет видео онлайн-клуба'
        elif mode == 'offline':
            answer = 'Тут будет видео офлайн-клуба'
        video_markup = types.ReplyKeyboardMarkup()
        buttonPayment = types.KeyboardButton("Покупаю! Куда платить?")
        buttonBack = types.KeyboardButton("Обратно в меню")
        video_markup.add(buttonPayment, buttonBack)
        bot.send_message(chat_id, answer, reply_markup=video_markup)
