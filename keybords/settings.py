from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_lang_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="🇷🇺", callback_data="land_ru")
    builder.button(text="🇬🇧", callback_data="land_en")
    builder.button(text="", callback_data="land_uz")
    return builder.as_markup()