
from platform import system as systemos
from os import getuid


def compatibility_checker():

    if systemos() != "Windows":
        if getuid() == 0:
            print("Permissions granted!")
        else:
            print("Permissions denied! Run with 'sudo'")
            exit()
    else:
        print(
            "Windows system not compatible yet. Make sure you're using it on supported system.")
        exit()
