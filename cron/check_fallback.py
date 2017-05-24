import arrow
import logging

import settings
import github_api as gh

__log = logging.getLogger("chaosbot")

def  check_fallback():
    latest_commit = Commit(gh.get_latest_commit(api, settings.URN))
    commit_time = arrow.get(latest_commit.get_commit_date())
    now = arrow.utcnow()
    span = now - commit_time
    if(span.seconds < setings.FALLBACK_WINDOW_SECONDS)
        revert_last_commit(latest_commit.get_parent_sha())

def revert_last_commit(sha):


