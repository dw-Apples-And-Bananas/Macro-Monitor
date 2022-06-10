import os

def echo(msg):
    msg = msg.replace("$(0)", "$(tput sgr0)")
    msg = msg.replace("$(", "$(tput setaf ")
    os.system(f'echo "{msg}$(tput sgr0)"')
