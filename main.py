import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from buttons import main_buttons, school_buttons

bot = Bot(token="8753784106:AAFtcRo75PgKSpkutUAkfSxyJxmyS4TKzh0")
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    full_name = message.from_user.full_name
    await message.answer(f"Xush kelibsiz {full_name} zoti oliylari!",
                         reply_markup=await main_buttons())


@dp.message(F.text == "📚 maktab darsliklari")
async def reaction_to_school_lessons(message: Message):
    await message.answer("Sinf tanlang!", reply_markup=await school_buttons())


@dp.message(F.text == "Go Back")
async def reaction_to_go_back(message: Message):
    await message.answer("Asosiy sahifa", reply_markup=await main_buttons())


@dp.message(F.text.startswith("📙 ") and F.text.endswith("-sinf darsliklari"))
async def reaction_to_lessons(message: Message):
    if message.text == "📙 1-sinf darsliklari":
        # photo = FSInputFile("files/img.png")
        # await message.answer_photo(photo)
        #
        # file = FSInputFile("files/ona_tili.pdf")
        # await message.answer_document(file)

        await message.answer_photo(
            "https://suret.pics/uploads/posts/2023-09/1695384937_2-7.jpg",
            caption="Bu dinozavrlar rasmi",
            has_spoiler=True
        )

    elif message.text == "📙 2-sinf darsliklari":
        pass
    elif message.text == "📙 3-sinf darsliklari":
        pass
    elif message.text == "📙 4-sinf darsliklari":
        pass
    elif message.text == "📙 5-sinf darsliklari":
        pass
    elif message.text == "📙 6-sinf darsliklari":
        pass
    elif message.text == "📙 7-sinf darsliklari":
        pass
    elif message.text == "📙 8-sinf darsliklari":
        pass
    elif message.text == "📙 9-sinf darsliklari":
        pass
    elif message.text == "📙 10-sinf darsliklari":
        pass
    elif message.text == "📙 11-sinf darsliklari":
        pass


@dp.message(F.contact)
async def reaction_to_contact(message: Message):
    if message.contact:
        phone_number = message.contact.phone_number
        await message.answer(f"Sizning phone numberingiz: {phone_number}")


@dp.message(F.location)
async def reaction_to_location(message: Message):
    if message.location:
        lat = message.location.latitude
        long = message.location.longitude
        await message.answer_location(lat, long)


async def main():
    await dp.start_polling(bot)



asyncio.run(main())