import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from PrimeMega.events import register
from PrimeMega import telethn as tbot


PHOTO = "https://telegra.ph/file/51c8712f990fd5ab751b8.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭.** \n\n"
  TEXT += "⚡ **I'm Working Properly** \n\n"
  TEXT += f"👨‍💻 **My Master : [Yanzz](https://t.me/BotMr07)** \n\n"
  TEXT += f"📃 **Library Version :** `{telever}` \n\n"
  TEXT += f"🔰 **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"💥 **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/zenitsuclonev1bot?start=help"), Button.url("Support", "https://t.me/zennih")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
