import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from buttons import *
from pay import order1, order2, order3, order4, order5, pre_checkout_query, successful_payment, ba1, ba2, ba3, ba4, ba5
from config import Token

bot = Bot(token=Token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        f"""<b>Assalomu Alaykum</b>, {message.from_user.full_name} !

Ijodimizga qiziqish bildirganingiz uchun tashakkur!

O'zbekiston bo'ylab yetkazib berish 2-5 ish kunini tashkil qiladi.

Toshkent bo'ylab yetkazib berish - 20 000 so'm.
O‘zbekiston bo'ylab yetkazib berish - 30 000 so‘m.

450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!

Agar bu shartlar sizni qoniqtirsa, 🔥 Mahsulotlar bo'limiga o'tish orqali buyurtma berishni boshlashingiz mumkin.""",
        parse_mode="HTML", reply_markup=menu)


@dp.message(F.text == "🔥 Mahsulotlar")
async def cmd_start(message: types.Message):
    await message.answer(f"Xurmatli {message.from_user.full_name}!\nMahsulotni tanlang",
                         reply_markup=keyboard)


@dp.message(F.text == "Phone 📱")
async def cmd_start(message: types.Message):
    await message.answer(f"Xurmatli {message.from_user.full_name}!\nMahsulotni tanlang",
                         reply_markup=IPhone)

    @dp.message(F.text == "iPhone 15 PRO")
    async def cmd_start(message: types.Message):
        await message.answer_photo("https://images.uzum.uz/cn7hgprifoubkc6s4cs0/original.jpg",
                                   caption=f"Xurmatli {message.from_user.full_name}!",
                                   reply_markup=inline_btn)

    @dp.message(F.text == "iPhone 14 Plus")
    async def cmd_start(message: types.Message):
        await message.answer_photo("https://images.uzum.uz/cnk67og4idugcqegf1l0/original.jpg",
                                   caption=f"Xurmatli {message.from_user.full_name}!",
                                   reply_markup=inline_btn1)


@dp.message(F.text == "Laptop 💻")
async def cmd_start(message: types.Message):
    await message.answer(f"Xurmatli {message.from_user.full_name}!",
                         reply_markup=macBook)

    @dp.message(F.text == "MacBook Air 13")
    async def cmd_start(message: types.Message):
        await message.answer_photo("https://images.uzum.uz/cnat9s1s99ouqbfvegsg/original.jpg",
                                   caption=f"Xurmatli {message.from_user.full_name}!",
                                   reply_markup=inline_btn2)


@dp.message(F.text == "Watch ⌚")
async def cmd_start(message: types.Message):
    await message.answer(f"Xurmatli {message.from_user.full_name}!",
                         reply_markup=watch)

    @dp.message(F.text == "X8 Ultra")
    async def cmd_start(message: types.Message):
        await message.answer_photo("https://images.uzum.uz/cjivj2jk9fq53ftf0ei0/original.jpg",
                                   caption=f"Xurmatli {message.from_user.full_name}!",
                                   reply_markup=inline_btn3)


@dp.message(F.text == "Keyboard ⌨")
async def cmd_start(message: types.Message):
    await message.answer(f"Xurmatli {message.from_user.full_name}!",
                         reply_markup=keyboardd)

    @dp.message(F.text == "Klaviaturasi T60")
    async def cmd_start(message: types.Message):
        await message.answer_photo("https://images.uzum.uz/cmsuqg925ku8jql6d510/original.jpg",
                                   caption=f"Xurmatli {message.from_user.full_name}!",
                                   reply_markup=inline_btn4)


@dp.message(F.text == "ℹ️ Ma'lumot")
async def start(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=malumotlar)


@dp.message(F.text == "🚀 Yetkazib berish shartlari")
async def yet(message: types.Message):
    await message.answer("""Yetkazib berish shartlari:
O'zbekiston bo'ylab yetkazib berish 2-5 ish kuni ichida amalga oshiriladi. 
Toshkent bo'ylab yetkazib berish - 20 USD.
O‘zbekiston bo'ylab yetkazib berish - 30 USD.

1 000 USD dan ortiq buyurtmalarni yetkazib berish - tekin!""")


@dp.message(F.text == "☎️ Kontaktlar")
async def malumot(message: types.Message):
    await message.answer("Contact jo'nating ⬇️", reply_markup=contact)


@dp.message(F.text == "💼 Hamkorlik")
async def ham(message: types.Message):
    await message.answer("""Biz sizning kompaniyangiz bilan hamkorlik qilishdan mamnunmiz va sizning buyurtmangizga asosan futbolkalar, xudi, svitshot va boshqa ko'p narsalarni tayyorlashimiz mumkin.

Menejer bilan bog'lanish uchun: @all_linux""")


@dp.message(F.text == "🏠 Bosh Menu")
async def bosh(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=menu)


dp.callback_query.register(order1, F.data == "Tolov")
dp.callback_query.register(order2, F.data == "Tolov1")
dp.callback_query.register(order3, F.data == "Tolov2")
dp.callback_query.register(order4, F.data == "Tolov3")
dp.callback_query.register(order5, F.data == "Tolov4")
dp.callback_query.register(ba1, F.data == "Ba1")
dp.callback_query.register(ba2, F.data == "Ba2")
dp.callback_query.register(ba3, F.data == "Ba3")
dp.callback_query.register(ba4, F.data == "Ba4")
dp.callback_query.register(ba5, F.data == "Ba5")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
