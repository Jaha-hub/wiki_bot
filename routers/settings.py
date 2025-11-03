from aiogram import Router,F

from aiogram.types import Message
from keybords.settings import get_lang_kb
from keybords.start import get_back_kb
router = Router()

@router.message(F.text == "⚙️ Настройки")
async def setting_handler(message: Message):
    await message.answer("Настройки",reply_markup=get_back_kb())
    await message.answer("выберите язык:", reply_markup=get_lang_kb())