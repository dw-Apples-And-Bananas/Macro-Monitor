import update
from echo import *
import time

echo("$(3)Checking For Updates")
time.sleep(0.5)
ver, creator = update.check()
print()


import threading
import os, sys

loading = True
def load():
    os.system("tput setaf 2")
    i = 1
    while loading:
        sys.stdout.write("\r" + "Loading" + "."*i)
        time.sleep(0.2)
        sys.stdout.flush()
        i += 1
    print()
loadingThread = threading.Thread(target=load)
loadingThread.start()


import readline
from commands import cmds
import keybinds

usr = os.path.expanduser("~")
os.chdir(f"{usr}/Documents/Coding/Macro-Monitor")

keybinds.listen()

time.sleep(0.5)
loading = False
time.sleep(0.5)

echo(f"\n$(1)Macro Monitor$(0)\nversion: {ver}\ncreated by: {creator}\n")

try:
    cmds.input()
except KeyboardInterrupt:
    echo("\n$(1)Stopping Macro Monitor")
