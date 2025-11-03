from aiogram import Bot , Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from configs import TOKEN
from routers.settings import router as settings_router
from routers.start import router as start_router
from routers.about import router as about_router
from routers.search import router as search_router
properties = DefaultBotProperties(
    parse_mode=ParseMode.HTML
)

bot = Bot(TOKEN, default=properties)
dp = Dispatcher()

#Роутеры

dp.include_router(start_router)
dp.include_router(about_router)
dp.include_router(settings_router)
dp.include_router(search_router)