from aiogram import Router, F
from aiogram.types import CallbackQuery

from aiogram.types.message import Message
from aiogram.fsm.context import FSMContext

from keybords.search import get_article_kb
from keybords.start import get_back_kb

from states.search import SearchForm

router = Router()

@router.message(F.text =="🔎 поиск")
async def search_handler(message: Message, state: FSMContext):
    await message.answer("Что вы ищите", reply_markup=get_back_kb())
    await state.set_state(SearchForm.query)

@router.message(F.text, SearchForm.query)
async def get_search_text_handler(message: Message, state: FSMContext):
    await state.update_data(query=message.text) # {"query": text}
    query = message.text
    # Логика поиска
    data = [
        {
            "pageId": "1234",
        },
        {
            "pageId": "12",
        }
    ]
    await message.answer("Выберите статью: ",reply_markup=get_article_kb(data))
    await state.set_state(SearchForm.article)

@router.callback_query(F.data.isdigit(),SearchForm.article)
async def article_handler(cb: CallbackQuery, state: FSMContext):
    await state.update_data(article=cb.data)
    data = await state.get_data()
    print(data)