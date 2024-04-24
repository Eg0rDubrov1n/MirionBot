from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


rKB_MainTask = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Играть")]
    ]
)
Finish = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Продолжить")]
    ]
)
rKB_ModeSelection = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Реформы"),KeyboardButton(text="Войны и восстания")],
        [KeyboardButton(text="Битвы"),KeyboardButton(text="Время правления")],
        [KeyboardButton(text="Все темы")]

    ]
)

rKB_InPlay = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/exit",), KeyboardButton(text="Next")]
    ]
)

rKB_NumberOfQuestions = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="5",), KeyboardButton(text="10"), KeyboardButton(text="15")],
        [KeyboardButton(text="20"),KeyboardButton(text="25"),KeyboardButton(text="30")]
    ]
)