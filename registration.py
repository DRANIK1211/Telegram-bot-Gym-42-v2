# Регистрация людей в базе данных

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import sql
import config as cd
from textMessages import *
from buttons import *
from states import *

registration = Router()


@registration.callback_query(F.data == "but_registration")
async def reg(cb: CallbackQuery, state: FSMContext):
    global but
    await cb.answer()
    user = sql.search_user(cb.from_user.id)  # Проверяем есть ли пользователь в бд
    if user != []:
        role = user[0][2]
        match role:  # Проверяем роль пользователя и выводим соответствующие кнопки
            case "User":
                but = button_user
            case "Admin":
                but = button_admin
            case "IT":
                but = button_otdel
            case "Xoz":
                but = button_otdel
        await cb.message.answer("Вы уже зарегистрированы", reply_markup=but)
        await cb.message.delete()
        return

    await cb.message.edit_text("Регистрация!", reply_markup=None)  # Отправляем пользователя на регистрацию
    await cb.message.answer("Введите ваше ФИО\n"
                    "Например: Иванов Иван Иванович")
    await state.set_state(Registration.name)


@registration.message(Registration.name)
async def reg_name(mes: Message, state: FSMContext):
    await state.update_data(name=mes.text.lower())
    await mes.answer("Введите кодовое слово")
    await state.set_state(Registration.role)


@registration.message(Registration.role)
async def reg_role(mes: Message, state: FSMContext):
    await state.update_data(role=mes.text)
    data = await state.get_data()
    global role, but
    match data["role"]:
        case cd.CODE_1:
            role = "User"
        case cd.CODE_2:
            role = "Admin"
        case cd.CODE_3:
            role = "IT"
        case cd.CODE_4:
            role = "Xoz"
        case _:  # Если есть ошибка в кодовом слове пользователя отправляет на регистрацию
            await mes.message.answer("Ошибка. Попробуйте зарегистрироваться ещё раз. \n-> /start <-")
            await state.clear()
            return

    mas = (mes.from_user.id, data["name"], role, 0)  # Массив с данными пользователя
    res = sql.add_user(mas)
    if res:  # Если регистрация прошла успешно
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
                but = None
        await mes.answer(reg_true, reply_markup=but)
    else:
        await mes.answer("Возникла ошибка, обратитесь в поддержку")
        await mes.answer(res)
    await state.clear()

