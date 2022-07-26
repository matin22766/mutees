from pyrogram import Client,filters
from pyrogram.types import Message
import time
api_id = 19504232
api_hash = "014607e14241d2da92b94b61a5e8d7ec"
bot = Client("newpuup2",api_id,api_hash)
lis = []
username = "elsaharm"#without @
helper_list = """/mute
/unmute
/mlist(list mute ha)
/clear(clear mute list)"""
@bot.on_message()
def action(cli:Client, m:Message):
    word = m.text
    grop = m.chat.id
    ch_id = m.from_user.username
    if ch_id == username:
        if word == "/help":
            m.edit(helper_list)
        if "/mute" in word:
            m.reply("set in...")
            if "list" in lis:
                lis.remove("list")
            if "_list" in lis:
                lis.remove("_list")
            edired = word.replace("/mute", "").replace(" ", "").replace("@", "")
            lis.append(edired)
        if "/unmute" in word:
            m.reply("ok!")
            if "list" in lis:
                lis.remove("list")
            if "_list" in lis:
                lis.remove("_list")
            edired2 = word.replace("/unmute", "").replace(" ", "").replace("@", "")
            lis.remove(edired2)            
        if word == "/mlist":
            if "list" in lis:
                lis.remove("list")
            if "_list" in lis:
                lis.remove("_list")            
            m.reply(lis)
        if word == "/clear":
            m.reply("mute list cleaned!")
            lis.clear()
    target = lis
    if ch_id in target:
        m.delete()
    else:
        pass
    
                
                
        
        
bot.run()