import vk
import os
from aiogram import Router
from aiogram.types import Message, InputMediaPhoto
from aiogram.filters import CommandStart
from database.db import db
from dotenv import load_dotenv

load_dotenv()
router = Router()

session = vk.API(
    access_token=os.environ.get('VK_TOKEN'))
groups_id = ['-202233169', '-177572334', '-123224791']


@ router.message(CommandStart())
async def start_handler(msg: Message):
    for _id in groups_id:
        post = session.wall.get(owner_id=_id, count=1, v=5.92)
        is_ads = post['items'][0]['marked_as_ads']

        if is_ads:
            continue

        medias = session.wall.get(
            owner_id=_id, count=1, v=5.92)['items'][0]['attachments']

        photo_album = []
        for media in medias:
            if media['type'] != 'photo':
                continue

            photo_album.append(InputMediaPhoto(
                media=media['photo']['sizes'][4]['url']))

        await msg.answer_media_group(media=photo_album)
