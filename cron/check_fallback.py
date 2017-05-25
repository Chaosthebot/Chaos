import arrow
import logging

import settings
import github_api as gh

__log = logging.getLogger("chaosbot")
api = gh.API(settings.GITHUB_USER, settings.GITHUB_SECRET)
urn = settings.URN

def  check_fallback():
    latest_commit = Commit(gh.get_latest_commit(api, settings.URN))
    commit_time = arrow.get(latest_commit.get_commit_date())
    now = arrow.utcnow()
    span = now - commit_time
    if(span.seconds < setings.FALLBACK_WINDOW_SECONDS)
        # it happened
        message = "No pull requests were approved in the last {fallback_hours} hours. Therefore, a random compatible PR was chosen to be merged in spite of current voting status.".format(fallback_hours=settings.FALLBACK_WINDOW_HOURS)
        gh.merge_random(api, urn, message)


