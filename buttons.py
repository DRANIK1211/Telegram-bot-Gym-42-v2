#  Заготовки кнопок CallbackQuery

from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup


button_registration = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(
            text="Зарегистрироваться",
            callback_data="but_registration"
        )
    ]]
)  # Кнопка регистрации


button_user = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Создать заявку", callback_data="but_user_sendApplication")],
        [InlineKeyboardButton(text="Посмотреть отправленные заявки", callback_data="but_user_getApplications")]
    ]
)  # Кнопки User: отправка заявки, получение отправленных заявок


button_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Удалить пользователя", callback_data="but_admin_deleteUser")],
        [InlineKeyboardButton(text="Создать отчёт по заявкам", callback_data="but_admin_getReport")]
    ]
)  # Кнопки Admin: удаление пользователя, создание отчёта


button_otdel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть заявки", callback_data="but_otdel_getApplications")]
    ]
)  # Кнопки IT и Xoz: посмотреть пришедшие заявки

