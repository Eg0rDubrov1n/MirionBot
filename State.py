import datetime
from aiogram.fsm.state import StatesGroup, State

class s_State(StatesGroup):
    PlayMode = State()
    Question = State()
    Answer = State()

    Finish = State()

    answeredQuestion = State()

    NumberOfQuestions = State()
    NumberOfQuestions_answers = State()
    Correct_answers_m = State()


    Start_Messege_Id = State()

