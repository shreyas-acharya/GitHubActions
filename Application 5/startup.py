import os
from art import *
import datetime

USERNAME = os.getenv("USERNAME")
STYLE = os.getenv("STYLE")


def startup(USERNAME):
    print(text2art(f"Welcome {USERNAME}", "random"))
    return datetime.datetime.now()


time = f"{startup(USERNAME)}"
print(f"echo 'time={time}' >> $GITHUB_OUTPUT")
