import os
import random

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.utils.chat_action import ChatActionSender

from CONFIG import arr_PlayMode, arr_Question, arr_Answer
from GPT import AiGPT
from State import s_State
from core.keyboards.inline import WikipediaKeyBoard
from core.keyboards.reply import rKB_ModeSelection, rKB_MainTask, rKB_InPlay, rKB_NumberOfQuestions, Finish


async def Help(message: Message, state: FSMContext):
    pass

async def bot_Start(message: Message, state: FSMContext):
    await message.answer(text="Приветствую тебя, будущий 100 бальник ЕГЭ! "
                              "Добро пожаловать в наш уютный уголок знаний, "
                              "где мы вместе разберёмся в исторических тонкостях и подготовимся к главному экзамену твоей жизни. "
                              "Этот бот создан специально для тех, кто стремится стать настоящим знатоком истории и показать свои знания на экзамене. "
                              "Вместе мы пройдём через все испытания, и ты сможешь легко запомнить все важные даты. "
                              "Мы будем поддерживать тебя на каждом шагу, поэтому обязательно ознакомься с инструкцией, чтобы обучение было максимально эффективным. "
                              "Удачи тебе, будущий победитель!", reply_markup=Finish)
    await state.set_state(s_State.Finish)


async def Play(message: Message, state: FSMContext, bot:Bot):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_sticker(message.chat.id,sticker="CAACAgIAAxkBAAEL-jhmJ-3Y5GE35ZZgEELoH2VE0tqv9wACBTUAAvVE-UnZVYpCYJwJCDQE")
    await message.answer(text="<em>Хочешь подтянуть свои знания истории</em>", reply_markup=rKB_MainTask,parse_mode="HTML")
async def Start_Game(message: Message, state: FSMContext):
    print("Play")
    await state.clear()
    # await state.set_state(s_State.PlayMode)
    await state.set_state(s_State.NumberOfQuestions)
    await state.update_data(answeredQuestion=list())
    await state.update_data(Correct_answers_m=0)
    await state.update_data(NumberOfQuestions_answers=0)
    await state.update_data(Start_Messege_Id=message.message_id)

    # await message.answer(text="Выберите режим:", reply_markup=rKB_ModeSelection)
    await message.answer(text="<em>Выбери количество вопросов:</em>", reply_markup=rKB_NumberOfQuestions, parse_mode="HTML")

async def NumberOfQuestions(message: Message, state: FSMContext, bot:Bot):
    try:
        await state.update_data(NumberOfQuestions=int(message.text))
        await state.set_state(s_State.PlayMode)
        await message.answer(text="<em>Выбери тему подготовки:</em>", reply_markup=rKB_ModeSelection, parse_mode="HTML")
    except Exception as error:
        print(error)
        await bot.send_sticker(message.chat.id,
                               sticker="CAACAgIAAxkBAAEL-kBmJ_J6fboxOYEcWhTTsIsbHdm-uAACHzUAAoDH-Enfbde91kzF9DQE")
        await message.answer(text="<em>НУЖНО ВВЕСТИ ЧИСЛО!!!</em>",parse_mode="HTML")
        await state.set_state(s_State.NumberOfQuestions)
        await bot.delete_message(message.chat.id,message.message_id)






async def PlayMode(message: Message, state: FSMContext, bot:Bot):
    print("PlayMode")
    data = await state.get_data()

    if message.text == "Реформы" or message.text == "Войны и восстания" or\
         message.text == "Время правления" or message.text == "Битвы" or message.text == "Все темы":
        print("PlayMode2")
        await bot.delete_messages(message.chat.id, range(message.message_id, data.get("Start_Messege_Id")-1,-1))
        await message.answer(text="<em>Начнем...</em>", reply_markup=rKB_InPlay, parse_mode="HTML")
        await state.update_data(PlayMode=arr_PlayMode[message.text])
        await state.set_state(s_State.Question)
        await Question(message,state)
    else:
        await bot.send_sticker(message.chat.id,
                               sticker="CAACAgIAAxkBAAEL-kBmJ_J6fboxOYEcWhTTsIsbHdm-uAACHzUAAoDH-Enfbde91kzF9DQE")
        await message.answer(text="<em>НУЖНО ВЫБРАТЬ СУЩЕСТВУЮЩУЮ ТЕМУ!!!</em>", parse_mode="HTML")
        await bot.delete_message(message.chat.id,message.message_id)


