import os

PROJECT_NAME: str = "Electrum ABC"
PROJECT_NAME_NO_SPACES = "ElectrumABC"
SCRIPT_NAME: str = "electrum-abc"
REPOSITORY_URL: str = "https://github.com/PiRK/ElectrumBCHA"
RELEASES_JSON_URL: str = "https://raw.github.com/PiRK/ElectrumBCHA/master/contrib/update_checker/releases.json"

POSIX_DATA_DIR: str = os.path.join(os.environ["HOME"], ".electrum-abc")
"""This is where the wallets, recent server lists and some
other things are saved.
"""
