import wikipedia

def get_result(pageid: int, lang:str ):
    wikipedia.set_lang(lang)
    page = wikipedia.page(pageid=pageid)
    text = f"<b>{page.title}</b>\n\n{page.summary}"
    return text, page.url
