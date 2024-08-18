import handler
from bot_config import *

cmds = {
    "/start": handler.MessageHandlers.helper,
    "начать": handler.MessageHandlers.helper,
    "help": handler.MessageHandlers.helper,
    "помощь": handler.MessageHandlers.helper,
    "команды": handler.MessageHandlers.helper,
    "привет": handler.MessageHandlers.helper,
    "обратно в меню": handler.MessageHandlers.helper,
    "расскажи про клуб (что? где? когда?)": handler.MessageHandlers.club_info,
    "хочу записаться в клуб!": handler.MessageHandlers.ready_pay,
    "мне нужны бесплатные материалы!": handler.MessageHandlers.free_materials,
    "ты сказал 18+? а что там?": handler.MessageHandlers.for_adults,
    "хочу посмотреть видео, как проходит клуб!": handler.MessageHandlers.show_video,
    "покупаю! куда платить?": handler.MessageHandlers.ready_pay,
    "всё, оплачиваю!": handler.MessageHandlers.in_work,
}

callbacks = {
    "online_club_button": (handler.CommandsHandlers.show_club_info, handler.answers['online_club']),
    "offline_club_button": (handler.CommandsHandlers.show_club_info, handler.answers['offline_club']),
    "online_club_video": (handler.CommandsHandlers.show_club_video, handler.answers['online_club_vid']),
    "offline_club_video": (handler.CommandsHandlers.show_club_video, handler.answers['offline_club_vid']),
}

@bot.message_handler(content_types=['text'])
def on_message(message):
    message_text = message.text.lower().strip()
    try:    
        cmds[message_text](message)
    except KeyError:
        handler.MessageHandlers.no_com(message)


@bot.callback_query_handler(func=lambda call: call.data in callbacks)
def cancel_btn(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    data = call.data
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=callbacks[data][1])
    if data == 'online_club_video':
        callbacks[data][0](chat_id, 'online')
    elif data == 'offline_club_video':
        callbacks[data][0](chat_id, 'offline')
    else:
        callbacks[data][0](chat_id)


bot.infinity_polling()
