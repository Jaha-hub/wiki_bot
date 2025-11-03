from aiogram.filters import or_f
from aiogram.filters.command import CommandStart

from aiogram import Router, F
from aiogram.fsm.context import FSMContext

from aiogram.types import Message

from keybords.start import get_start_kb

router = Router()


@router.message(or_f(CommandStart(), F.text == "назад"))
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Hello", reply_markup=get_start_kb())

# @router.message(F.text == "Назад")
# async def get_back_handler(message: Message):
#     await message.answer("Главное",reply_markup=get_start_kb())
