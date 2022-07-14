from aiogram import types
import text,config
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

buttons = types.InlineKeyboardMarkup()
btn_sub_1 = types.InlineKeyboardButton(text=text.btn_sub_1_text, url=config.SUBSCRIBE_LINK)
btn_sub_2 = types.InlineKeyboardButton(text=text.btn_sub_2_text, url=config.SUBSCRIBE_LINK)
buttons.add(btn_sub_1,btn_sub_2)

button_5 = KeyboardButton('5')
button_7 = KeyboardButton('7')
button_14 = KeyboardButton('14')
button_21 = KeyboardButton('21')
button_28 = KeyboardButton('28')

intervals = ReplyKeyboardMarkup()
intervals.add(button_5,button_7,button_14,button_21,button_28)

weather_buttons = types.InlineKeyboardMarkup()
btn_place = types.InlineKeyboardButton(text=text.btn_place_text, callback_data='place')
btn_gps = types.InlineKeyboardButton(text=text.btn_gps_text, callback_data='gps')
btn_zip = types.InlineKeyboardButton(text=text.btn_zip_text, callback_data='zip')
weather_buttons.add(btn_place,btn_gps,btn_zip)

donate_buttons = types.InlineKeyboardMarkup()
btn_donate = types.InlineKeyboardButton(text=text.btn_donate_text, url=config.DONATE_LINK)
donate_buttons.add(btn_donate)

geo_buttons = types.InlineKeyboardMarkup()
btn_geo = types.InlineKeyboardButton(text=text.btn_donate_text,request_location=True)
geo_buttons.add(btn_geo)

subscribe_button = types.InlineKeyboardMarkup()
btn_subscribe = types.InlineKeyboardButton(text=text.subscribe_btn_text, callback_data='subscribe_weather')
subscribe_button.add(btn_subscribe)

subscribed_buttons = types.InlineKeyboardMarkup()
btn_unsubscribe = types.InlineKeyboardButton(text=text.unsubscribe_btn_text, callback_data='unsubscribe_weather')
btn_edit = types.InlineKeyboardButton(text=text.edit_btn_text, callback_data='edit_weather')
subscribed_buttons.add(btn_unsubscribe,btn_edit)