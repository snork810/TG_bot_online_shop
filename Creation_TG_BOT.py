#!/usr/bin/env python3.11.5
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton #блок работы с клавиатурами и объект самой кнопки
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
import asyncio 
import logging
from config import API
from keyboards import *
import texts
from admin import *
from db import *
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)


#Машина состояний
class UserState(StatesGroup): 
    adress = State()


@dp.callback_query_handler(text='info') #передаем в параметр text id кнопки который указали в callback_data при инициализации кнопки
async def inlin_inform(call):
    await call.message.answer('Информация о боте')
    await call.answer() #Окончание работы кнопки

#клавиатуры кнопок
@dp.message_handler(commands=['start']) #Хэндлер для реагирования на команды
async def start_message(message):
    print("Бот запущен")  
    await message.answer(f"Добро пожаловать, {message.from_user.username}. " + texts.start, reply_markup=start_menu)

# Команды для отправки файлов юзеру в ответ на сообщение
#message.answer_photo 
#message.answer_video
# message.answer_file

@dp.message_handler(text='INFO')
async def inform(message):
    with open('TG_BOT/4.jpg', 'rb')as img:
        await message.answer_photo(img, f"{texts.about}", reply_markup=start_menu)
    

@dp.message_handler(text='Ассортимент')
async def assortiment(message):
    await message.answer("Вот наш ассортимент", reply_markup=assortiment_kb)

@dp.callback_query_handler(text='medium')
async def buy_M(call):
    with open('TG_BOT/1.jpg', 'rb')as img:
        await call.message.answer_photo(img, texts.Mgame, reply_markup = buy_kb)
    await call.answer()
@dp.callback_query_handler(text='big')
async def buy_L(call):
    with open('TG_BOT/2.jpg', 'rb')as img:
        await call.message.answer_photo(img, texts.Lgame, reply_markup = buy_kb)
    await call.answer()
@dp.callback_query_handler(text='mega')
async def buy_XL(call):
    with open('TG_BOT/3.jpg', 'rb')as img:
        await call.message.answer_photo(img, texts.XLgame, reply_markup = buy_kb)
    await call.answer()
@dp.callback_query_handler(text='other')
async def back_to_assortiment(call):
    await call.message.answer(f'{texts.other}', reply_markup=start_menu)
    await call.answer()





@dp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer("Вы можете посмотреть свою корзину или оформить заказ", reply_markup=assortiment_kb)
    await call.answer()
@dp.message_handler(text = 'Заказать')
async def buy(message):
    await message.answer('Отправь нам свой адрес, пожалуйста')
    await UserState.adress.set()
@dp.message_handler(state=UserState.adress)
async def fsm_handler(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()  #Сохранине адреса клиента в словаре для дальнейшего оперирования\логирования\обработки
    await message.answer(f'Доставка будет отправлена на адрес {data["first"]}')
    await state.finish()





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)