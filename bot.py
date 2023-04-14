import asyncio
from loguru import logger
from bot_settings import bot, dp
from database.db import db
from handlers.base_handler import router


async def main():
    db.init_db()
    dp.include_routers(router)
    logger.info('polling...')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
