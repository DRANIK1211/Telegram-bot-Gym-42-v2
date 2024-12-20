from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
import logging
import sql
from config import *
from textMessages import *
from buttons import *
from registration import registration

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(mes: Message):
    global but
    user = sql.search_user(mes.from_user.id)
    # Ищем в таблице users людей с id, в ответе массив [id, username, role, count]
    if user != []:  # Проверяем пустой ли массив
        role = user[0][2]
    else:
        await mes.answer(messageStart_userNull, reply_markup=button_registration)
        return

    match role:  # Проверяем роль пользователя и выводим соответствующие кнопки
        case "User":
            but = button_user
        case "Admin":
            but = button_admin
        case "IT":
            but = button_otdel
        case "Xoz":
            but = button_otdel
        case _:
            await mes.answer("Ошибка роли пользователя. Обратитесь в поддержку")

    await mes.answer(messageStart, reply_markup=but)


async def run_bot():
    dp.include_router(registration)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Удалить после разработки
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        print("EXIT")
