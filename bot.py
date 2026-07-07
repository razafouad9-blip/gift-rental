import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

# توكن البوت
TOKEN = "8982670998:AAGlTVaYNsCNDvt79dUX7grIy6riNqY9hvo"

# إنشاء البوت
bot = Bot(token=TOKEN)
dp = Dispatcher()

# أمر /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🎉 أهلاً بك في Gift Rental\n\n"
        "✅ البوت يعمل بنجاح."
    )

# تشغيل البوت
async def main():
    print("🚀 Bot Started...")
    await dp.start_polling(bot)

# بدء التشغيل
if __name__ == "__main__":
    asyncio.run(main())