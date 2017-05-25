import schedule
import settings

from .poll_pull_requests import poll_pull_requests as poll_pull_requests
from .restart_homepage import restart_homepage as restart_homepage
from .check_fallback import check_fallback

def schedule_jobs():
    schedule.every(settings.PULL_REQUEST_POLLING_INTERVAL_SECONDS).seconds.do(poll_pull_requests)
    schedule.every(settings.FALLBACK_WINDOW_SECONDS).seconds.do(check_fallback)
    schedule.every(120).seconds.do(restart_homepage)
