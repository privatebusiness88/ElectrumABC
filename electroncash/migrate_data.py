"""This module handles copying the Electron Cash data dir
to the Electrum ABC data path if it does not already exists.

The first time a user runs this program, if he already uses Electron Cash,
he should be able to see all his BCH wallets.
"""
import os
import shutil
from typing import Optional

from .util import get_user_dir


# function copied from https://github.com/Electron-Cash/Electron-Cash/blob/master/electroncash/util.py
def get_ec_user_dir() -> Optional[str]:
    """Get the Electron Cash data directory.
    """
    if os.name == 'posix' and "HOME" in os.environ:
        return os.path.join(os.environ["HOME"], ".electron-cash")
    elif "APPDATA" in os.environ or "LOCALAPPDATA" in os.environ:
        app_dir = os.environ.get("APPDATA")
        localapp_dir = os.environ.get("LOCALAPPDATA")
        if app_dir is None:
            app_dir = localapp_dir
        return os.path.join(app_dir, "ElectronCash")
    else:
        return


def does_user_dir_exist() -> bool:
    """Return True if an Electrum ABC directory exists.
    It will be False the first time a user runs the application.
    """
    user_dir = get_user_dir()
    if user_dir is None or not os.path.isdir(user_dir):
        return False
    return True


def does_ec_user_dir_exist() -> bool:
    """Return True if an Electron Cash user directory exists.
    It will return False if Electron Cash is not installed.
    """
    user_dir = get_ec_user_dir()
    if user_dir is None or not os.path.isdir(user_dir):
        return False
    return True


def migrate_data_from_ec():
    """Copy the EC data dir the first time Electrum ABC is executed.
    This makes all the wallets and settings available to users.
    """
    if does_ec_user_dir_exist() and not does_user_dir_exist():
        src = get_ec_user_dir()
        dest = get_user_dir()
        shutil.copytree(src, dest)
