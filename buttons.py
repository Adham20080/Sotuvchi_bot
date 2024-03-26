from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

con = [
    [types.KeyboardButton(text="☎️ Kontaktlar", request_contact=True),
     types.KeyboardButton(text="🏠 Bosh Menu")]
]
contact = types.ReplyKeyboardMarkup(keyboard=con, resize_keyboard=True)

key1 = [
    [types.KeyboardButton(text="🔥 Mahsulotlar"),
     types.KeyboardButton(text="ℹ️ Ma'lumot")],
    [types.KeyboardButton(text="💼 Hamkorlik")]
]
menu = types.ReplyKeyboardMarkup(keyboard=key1, resize_keyboard=True)

men = [
    [types.KeyboardButton(text="✍️ Izoh qoldirish"),
     types.KeyboardButton(text="🚀 Yetkazib berish shartlari")],
    [types.KeyboardButton(text="☎️ Kontaktlar"),
     types.KeyboardButton(text="🏠 Bosh Menu")]
]
malumotlar = types.ReplyKeyboardMarkup(keyboard=men, resize_keyboard=True)

inline_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="To'lov qilish", callback_data="Tolov")],
    [InlineKeyboardButton(text="Batafsil", callback_data="Ba1")]
])

inline_btn1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="To'lov qilish", callback_data="Tolov1")],
    [InlineKeyboardButton(text="Batafsil", callback_data="Ba2")]
])

inline_btn2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="To'lov qilish", callback_data="Tolov2")],
    [InlineKeyboardButton(text="Batafsil", callback_data="Ba3")]
])

inline_btn3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="To'lov qilish", callback_data="Tolov3")],
    [InlineKeyboardButton(text="Batafsil", callback_data="Ba4")]
])
inline_btn4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="To'lov qilish", callback_data="Tolov4")],
    [InlineKeyboardButton(text="Batafsil", callback_data="Ba5")]
])

key = [
    [types.KeyboardButton(text="Phone 📱"),
     types.KeyboardButton(text="Laptop 💻")],
    [types.KeyboardButton(text="Watch ⌚"),
     types.KeyboardButton(text="Keyboard ⌨")],
    [types.KeyboardButton(text="🏠 Bosh Menu")]
]
keyboard = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)

iphone = [
    [types.KeyboardButton(text="iPhone 15 PRO"),
     types.KeyboardButton(text="iPhone 14 Plus")],
    [types.KeyboardButton(text="🏠 Bosh Menu")]
]
IPhone = types.ReplyKeyboardMarkup(keyboard=iphone, resize_keyboard=True)

whaa = [
    [types.KeyboardButton(text="X8 Ultra")],
    [types.KeyboardButton(text="🏠 Bosh Menu")]
]
watch = types.ReplyKeyboardMarkup(keyboard=whaa, resize_keyboard=True)

keyb = [
    [types.KeyboardButton(text="Klaviaturasi T60")],
    [types.KeyboardButton(text="🏠 Bosh Menu")]
]
keyboardd = types.ReplyKeyboardMarkup(keyboard=keyb, resize_keyboard=True)

mac = [
    [types.KeyboardButton(text="MacBook Air 13"), ],
    [types.KeyboardButton(text="🏠 Bosh Menu")]
]
macBook = types.ReplyKeyboardMarkup(keyboard=mac, resize_keyboard=True)
