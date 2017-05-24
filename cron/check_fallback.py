import arrow
import logging

import settings
import github_api as gh

__log = logging.getLogger("chaosbot")

def  check_fallback():
    latest_commit = gh.get_latest_commit(api, settings.URN)
    commit_time = arrow.get(latest_commit['commit']['author']['date'])
    now = arrow.utcnow()
    span = now - commit_time
    if(span.hour < setings.FALLBACK_WINDOW)
        revert_last_commit(latest_commit['sha'])

def revert_last_commit(sha):


