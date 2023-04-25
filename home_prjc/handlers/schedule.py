import datetime

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from config import ADMINS, bot


async def go_to_shopping(bot: Bot):
    admin = ADMINS[0]
    await bot.send_message(admin, f"It is time to do shopping!")


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")

    scheduler.add_job(
        go_to_shopping,
        kwargs={"bot": bot},
        trigger=CronTrigger(
            day_of_week=6,
            hour=10,
            start_date=datetime.datetime.now()
        )
    )

    scheduler.start()
