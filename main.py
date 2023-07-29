from aiogram import Bot, Dispatcher, executor, types
from conf import TOKEN_API,WEATHER_API
from weather import get_weather
from trans import text_trans, original_language
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""🇬🇧Welcome to the weather forecaster bot!
click /weather to find out the weather in your city!

🇷🇺Добро пожаловать в бота синоптика
нажмите /weather, чтобы узнать погоду в вашем городе""",)


@dp.message_handler(commands=['weather'])
async def weather_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Enter your city/Введите город")


@dp.message_handler()
async def weather_ifo(message: types.Message):
    lang = original_language(message.text)
    if get_weather(message.text,WEATHER_API,lang) == 0:
        await message.answer(text="""🇬🇧Check the name of the city
        
🇷🇺Проверьте название вашего города""")
    else:
        ans = get_weather(message.text, WEATHER_API, lang)
        await message.answer(text=f"""{text_trans(f"🏙City:", lang)} {ans['city_name']}""")

        await message.answer(text=text_trans(f"""🌡Temperature: {'+' if ans['temp'] > 0 else ''}{round(ans['temp'])}°C
        
Feels like:{'+' if ans['feels_like'] > 0 else ''}{ans['feels_like']}°C
        
🔽Minimum temperature: {'+' if ans['temp_min'] > 0 else ''}{ans['temp_min']}°C
        
🔼Maximum temperature: {'+' if ans['temp_max'] > 0 else ''}{ans['temp_max']}°C
        """, lang))
        await message.answer(text=text_trans(f"☀Weather:", lang) + f" {ans['weather_status']}")
        await message.answer(text=text_trans(f"💧Humidity:{round(ans['humidity'])}%", lang))
        await message.answer(text=text_trans(f"🌬Wind speed: {ans['wind_speed']} m/s", lang))



if __name__ == '__main__':
    executor.start_polling(dp)
