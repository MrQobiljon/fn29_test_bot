from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def main_buttons():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📚 maktab darsliklari"),
                KeyboardButton(text="📚 badiiy adabiyotlar")
            ],
            [
                KeyboardButton(text="🌐 IT Course"),
                KeyboardButton(text="📚 IELTS Course")
            ],
            [
                KeyboardButton(text="Send location", request_location=True),
                KeyboardButton(text="Send contact", request_contact=True)
            ]
        ],
        resize_keyboard=True
    )
    return markup


async def school_buttons():
    buttons = []
    for i in range(1, 12):
        buttons.append([KeyboardButton(text=f"📙 {i}-sinf darsliklari")])
    buttons.append([KeyboardButton(text="Go Back")])
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)