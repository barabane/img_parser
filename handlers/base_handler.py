import vk
import os
import asyncio
from aiogram import Router
from aiogram.types import Message, InputMediaPhoto, Chat
from aiogram.filters import CommandStart
from database.db import db
from dotenv import load_dotenv
from utils.media_handlers import photo_handler
from bot_settings import bot


load_dotenv()
router = Router()

session = vk.API(
    access_token=os.environ.get('VK_TOKEN'))
groups_id = ['-177572334', '-123224791',
             '-202233169', '-206380060', '-218007629', '-207077429']


@router.message(CommandStart())
async def start_handler(msg: Message):
    posts = []

    for _id in groups_id:
        post = session.wall.get(owner_id=_id, count=1, v=5.92)
        is_ads = post['items'][0]['marked_as_ads']
        attachments = post['items'][0]['attachments']
        post_hash = post['items'][0]['hash']

        if is_ads:
            continue

        if db.find_post(_id, post_hash):
            await asyncio.sleep(2)
            continue
        else:
            db.add_post(_id, post_hash)

        album = []
        for attach in attachments:
            if attach['type'] == 'photo':
                album.append(InputMediaPhoto(
                    media=photo_handler(attach)))
        posts.append(album)
        await asyncio.sleep(2)

    if len(posts) == 0:
        await msg.answer(text='Новых постов пока нет...')
        return

    for post in posts:
        await asyncio.sleep(5)
        await bot.send_media_group(chat_id=os.environ.get('CHANNEL_ID'), media=post, disable_notification=True)
