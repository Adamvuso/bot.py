from aiogram import Bot, Dispatcher, executor, types
from  aiogram . types  import  ReplyKeyboardRemove , ReplyKeyboardMarkup , KeyboardButton , InlineKeyboardMarkup , InlineKeyboardButton

API_TOKEN = '1324835503:AAEWZ6NY_MskhIVq4VQfnKEKwkOuO0MZT8Y'


#Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)
@dp.message_handler(commands=['test'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!",reply_markup=kb.greet_kb) 

@dp.message_handler(commands=['start'])
async def start(msg: types.message):
  await msg.answer("🌬️Я пока ничего не умею!?🌬️")



@dp.message_handler(commands=['help'])
async def echo(msg: types.message):
  await msg.answer("Привет! Я бот Бабэтта. Пока я только умею повторять за вами, но вскоре появятся новые функции!")

if __name__=='__main__':
  executor.start_polling(dp, skip_updates=True)


      



