import sys
import os
import time
from datetime import timedelta
from games.functions import *;
import threading


def lc():
    FIRST_LOAD = True
    while True:
        if FIRST_LOAD:
            updateGames()
            FIRST_LOAD = False

        
        # update every 24 hours at 4am
        current_time = time.localtime()
        if current_time.tm_hour == 4 and current_time.tm_min == 0:
            updateGames()  # sleep for a minute to avoid repeated updates within the same minute



        time.sleep(60*60*10)


def run_lc():
    thread = threading.Thread(target=lc)
    thread.daemon = True  # Set the thread as a daemon thread
    thread.start()