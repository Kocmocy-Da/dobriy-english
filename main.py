import handler
from bot_config import *

cmds = {
    "/start": handler.helper,
    "начать": handler.helper,
    "help": handler.helper,
    "помощь": handler.helper,
    "команды": handler.helper,
    "привет": handler.helper,
    "хочу знать цену": handler.check_price,
    "когда следующий клуб?": handler.in_work,
    "когда следующий клуб": handler.in_work,
    "как записаться на занятия?": handler.in_work,
    "как записаться на занятия": handler.in_work,
    "гайд по релокации": handler.in_work,
    "гайд «как улучшить английский летом»": handler.in_work,
    "гайд как улучшить английский летом": handler.in_work,
    "как улучшить английский летом": handler.in_work,
}

callbacks = {
    "pay_button": (handler.payment, 'Хорошо! Давай оплачивать!'),
    "cancel_button": (handler.show_main_menu, 'Хорошо! Тогда до следующего раза!'),
}

@bot.message_handler(content_types=['text'])
def on_message(message):
    message_text = message.text.lower().strip()
    try:    
        cmds[message_text](message)
    except KeyError:
        handler.no_com(message)


@bot.callback_query_handler(func=lambda call: call.data in callbacks)
def cancel_btn(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    data = call.data
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=callbacks[data][1]) 
    callbacks[data][0](chat_id)


bot.infinity_polling()
