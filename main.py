import os
import time
import asyncio
import datetime
import aiofiles
from random import choice
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import *
from database import Database
from config import *
import aiohttp
CHANNEL_ID1 = -1002189546391
YOUR_USER_ID = [6359874284, 897584437]  # <-- Apna Telegram ID
# =======================

@Client.on_message(filters.command(["addmovie"]) & filters.user(YOUR_USER_ID))
async def addmovie_cmd(client, message: Message):
    if len(message.command) < 2:
        return await message.reply(
            "Please provide a movie name and optional year.\n\n<code>/addmovie Interstellar 2014</code>\n<code>/addmovie Breaking Bad</code>"
        )

    query = " ".join(message.command[1:])
    api_url = f"https://terabox-vercel-api-hgbotz-s-projects.vercel.app/query?query={query}"

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as resp:
            if resp.status != 200:
                return await message.reply("Failed to fetch movie details from API.")
            data = await resp.json()

    # Correct field names according to your JSON
    movie_name = data.get("matched_title", query)
    release_year = data.get("matched_year", "")
    media_type = data.get("media_type", "") 
    rating = data.get("rating", "") 
    overview = data.get("overview", "") 
    caption = f"#New_File_Added ✅ \n\n<b>📽️ 𝙵𝚒𝚕𝚎 𝙽𝚊𝚖𝚎 :- {movie_name} ({release_year})</b>\n\n<b>𝙼𝚎𝚍𝚒𝚊 𝚃𝚢𝚙𝚎 👉:-</b> {media_type} | <b>𝚁𝚊𝚝𝚒𝚗𝚐 💫:-</b> {rating} \n<b><blockquote>Powered by <a href='https://t.me/Movies_Eera'>Movies Eera 🦋</a></blockquote></b>"
    caption1 = f"#New_File_Added ✅ \n\n<b>📽️ 𝙵𝚒𝚕𝚎 𝙽𝚊𝚖𝚎 :- {movie_name} ({release_year})</b>\n\n<b>𝙼𝚎𝚍𝚒𝚊 𝚃𝚢𝚙𝚎 👉:-</b> {media_type} | <b>𝚁𝚊𝚝𝚒𝚗𝚐 💫:-</b> {rating} \n<b><blockquote>Powered by <a href='https://t.me/alsamovieszone'>ALSA MOVIES 🦋</a></blockquote></b>"
    image_url = None

    # Priority: English > Hindi > Default backdrops
    en_backs = data.get("english_backdrops", [])
    if en_backs:
        image_url = en_backs[0]
    else:
        hi_backs = data.get("hindi_backdrops", [])
        if hi_backs:
            image_url = hi_backs[0]
        else:
            def_backs = data.get("default_backdrops", [])
            if def_backs:
                image_url = def_backs[0]
            else:
                posters = data.get("posters", [])
                if posters:
                    image_url = posters[0]
    
    if not image_url:
        return await message.reply("No landscape image found for this movie.")

    # Invisible char trick for top preview
    text_to_send = f"<a href='{image_url}'>ㅤ</a> {caption}"
    text_to_send1 = f"<a href='{image_url}'>ㅤ</a> {caption1}"

    try:
        
        await client.send_message(
            chat_id=CHANNEL_ID1,
            text=text_to_send1,
            invert_media=True, 
            reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Search Here 🔥Alsa🔥" , url="https://t.me/alsamovieszone")]]), 
            disable_web_page_preview=False  # Important for preview
        )
        await message.reply("✅ Movie posted successfully with preview on top!")
    except Exception as e:
        await message.reply(f"❌ Failed to post movie:\n<code>{e}</code>")
# Database initialization
db = Database(DATABASE_URL, "autoreactionbot")

# Bot setup
Bot = Client(
    "Auto Reaction Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
)

# Messages and buttons
START_TEXT = """<b>{},

ɪ ᴀᴍ sɪᴍᴘʟᴇ ʙᴜᴛ ᴘᴏᴡᴇʀꜰᴜʟʟ ᴀᴜᴛᴏ ʀᴇᴀᴄᴛɪᴏɴ ʙᴏᴛ. 𝙱𝚢 ➥× ᏚᎧƝU⁣𓆩

ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀs ᴀ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ

<blockquote><spoiler>ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ  <a href='https://t.me/alsamovies'>× ᏚᎧƝU⁣𓆩💞𓆪</spoiler></a></blockquote></b>"""

