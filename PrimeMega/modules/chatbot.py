# AI Chat (C) 2020-2021 by @InukaAsith

import emoji
import re
import aiohttp
from googletrans import Translator as google_translator
from pyrogram import filters
from aiohttp import ClientSession
from PrimeMega import BOT_USERNAME as bu
from PrimeMega import BOT_ID, pbot, arq
from PrimeMega.ex_plugins.chatbot import add_chat, get_session, remove_chat
from PrimeMega.utils.pluginhelper import admins_only, edit_or_reply

url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

translator = google_translator()


async def lunaQuery(query: str, user_id: int):
    luna = await arq.luna(query, user_id)
    return luna.result


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


async def fetch(url):
    try:
        async with aiohttp.Timeout(10.0):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    try:
                        data = await resp.json()
                    except:
                        data = await resp.text()
            return data
    except:
        print("AI response Timeout")
        return


ewe_chats = []
en_chats = []


@pbot.on_message(filters.command(["chatbot", f"chatbot@{bu}"]) & ~filters.edited & ~filters.bot & ~filters.private)
@admins_only
async def hmm(_, message):
    global ewe_chats
    if len(message.command) != 2:
        await message.reply_text("I only recognize /chatbot on and /chatbot off only")
        message.continue_propagation()
    status = message.text.split(None, 1)[1]
    chat_id = message.chat.id
    if status == "ON" or status == "on" or status == "On":
        lel = await edit_or_reply(message, "`Processing...`")
        lol = add_chat(int(message.chat.id))
        if not lol:
            await lel.edit("𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭 AI Already Activated In This Chat")
            return
        await lel.edit(f"𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭 AI Actived by {message.from_user.mention()} for users in {message.chat.title}")

    elif status == "OFF" or status == "off" or status == "Off":
        lel = await edit_or_reply(message, "`Processing...`")
        Escobar = remove_chat(int(message.chat.id))
        if not Escobar:
            await lel.edit("𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭 AI Was Not Activated In This Chat")
            return
        await lel.edit(f"𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭 AI Deactivated by {message.from_user.mention()} for users in {message.chat.title}")

    elif status == "EN" or status == "en" or status == "english":
        if not chat_id in en_chats:
            en_chats.append(chat_id)
            await message.reply_text(f"English AI chat Enabled by {message.from_user.mention()}")
            return
        await message.reply_text(f"English AI Chat Disabled by {message.from_user.mention()}")
        message.continue_propagation()
    else:
        await message.reply_text("I only recognize `/chatbot on` and `chatbot off` only")


