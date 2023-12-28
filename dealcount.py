from datetime import datetime, timedelta
import pytz
from decouple import config
from apscheduler.job import Job
from apscheduler.triggers.date import DateTrigger
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler

SQLITE_LOCATION = config("SQLITE_LOCATION", default = "/jobs.sqlite")
TIMEZONE = config("TIMEZONE", default = "UTC")
LOG_LEVEL = config("LOG_LEVEL", default = "INFO")
WEBHOOK = config("WEBHOOK_URL", default = "NONE")

jobstores : dict[str,SQLAlchemyJobStore] = {"default", SQLAlchemyJobStore(url = f"sqlite://{SQLITE_LOCATION}")}