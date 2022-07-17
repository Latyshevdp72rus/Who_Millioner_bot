from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

play_game = KeyboardButton('<НОВАЯ  ИГРА>')
cancel_game = KeyboardButton('<ВЫХОД>')
new_game = ReplyKeyboardMarkup(resize_keyboard=True).row(play_game, cancel_game)

