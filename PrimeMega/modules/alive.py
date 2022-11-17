import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from PrimeMega.events import register
from PrimeMega import telethn as tbot
from PrimeMega import dispatcher, OWNER_USERNAME as uname, BOT_USERNAME as bu, IMG_BOT, SUPPORT_CHAT

PHOTO = IMG_BOT

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm {dispatcher.bot.first_name}.** \n\n"
  TEXT += "⚡️ **I'm Working Properly** \n\n"
  TEXT += f"⚡️ **My Master : [master](t.me/{uname})** \n\n"
  TEXT += f"⚡️ **Library Version :** `{telever}` \n\n"
  TEXT += f"⚡️ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"⚡️ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Help", f"https://t.me/{bu}?start=help"), Button.url("Support", f"https://t.me/{SUPPORT_CHAT}")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
