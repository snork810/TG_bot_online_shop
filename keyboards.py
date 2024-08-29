from aiogram.types import ReplyKeyboardMarkup, KeyboardButton #блок работы с клавиатурами и объект самой кнопки
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton #блок работы с инлайн клавиатурами и объект самой кнопки
start_menu = ReplyKeyboardMarkup(
      keyboard = [
      [KeyboardButton(text='INFO')], 
      [KeyboardButton(text='Ассортимент'), KeyboardButton(text='Корзина')],
      [KeyboardButton(text='Заказать')]
      ],resize_keyboard=True
                                )

assortiment_kb = InlineKeyboardMarkup(
      inline_keyboard=[[InlineKeyboardButton(text='Средняя Игра', callback_data='medium')],
                       [InlineKeyboardButton(text='Большая Игра', callback_data = 'big')],
                       [InlineKeyboardButton(text='Очень Большая Игра',callback_data = 'mega')],
                       [InlineKeyboardButton(text='Другие предложения', callback_data = 'others',)]
                        ])

buy_kb = InlineKeyboardMarkup(
      inline_keyboard=[[InlineKeyboardButton(text='Купить', url='https://ya.ru')],
                       [InlineKeyboardButton(text='Назад', callback_data='back_to_catalog')]],
)


admin_panel = InlineKeyboardMarkup(
      inline_keyboard=[
            [InlineKeyboardButton(text='Пользователи', callback_data='users')],
            [InlineKeyboardButton(text='Статистика', callback_data='stat')],
            [InlineKeyboardButton(text='Блокировка', callback_data='block'),
             InlineKeyboardButton(text='Разблокировка', callback_data='unblock')
            ],
      ]
)