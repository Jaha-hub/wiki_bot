from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_article_kb(data):
    builder = InlineKeyboardBuilder()
    i = 1
    for article in data:
        builder.button(text=str(i), callback_data=f"article_{article.get("pageid")}")
        i += 1
    builder.adjust(5,5)
    return builder.as_markup()

def get_article_link_kb(url, lang="ru"):
    builder = InlineKeyboardBuilder()
    builder.button(text="Просмотр Статьи", url=url)
    return builder.as_markup()