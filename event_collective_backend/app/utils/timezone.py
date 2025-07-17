from datetime import datetime
import pytz

def convert_utc_to_local(utc_dt: datetime, tz_str: str = "US/Eastern") -> datetime:
    local_tz = pytz.timezone(tz_str)
    return utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)

def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %I:%M %p") -> str:
    return dt.strftime(fmt)
