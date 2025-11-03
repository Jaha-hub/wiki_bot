from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_article_kb(data):
    builder = InlineKeyboardBuilder()
    i = 1
    for article in data:
        builder.button(text=str(i), callback_data=article.get("pageId"))
        i += 1
    return builder.as_markup()