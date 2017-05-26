#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import dirname, abspath, join

import time
import sys
import logging
import subprocess
import settings
import schedule

import cron
import github_api as gh


def main():
    """main entry"""
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M')
    logging.getLogger("requests").propagate = False
    logging.getLogger("sh").propagate = False

    log = logging.getLogger("chaosbot")

    gh.API(settings.GITHUB_USER, settings.GITHUB_SECRET)

    log.info("starting up and entering event loop")

    os.system("pkill chaos_server")

    server_dir = join(dirname(abspath(__file__)), "server")
    subprocess.Popen([sys.executable, "server.py"], cwd=server_dir)

    # Schedule all cron jobs to be run
    cron.schedule_jobs()

    while True:
        # Run any scheduled jobs on the next second.
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
