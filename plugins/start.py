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
          InlineKeyboardButton("โ๏ธ ๐๐โ๐ผโ โ๏ธ" ,url="https://t.me/mnzks"), 
	  InlineKeyboardButton("๐ฎ๐ณ ๐๐โโ๐โ๐ ๐ฎ๐ณ", url="https://t.me/inblizbots")
          ],[
          InlineKeyboardButton("๐ฐ โโ๐ธโโ๐ผ๐ ๐ฐ", url="https://t.me/srsuggestionsmc")
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
       f"""<code>{filename}</code>"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("๐ Rename ",callback_data = "rename")
       ,InlineKeyboardButton("Cancelโ๏ธ",callback_data = "cancel")  ]]))