LOG_TEXT = """<b>#NewUser Reaction 
    
ID - <code>{}</code>

Name - {}</b>"""

START_BUTTONS = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton(text='⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ⇆', url=f'https://telegram.me/{BOT_USERNAME}?startgroup=botstart')
    ],[
        InlineKeyboardButton(text='• ᴜᴩᴅᴀᴛᴇꜱ •', url='https://t.me/alsamovies'),
        InlineKeyboardButton(text='• ꜱᴜᴩᴩᴏʀᴛ •', url='https://t.me/hollywood_movies_in_hindidubs')
    ],[
        InlineKeyboardButton(text='⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇆', url=f'https://telegram.me/{BOT_USERNAME}?startchannel=botstart')
    ]]
)


# Helper functions
async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return send_msg(user_id, message)
    except (InputUserDeactivated, UserIsBlocked):
        return 400, f"{user_id} : error\n"
    except Exception as e:
        return 500, f"{user_id} : {str(e)}\n"

async def get_fsub(bot, message):
    target_channel_id = AUTH_CHANNEL  # Your channel ID
    user_id = message.from_user.id
    try:
        # Check if user is a member of the required channel
        await bot.get_chat_member(target_channel_id, user_id)
    except UserNotParticipant:
        # Generate the channel invite link
        channel_link = (await bot.get_chat(target_channel_id)).invite_link
        keyboard = [[InlineKeyboardButton("🔔 Join Our Channel", url=channel_link)]]

        # Display a message encouraging the user to join
        await message.reply(
            f"<b>👋 Hello {message.from_user.mention()}, Welcome!</b>\n\n"
            "📢 <b>Exclusive Access Alert!</b> ✨\n\n"
            "To unlock all the amazing features I offer, please join our updates channel. "
            "This helps us keep you informed and ensures top-notch service just for you! 😊\n\n"
            "<i>🚀 Join now and dive into a world of knowledge and creativity!</i>",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return False
    else:
        return True


# Handlers
@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    if not await db.is_user_exist(update.from_user.id):
        await db.add_user(update.from_user.id)
        await bot.send_message(LOG_CHANNEL, LOG_TEXT.format(update.from_user.id, update.from_user.mention))
    
    is_subscribed = await get_fsub(bot, update)
    if not is_subscribed:
        return

    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

@Bot.on_message(filters.private & filters.command("users") & filters.user(BOT_OWNER))
async def users(bot, update):
    total_users = await db.total_users_count()
    text = f"Bot Status\n\nTotal Users: {total_users}"
    await update.reply_text(
        text=text,
        quote=True,
        disable_web_page_preview=True
    )

@Bot.on_message(filters.private & filters.command("broadcast") & filters.user(BOT_OWNER) & filters.reply)
async def broadcast(bot, update):
    broadcast_ids = {}
    all_users = await db.get_all_users()
    broadcast_msg = update.reply_to_message
    out = await update.reply_text(text="Broadcast Started!")
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids["broadcast"] = {"total": total_users, "current": done, "failed": failed, "success": success}

    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id=int(user['id']), message=broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user['id'])
            done += 1

            broadcast_ids["broadcast"].update({"current": done, "failed": failed, "success": success})

    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await update.reply_text(
            text=f"Broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nDone: {done}, Success: {success}, Failed: {failed}",
            quote=True
        )
    else:
        await update.reply_document(
            document='broadcast.txt',
            caption=f"Broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nDone: {done}, Success: {success}, Failed: {failed}"
        )
    os.remove('broadcast.txt')

# Reaction handling
@Bot.on_message(filters.all)
async def send_reaction(_, msg: Message):
    try:
        # Assuming Config.EMOJIS is a predefined list of emojis
        await msg.react(choice(EMOJIS))
    except:
        pass

# Start bot
Bot.run()
