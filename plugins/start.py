from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	Hello {message.from_user.first_name }
	__I am file renamer bot, Please sent any telegram 
	**Document Or Video** and enter new filenameto rename it__
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("⛓️ 𝕆𝕎ℕ𝔼ℝ ⛓️" ,url="https://t.me/mnzks"), 
	  InlineKeyboardButton("🇮🇳 𝕊𝕌ℙℙ𝕆ℝ𝕋 🇮🇳", url="https://t.me/inblizbots")
          ],[
          InlineKeyboardButton("🔰 ℂℍ𝔸ℕℕ𝔼𝕃 🔰", url="https://t.me/srsuggestionsmc")
          ]]
          )
        )



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__What do you want me to do with this file?__\n**File Name** :- <code>{filename}</code>\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename ",callback_data = "rename")
       ,InlineKeyboardButton("Cancel✖️",callback_data = "cancel")  ]]))
