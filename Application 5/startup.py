import os
from art import *
import datetime
from subprocess import run

USERNAME = os.getenv("USERNAME")
STYLE = os.getenv("STYLE")


def startup(USERNAME):
    print(text2art(f"Welcome {USERNAME}", "random"))
    return datetime.datetime.now()


time = f"{startup(USERNAME)}"
run(['echo', f"'time={time}'", ">>", "$GITHUB_OUTPUT"], capture_output=True)
