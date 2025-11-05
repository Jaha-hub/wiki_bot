from aiogram import Router, F
from aiogram.types import CallbackQuery

from aiogram.types.message import Message
from aiogram.fsm.context import FSMContext


from keybords.search import get_article_kb, get_article_link_kb
from keybords.start import get_back_kb, get_start_kb
from services.result import get_result
from services.search import get_wikipedia_results
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
    data = get_wikipedia_results(query)
    if len(data) == 0:
        await message.answer("Мы не нашли совпадений попробуйте ещё раз")
        await state.set_state(SearchForm.query)
        return None

    text = "Выберите статью: \n"
    for i in range(len(data)):
        text += f"\n<b>{i+1}.</b> {data[i].get('title')}"


    await message.answer(text, reply_markup=get_article_kb(data))
    await state.set_state(SearchForm.article)

@router.callback_query(F.data.startswith("article"),SearchForm.article)
async def article_handler(cb: CallbackQuery, state: FSMContext):
    _, pageid = cb.data.split("_")
    pageid = int(pageid)
    text,url = get_result(pageid,"ru")

    await state.update_data(article=cb.data)
    data = await state.get_data()
    print(data)
    await cb.message.delete()
    await cb.message.answer("результат", reply_markup=get_start_kb())
    await cb.message.answer(text,reply_markup=get_article_link_kb(url))
    await state.clear()