async def QuestionRandom(question, state):
    data = await state.get_data()
    if question < 0:
        question = random.randint(0, 4)
    answeredQuestion = data.get("answeredQuestion")
    randomMeaning = random.randint(0, len(arr_Question[question]) - 1)
    while (question,randomMeaning) in answeredQuestion:
        randomMeaning = random.randint(0, len(arr_Question[question]) - 1)
    answeredQuestion.append((question,randomMeaning))
    await state.update_data(answeredQuestion=answeredQuestion)
    return (question,randomMeaning)


async def Question(message: Message, state: FSMContext):
    print("Question")
    data = await state.get_data()
    await state.set_state(s_State.Answer)
    iQuestion = await QuestionRandom(data.get("PlayMode"), state)
    await message.answer(text=f" <b>--------------ВОПРОС-------------- </b>", parse_mode="HTML")
    await message.answer(text=f" <em>{arr_Question[iQuestion[0]][iQuestion[1]]} </em>", parse_mode="HTML")
    await state.update_data(Question=iQuestion)
    await state.set_state(s_State.Answer)


async def Answer(message: Message, state: FSMContext,bot:Bot):
    print("Answer")

    data = await state.get_data()
    # GPT = await AiGPT(arr_Question[data.get("Question")[0]][data.get("Question")[1]])

    if arr_Answer[data.get("Question")[0]][data.get("Question")[1]] in message.text:
        await state.update_data(Correct_answers_m=data.get("Correct_answers_m") + 1)
        await message.answer(text="Правильный ответ")
    else:
        if message.text != "Next":
            await bot.send_sticker(message.chat.id,
                               sticker="CAACAgIAAxkBAAEL-jxmJ-5sT8Ms2wsrnDR3Zx3noRPQhQACWjcAAlrU8Ulm4AVBc4WMFzQE")
        print("+++",arr_Question[data.get("Question")[0]][data.get("Question")[1]])

        try:
            await message.answer(
                text=f"<b>Ответ неверный\nПравильный ответ:</b> <tg-spoiler>{arr_Answer[data.get('Question')[0]][data.get('Question')[1]]}</tg-spoiler>",
                parse_mode="HTML",
                reply_markup=await WikipediaKeyBoard(arr_Question[data.get("Question")[0]][data.get("Question")[1]]))
        except Exception as error:
            print(error)
            await message.answer(text=f"<b>Ответ неверный\nПравильный ответ:</b> <tg-spoiler>{arr_Answer[data.get('Question')[0]][data.get('Question')[1]]}</tg-spoiler>", parse_mode="HTML")

    # await message.answer(text=f"<b>{GPT}</b>", parse_mode="HTML")


    await state.update_data(NumberOfQuestions_answers=int(data.get("NumberOfQuestions_answers")) + 1)
    data = await state.get_data()
    if data.get("NumberOfQuestions_answers") < data.get("NumberOfQuestions"):
        await state.set_state(s_State.Question)
        await Question(message,state)
    else:
        Prosent = int(data.get('Correct_answers_m')/data.get('NumberOfQuestions')*100)
        directory = f'video/{Prosent//20}'
        print(fr'video/{Prosent//20}/{random.randint(1,len(os.listdir(directory)))}.gif')
        video = FSInputFile(fr'video/{Prosent//20}/{random.randint(1,len(os.listdir(directory)))}.gif')

        await bot.send_video(message.chat.id, video)
        await message.answer(text=f"Верно{data.get('Correct_answers_m')}/{data.get('NumberOfQuestions')}",reply_markup=Finish)
        # await g_Start(message,state,bot)
        await state.set_state(s_State.Finish)

async def Wikipedia2(call: CallbackQuery, state: FSMContext,bot:Bot):
    import wikipedia
    wikipedia.set_lang("ru")
    # распечатать резюме того, что такое питон

    Question = call.data.split('/')
    print()
    # # wikipedia.summary("Присоединение Новгорода к Москве")

    async with ChatActionSender.typing(call.message.chat.id, bot):
        await bot.edit_message_text(text=f"{wikipedia.summary(Question[1])}{wikipedia.page(Question[1]).url}\n",
                                    chat_id=call.message.chat.id, message_id=call.message.message_id)
async def Wikipedia(call: CallbackQuery, state: FSMContext,bot:Bot):
    await Wikipedia2(call, state,bot)
    data = await state.get_data()
    print(data.get("Question"))
    if data.get("Question"):
        await state.set_state(s_State.Answer)


