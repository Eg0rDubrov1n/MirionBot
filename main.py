import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from State import s_State
from core.hendlers.Game import Play, PlayMode, Answer, NumberOfQuestions, Help, Wikipedia, Start_Game, bot_Start
from settings import settings


async def Start():
    dp = Dispatcher()
    bot = Bot(settings.bots.bot_token)
    dp.message.register(Help, Command(commands=["help"]))

    dp.message.register(bot_Start,Command(commands=["start"]))

    dp.message.register(Play,Command(commands=["play","exit"]))
    dp.message.register(Play,s_State.Finish, F.text == "Продолжить")

    dp.message.register(Start_Game,F.text == "Играть")
    dp.message.register(NumberOfQuestions, s_State.NumberOfQuestions)
    dp.message.register(PlayMode, s_State.PlayMode)
    # dp.message.register(Question, s_State.Question)
    dp.message.register(Answer, s_State.Answer)

    dp.callback_query.register(Wikipedia, lambda f: f.data.split('/')[0] == "Wikipedia")  # Отправить названия Задачи

    # dp.message.register(Settings,F.text == "Настройки")


    # dp.message.register(Registration,Command(commands=["start"]))
    # dp.message.register(Help,Command(commands=["help"]))
    # # dp.message.register(Check,Command(commands=["check"]))
    #
    # dp.message.register(createTask,F.text == "Создать задачу")
    # dp.message.register(viewingTasks,F.text == "Мои задачи")
    #
    # dp.message.register(SettingsStart,F.text == "Настройки")
    #
    # dp.callback_query.register(settings_URL, F.data == 'url')  # Отправить названия Задачи
    # dp.callback_query.register(settings_folderId, F.data == 'folderID')  # Отправить названия Задачи
    #
    # dp.callback_query.register(createTask_TITLE, F.data == 'createTask_TITLE')  # Отправить названия Задачи
    # dp.callback_query.register(createTask_RESPONSIBLE, F.data == 'createTask_RESPONSIBLE')  # Выбрать специалиста
    # dp.callback_query.register(createTask_UF_CRM_TASK, F.data == 'createTask_UF_CRM_TASK')  # Выбрать специалиста
    # dp.callback_query.register(createTask_DESCRIPTION, F.data == 'createTask_DESCRIPTION')  # Отправить Описание
    # dp.callback_query.register(createTask_GPT_DESCRIPTION, F.data == 'createTask_GPT_DESCRIPTION')
    # dp.callback_query.register(createTask_UF_TASK_WEBDAV_FILES, F.data == 'createTask_UF_TASK_WEBDAV_FILES')  # Отправить ZIP-file
    # dp.callback_query.register(createTask_DEADLINE, F.data == 'createTask_DEADLINE')  # Отправить ZIP-file
    # dp.callback_query.register(createTask_send, F.data.lower() == 'send')  # Сохранить
    # dp.callback_query.register(createTask_exit_In_iKB_CreateTask, F.data == 'exit_In_iKB_CreateTask')  # Сохранить
    # dp.callback_query.register(_exit, F.data == 'exit')
    # dp.callback_query.register(viewingTasks_exit_In_iKB_viewingTasks, F.data == 'exit_iKB_s_Tasks')
    #
    # dp.callback_query.register(m_createTask_GPT_DESCRIPTION_YES, s_CreateTask.DESCRIPTION_GPT, F.data == "yes")  # Отправить ZIP-file
    # dp.callback_query.register(m_createTask_GPT_DESCRIPTION_NO, s_CreateTask.DESCRIPTION_GPT, F.data == 'no')  # Отправить ZIP-file
    #
    # dp.callback_query.register(iKB_s_Lead_UP, s_CreateTask.UF_CRM_TASK, F.data == '>')  # Отправить ZIP-file
    # dp.callback_query.register(iKB_s_Lead_Down, s_CreateTask.UF_CRM_TASK, F.data == '<')  # Отправить ZIP-file
    # dp.callback_query.register(iKB_s_User_UP, s_CreateTask.RESPONSIBLE_ID ,F.data == '>')  # Отправить ZIP-file
    # dp.callback_query.register(iKB_s_User_Down, s_CreateTask.RESPONSIBLE_ID, F.data == '<')  # Отправить ZIP-file
    # dp.callback_query.register(iKB_Callender_Next_mounth, s_CreateTask.DEADLINE, F.data == '>')  # Отправить DEADLINE
    # dp.callback_query.register(iKB_Callender_Last_mounth, s_CreateTask.DEADLINE, F.data == '<')  # Отправить DEADLINE
    # dp.callback_query.register(iKB_s_Tasks_UP, s_Data.Task, F.data == '>')  # Отправить DEADLINE
    # dp.callback_query.register(iKB_s_Tasks_Down, s_Data.Task, F.data == '<')
    #
    # dp.message.register(m_createTask_TITLE, s_CreateTask.TITLE)  # Ввод названия
    # dp.message.register(m_createTask_DESCRIPTION, s_CreateTask.DESCRIPTION)  # Ввод Описания
    # dp.message.register(m_createTask_UF_TASK_WEBDAV_FILES, s_CreateTask.UF_TASK_WEBDAV_FILES, F.document)  # Ввод Zip file
    # dp.callback_query.register(m_createTask_UF_TASK_WEBDAV_FILES_del, s_CreateTask.UF_TASK_WEBDAV_FILES)
    #
    # dp.callback_query.register(m_createTask_DEADLINE, s_CreateTask.DEADLINE)
    # dp.callback_query.register(m_createTask_RESPONSIBLE, s_CreateTask.RESPONSIBLE_ID)
    # dp.callback_query.register(m_createTask_UF_CRM_TASK, s_CreateTask.UF_CRM_TASK)
    #
    # dp.message.register(m_settings_URL, User.URL)
    # dp.message.register(m_settings_folderID, User.folderId)
    #
    # dp.callback_query.register(viewingTaskInfo, s_Data.Task)
    #
    # # dp.message.register(,F.len()>10)
    # dp.message.register(messegeCreateTask,lambda messege: len(messege.text) > 10)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(Start())




