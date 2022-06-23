import Sleepblogger
import time

import CustomLogger

log = CustomLogger.getLogger(level=10)


def main():
    blogger = Sleepblogger.SleepBlogger()
    with blogger:
        log.info("Start inhibit.")
        time.sleep(1)
        log.info("End inhibit.")


if __name__ == "__main__":
    main()