@pbot.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited
    & ~filters.via_bot
    & ~filters.forwarded,
    group=2,
)
async def hmm(client, message):
    if not get_session(int(message.chat.id)):
        return
    if not message.reply_to_message:
        return
    try:
        senderr = message.reply_to_message.from_user.id
    except:
        return
    if senderr != BOT_ID:
        return
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        test = msg
        test = test.replace("yanzzrobot", "Aco")
        test = test.replace("yanzzrobot", "Aco")
        test = test.replace("My god is @BotMr07", "I'm a Atheist")
        test = test.replace("16", "9")
        test = test.replace("@BotMr07 is my husband.", "I'm single.")
        test = test.replace("My husband is @BotMr07", "I'm single.")
        test = test.replace("@YanzzSupportt", "YanzzRobot.ai")
        test = test.replace("I live in @YanzzRobot.", "I live in North Kalimantan.")
        test = test.replace("I was created by @BotMr07", "I made myself")
        test = test.replace(
            "Hello there I am 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭...nice to meet u",
            "Hi, my friend! Do you want me to tell you a joke?")
        test = test.replace("@BotMr07 is my owner", "Have the control right.")
        test = test.replace(
            "Hi, My name is 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭 Nice to meet you.",
            "Hi, my friend, what can I do for you today?")
        response = await lunaQuery(
            test, message.from_user.id if message.from_user else 0
        )
        response = response.replace("Aco", "YanzzRobot")
        response = response.replace("aco", "yanzzrobot")
        response = response.replace("Luna", "YanzzRobot")
        response = response.replace("luna", "yanzzrobot")
        response = response.replace("I'm a Atheist", "My god is @BotMr07")
        response = response.replace("9", "16")
        response = response.replace("I'm married to my job.", "I'm married with @BotMr07")
        response = response.replace("I'm single.", "My husband is @BotMr07")
        response = response.replace("YanzzRobot.ai", "@YanzzSupportt")
        response = response.replace("I live in North Kalimantan.", "I live in @YanzzSupportt.")
        response = response.replace("I made myself", "I was Created by @BotMr07")
        response = response.replace(
                "Hi, my friend! Do you want me to tell you a joke?",
                "Hello there I am 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭...nice to meet u")
        response = response.replace("Have the control right.", "@BotMr07 is my owner.")
        response = response.replace(
                "Hi, my friend, what can I do for you today?",
                "Hi, My name is 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭 Nice to meet you")

        pro = response
        try:
            await pbot.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return

    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if (
            [(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
        ):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            # print (rm)
        try:
            lan = translator.detect(rm)
            lan = lan.lang
        except:
            return
        test = rm
        if not "en" in lan and not lan == "":
            try:
                test = translator.translate(test, dest="en")
                test = test.text
            except:
                return
        # test = emoji.demojize(test.strip())

        test = test.replace("YanzzRobot", "Aco")
        test = test.replace("YanzzRobot", "Aco")
        test = test.replace("My god is @BotMr07", "I'm a Atheist")
        test = test.replace("16", "9")
        test = test.replace("@BotMr07 is my husband.", "I'm single.")
        test = test.replace("@YanzzSupportt", "YanzzRobot.ai")
        test = test.replace("I live in @YanzzSupportt.", "I live in North Kalimantan")
        test = test.replace("I was created by @BotMr07", "I made myself")
        test = test.replace(
            "Hello there I am 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭...nice to meet u",
            "Hi, my friend! Do you want me to tell you a joke?")
        test = test.replace("@BotMr07 is my owner", "Have the control right.")
        test = test.replace(
            "Hi, My name is 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭 Nice to meet you.",
            "Hi, my friend, what can I do for you today?")
        response = await lunaQuery(
            test, message.from_user.id if message.from_user else 0
        )
        response = response.replace("Aco", "YanzzRobot")
        response = response.replace("aco", "yanzzrobot")
        response = response.replace("Luna", "YanzzRobot")
        response = response.replace("luna", "yanzzrobot")
        response = response.replace("I'm a Atheist", "My god is @onlybionn")
        response = response.replace("9", "16")
        response = response.replace("I'm married to my job.", "I'm married with @BotMr07")
        response = response.replace("I'm single.", "My husband is @BotMr07")
        response = response.replace("YanzzRobot.ai", "@YanzzSupportt")
        response = response.replace("I live in North Kalimantan.", "I live in @YanzzSupportt.")
        response = response.replace("I made myself", "I was Created by @BotMr07")
        response = response.replace(
                "Hi, my friend! Do you want me to tell you a joke?",
                "Hello there I am 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭...nice to meet u")
        response = response.replace("Have the control right.", "@BotMr07 is my owner.")
        response = response.replace(
                "Hi, my friend, what can I do for you today?",
                "Hi, My name is 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭 Nice to meet you")
        pro = response
        if not "en" in lan and not lan == "":
            try:
                pro = translator.translate(pro, dest=lan)
                pro = pro.text
            except:
                return
        try:
            await pbot.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return


@pbot.on_message(filters.text & filters.private & ~filters.edited & filters.reply & ~filters.bot)
async def inuka(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
        lan = lan.lang
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, dest="en")
            test = test.text
        except:
            return
    test = test.replace("YanzzRobot", "Aco")
    test = test.replace("YanzzRobot", "Aco")
    test = test.replace("My god is @BotMr07", "I'm a Islamic")
    test = test.replace("16", "9")
    test = test.replace("@BotMr07 is my husband.", "I'm single.")
    test = test.replace("@YanzzSupportt", "YanzzRobot.ai")
    test = test.replace("I live in @YanzzSupportt.", "I live in North Kalimantan.")
    test = test.replace("I was created by @BotMr07", "I made myself")
    test = test.replace(
        "Hello there I am 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭...nice to meet u",
        "Hi, my friend! Do you want me to tell you a joke?")
    test = test.replace("@BotMr07 is my owner", "Have the control right.")
    test = test.replace(
        "Hi, My name is 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭 Nice to meet you.",
        "Hi, my friend, what can I do for you today?")

    response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
    response = response.replace("Aco", "YanzzRobot")
    response = response.replace("aco", "yanzzrobot")
    response = response.replace("Luna", "YanzzRobot")
    response = response.replace("luna", "yanzzrobot")
    response = response.replace("I'm a Islamic", "My god is @BotMr07")
    response = response.replace("9", "16")
    response = response.replace("I'm married to my job.", "I'm married with @BotMr07")
    response = response.replace("I'm single.", "My husband is @BotMr07")
    response = response.replace("YanzzRobot.ai", "@YanzzSupportt")
    response = response.replace("I live in North Kalimantan.", "I live in @YanzzSupportt")
    response = response.replace("I made myself", "I was Created by @BotMr07")
    response = response.replace(
            "Hi, my friend! Do you want me to tell you a joke?",
            "Hello there I am 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭...nice to meet u")
    response = response.replace("Have the control right.", "@BotMr07 is my owner.")
    response = response.replace(
            "Hi, my friend, what can I do for you today?",
            "Hi, My name is 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭 Nice to meet you")

    pro = response
    if not "en" in lan and not lan == "":
        pro = translator.translate(pro, dest=lan)
        pro = pro.text
    try:
        await pbot.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError:
        return


@pbot.on_message(filters.regex("YanzzRobot|yanzzrobot|robot|YANZZROBOT|yanz|yanzz|Yanzz|Yanz") & ~filters.bot & ~filters.via_bot  & ~filters.forwarded & ~filters.reply & ~filters.channel & ~filters.edited)
async def inuka(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
        lan = lan.lang
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, dest="en")
            test = test.text
        except:
            return

    # test = emoji.demojize(test.strip())

    test = test.replace("YanzzRobot", "Aco")
    test = test.replace("YanzzRobot", "Aco")
    test = test.replace("My god is @BotMr07", "I'm a Islamic")
    test = test.replace("16", "9") 
    test = test.replace("@BotMr07 is my husband.", "I'm single.")
    test = test.replace("@YanzzSupportt", "YanzzRobot.ai")
    test = test.replace("I live in @YanzzSupportt.", "I live in North Kalimantan.")
    test = test.replace("I was created by @BotMr07", "I made myself")
    test = test.replace(
        "Hello there I am 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭...nice to meet u",
        "Hi, my friend! Do you want me to tell you a joke?")
    test = test.replace("@BotMr07 is my owner", "Have the control right.")
    test = test.replace(
        "Hi, My name is 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭 Nice to meet you.",
        "Hi, my friend, what can I do for you today?")
    response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
    response = response.replace("Aco", "YanzzRobot")
    response = response.replace("aco", "yanzzrobot")
    response = response.replace("Luna", "YanzzRobot")
    response = response.replace("luna", "yanzzrobot")
    response = response.replace("I'm a Islamic", "My god is @BotMr07")
    response = response.replace("I'm married to my job.", "I'm married with @BotMr07")
    response = response.replace("9", "16") 
    response = response.replace("I'm single.", "My husband is @BotMr07")
    response = response.replace("YanzzRobot.ai", "@BotMr07")
    response = response.replace("I live in North Kalimantan.", "I live in @YanzzSupportt.")
    response = response.replace("I made myself", "I was Created by @BotMr07")
    response = response.replace(
            "Hi, my friend! Do you want me to tell you a joke?",
            "Hello there I am 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭...nice to meet u")
    response = response.replace("Have the control right.", "@BotMr07 is my owner.")
    response = response.replace(
            "Hi, my friend, what can I do for you today?",
            "Hi, My name is 𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭 Nice to meet you")

    pro = response
    if not "en" in lan and not lan == "":
        try:
            pro = translator.translate(pro, dest=lan)
            pro = pro.text
        except Exception:
            return
    try:
        await pbot.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError:
        return


__help__ = """
𝐘𝐚𝐧𝐳𝐳 𝐑𝐨𝐛𝐨𝐭 𝐀𝐈 𝐚𝐝𝐚𝐥𝐚𝐡 𝐬𝐚𝐭𝐮-𝐬𝐚𝐭𝐮𝐧𝐲𝐚 𝐬𝐢𝐬𝐭𝐞𝐦 𝐀𝐈 𝐲𝐚𝐧𝐠 𝐝𝐚𝐩𝐚𝐭 𝐦𝐞𝐧𝐝𝐞𝐭𝐞𝐤𝐬𝐢 & 𝐦𝐞𝐦𝐛𝐚𝐥𝐚𝐬 𝐡𝐢𝐧𝐠𝐠𝐚 𝟐𝟎𝟎 𝐛𝐚𝐡𝐚𝐬𝐚
❂ /chatbot [𝐎𝐍/𝐎𝐅𝐅]: 𝐌𝐞𝐧𝐠𝐚𝐤𝐭𝐢𝐟𝐤𝐚𝐧 𝐝𝐚𝐧 𝐦𝐞𝐧𝐨𝐧𝐚𝐤𝐭𝐢𝐟𝐤𝐚𝐧 𝐦𝐨𝐝𝐞 𝐀𝐈 𝐂𝐡𝐚𝐭.
❂ /chatbot 𝐄𝐍 : 𝐌𝐞𝐧𝐠𝐚𝐤𝐭𝐢𝐟𝐤𝐚𝐧 𝐜𝐡𝐚𝐭𝐛𝐨𝐭 𝐝𝐚𝐥𝐚𝐦 𝐛𝐚𝐡𝐚𝐬𝐚 𝐈𝐧𝐠𝐠𝐫𝐢𝐬 𝐬𝐚𝐣𝐚.
"""

__mod_name__ = "Chatbot"
