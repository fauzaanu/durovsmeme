from cred import *
from main import memedownloader
import logging
from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler
import os
import requests

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# check for a new meme every hour  
async def send_updates(context):
    chats = [chat_idx]
    
    # get the last meme from lastmeme.txt
    with open('lastmeme.txt', 'r') as f:
        last_meme = f.read()
    
    new_meme = await memedownloader()
    
    # check if the new meme is different from the last meme
    if new_meme != last_meme:
        # send the new meme to all the chats
        for chat_id in chats:
            await context.bot.send_photo(chat_id=chat_id, photo=open(f'meme/{new_meme}', 'rb'))
    
    # update the last meme
    with open('lastmeme.txt', 'w') as f:
        f.write(new_meme)
        
if __name__ == '__main__':
    token = bot_api_key
    
    print(token)
    application = ApplicationBuilder().token(token).build()
    

    job_queue = application.job_queue
    job_queue.run_repeating(send_updates, interval=30, first=0)

    application.run_polling()