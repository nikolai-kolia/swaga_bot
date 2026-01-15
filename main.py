import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from lyrics import get_random_line

TOKEN = "8593140276:AAE98JQIPctsFmwQzTqBSPe5xAVoe7xB4jg"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Йо! Напиши /swaga — и я кину строчку от ICEGERGERT 🎵\n"
        "Или попробуй /vibe 😎"
    )


@dp.message(Command("swaga"))
async def swaga_handler(message: types.Message):
    line = get_random_line()
    await message.answer(f"🔥 {line}")


@dp.message(Command("vibe"))
async def vibe_handler(message: types.Message):
    vibes = [
        "Сегодня твой день. Просто поверь в это.",
        "Ты делаешь больше, чем тебе кажется.",
        "Не останавливайся. Ты уже далеко зашёл.",
        "Всё получится. Даже если не сразу."
    ]
    await message.answer(vibes[hash(message.from_user.id) % len(vibes)])


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
