from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from geezram import pbot
from geezram.utils.errors import capture_err
from geezram.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


IRAA = "https://telegra.ph/file/c78bb1efdeed38ee16eb2.png"
Deploy = "https://telegra.ph/file/fbee80404f99a7a913d59.jpg"
String = "https://telegra.ph/file/1741ee14bb0ea0d0dc376.jpg"
Repo = "https://telegra.ph/file/e9a82819b8b101ec3c798.jpg"
Apikey = "https://telegra.ph/file/dab3063e78b367ca9e7af.jpg"
Tutorial = "https://telegra.ph/file/900382d68a127bc93af4b.jpg"

@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=IRAA,
        caption=f"""**Hai, saya Geez|Ram** 

**Owner repo : [izzy](https://t.me/jasadeak)**
**Python Version :** `{y()}`
**Library Version :** `{o}`
**Telethon Version :** `{s}`
**Pyrogram Version :** `{z}`

**Create your own with click button bellow.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repo", url="https://github.com/SangeanSquad/Queen-Iraa")
                ],
                [ 
                    InlineKeyboardButton(
                        "Geez Project", url="https://github.com/vckyou/GeezProjects"),
                    InlineKeyboardButton(
                        "RAM-UBOT", url="https://github.com/GeezRam/RAM-UBOT")
                ],
                [ 
                    InlineKeyboardButton(
                        "Geez Pyro", url="https://github.com/hitokizzy/Geez-Pyro"),
                    InlineKeyboardButton(
                        "RAM Pyro", url="https://github.com/izzy-adeeva/RamPyro-Bot")
                ],
                [ 
                    InlineKeyboardButton(
                        "Arya x Userbot", url="https://github.com/Onlymeriz/arya"),
                    InlineKeyboardButton(
                        "File Sharing 3 Button", url="https://github.com/Onlymeris/fs")
                ]
            ]
        )
    )

@pbot.on_message(filters.command("deploy"))
async def deploy(_, message):
    await message.reply_photo(
        photo=Deploy,
        caption=f"""**Deploy...**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "Geez Project", url="https://heroku.com/deploy?template=https://github.com/GeezRam/Geez-Projects"),
                    InlineKeyboardButton(
                        "RAM-Pyro", url="https://heroku.com/deploy?template=https://github.com/izzy-adeeva/RamPyro-Bot")
                ],  
                [ 
                    InlineKeyboardButton(
                        "Geez-Pyro Beta", url="https://github.com/hitokizzy/Geez-Pyro"),
                    InlineKeyboardButton(
                        "Arya-Userbot", url="https://github.com/Onlymeriz/Ayra")
                ]
            ]

        )
    )

@pbot.on_message(filters.command("tutorial"))
async def tutorial(_, message):
    await message.reply_photo(
        photo=Tutorial,
        caption=f"""**Tutorial & Dyno Heroku...**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "Tutorial", url="https://youtu.be/9rpm37jWx70"),
                    InlineKeyboardButton(
                        "On Dyno", url="https://t.me/GeezSupport/250434")
                ],  
                [ 
                    InlineKeyboardButton(
                        "Restart Dyno", url="https://t.me/Geezprojectt/75"),
                    InlineKeyboardButton(
                        "Buat Heroku", url="https://youtu.be/7Ujhl8qdeKY")
                ]
            ]

        )
    )

@pbot.on_message(filters.command("string"))
async def tutorial(_, message):
    await message.reply_photo(
        photo=String,
        caption=f"""**String...**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "String Geez|RAM", url="https://t.me/geezramstringbot"),
                    InlineKeyboardButton(
                        "String Replit", url="https://replit.com/@izzy-adeeva/UserButt")
                ],   
                    
            ]

        )
    )

@pbot.on_message(filters.command("api"))
async def tutorial(_, message):
    await message.reply_photo(
        photo=Apikey,
        caption=f"""**Api key & Hash...**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "Lebah Api", url="https://t.me/lebahsupportbot"),
                    InlineKeyboardButton(
                        "Telegram OF", url="https://my.telegram.org")
                ]
            ]

        )
    )
