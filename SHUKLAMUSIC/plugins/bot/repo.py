from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SHUKLAMUSIC import app
from config import BOT_USERNAME
from SHUKLAMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ωεℓ¢σмє ƒσя 𝚂𝚝𝚛𝚊𝚗𝚐𝚎𝚛 яєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ 𝗝𝗔 𝗕𝗘 𝗖𝗛𝗢𝗠𝗨 𝗥𝗘𝗣𝗢 𝗟𝗘𝗝𝗔 ✰
 
 ➲ 𝗝𝗔 𝗕𝗘 𝗖𝗛𝗢𝗠𝗨 𝗥𝗘𝗣𝗢 𝗟𝗘𝗝𝗔
 
 ➲𝗝𝗔 𝗕𝗘 𝗖𝗛𝗢𝗠𝗨 𝗥𝗘𝗣𝗢 𝗟𝗘𝗝𝗔✰
 
 ➲ Prince ko papa bolo  ✰
 
 ► 𝗝𝗔 𝗕𝗘 𝗖𝗛𝗢𝗠𝗨 𝗥𝗘𝗣𝗢 𝗟𝗘𝗝𝗔
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/l_ABOUT_PRINCE_l"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/l_ABOUT_PRINCE_l"),
          ],
               [
                InlineKeyboardButton("𝗨𝗣𝗗𝗔𝗧𝗘𝗦", url="https://t.me/l_ABOUT_PRINCE_l"),

],
[
              InlineKeyboardButton("𝗕𝗔𝗡 𝗔𝗟𝗟︎", url=f"https://t.me/l_ABOUT_PRINCE_l"),
              InlineKeyboardButton("︎𝗩2 𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/l_ABOUT_PRINCE_l"),
              ],
              [
              InlineKeyboardButton("𝗩1 𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/itzshukla/STRANGER-MUSIC2.0/fork"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/itzshukla/STRANGER-CHATBOT/fork"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://github.com/itzshukla/STRANGER-STRING-GEN/fork"),
InlineKeyboardButton("𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧", url=f"https://github.com/itzshukla/STRANGER-ROBOT/fork"),
],
[
              InlineKeyboardButton("𝗦𝗣𝗔𝗠 𝗕𝗢𝗧", url=f"https://github.com/itzshukla/STRANGER-SPAM-X/fork"),
              InlineKeyboardButton("𝗕𝗔𝗡𝗔𝗟𝗟 10 𝗕𝗢𝗧︎", url=f"https://github.com/itzshukla/STRANGER-BANALL-BOTS/fork"),
              ],
              [
              InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚 𝗛𝗔𝗖𝗞︎", url=f"https://t.me/l_ABOUT_PRINCE_l"),
InlineKeyboardButton("𝗜𝗗 𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://t.me/l_ABOUT_PRINCE_l"),
],
[
InlineKeyboardButton("𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://t.me/l_ABOUT_PRINCE_l"),
InlineKeyboardButton("𝗜𝗗-𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://t.me/l_ABOUT_PRINCE_l"),
],
[
InlineKeyboardButton("𝗦𝗨𝗣𝗘𝗥-𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://t.me/l_ABOUT_PRINCE_l"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/d9bddd89a8070632de73e.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/itzshukla/STRANGER-MUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/itzshukla/STRANGER-MUSIC) | [UPDATES](https://t.me/SHIVANSH474)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


