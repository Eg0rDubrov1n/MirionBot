from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

async def WikipediaKeyBoard(questipn):
    print("--->",questipn)
    WikipediaKeyBoard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=f'Wikipedia', url=None,callback_data=f'Wikipedia/{questipn}')]])
    return WikipediaKeyBoard