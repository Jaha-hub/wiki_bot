from aiogram.fsm.state import State, StatesGroup


#StateGroup - группа шагов
class SearchForm(StatesGroup):
    query = State()#Сам шаг
    article = State()
