from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1324835503:AAEWZ6NY_MskhIVq4VQfnKEKwkOuO0MZT8Y'


#Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(msg: types.message):
  await msg.answer("🌬️Я пока ничего не умею!?🌬️")

@dp.message_handler(commands= ['test'])
@dp.async_task
async def test(msg: types.message):
    a = 'удалить'
    b = 'выключено'
    i_b_1 = types.InlineKeyboardButton(a, callback_data='b1')
    i_b_2 = types.InlineKeyboardButton(b, callback_data= 'b2')
    i_k_1 = types.InlineKeyboardMarkup().add(i_b_1, i_b_2)
    print(msg.from_user.id)
    await msg.answer('Что хочешь узнать?', reply_markup = i_k_1)
    await asyncio.sleep(10)
    c_i = msg.chat.id
    m_i = msg.message_id +1
    await bot.message("Testiruem epti")



@dp.message_handler(commands=['help'])
async def echo(msg: types.message):
  await msg.answer("Привет! Я бот Бабэтта. Пока я только умею повторять за вами, но вскоре появятся новые функции!")

if __name__=='__main__':
  executor.start_polling(dp, skip_updates=True)


      



