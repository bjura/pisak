import sys

import pisak
from pisak import app_manager, res
from pisak.libs import handlers

from pisak.libs.speller import widgets  # @UnusedImport
import pisak.libs.speller.handlers  # @UnusedImport


def prepare_main_view(app, window, script, data):
    handlers.button_to_view(window, script, "button_exit")


if __name__ == "__main__":
    pisak.init()
    _speller_app = {
        "app": "speller",
        "type": "clutter",
        "views": [("main", prepare_main_view)]
    }
    app_manager.run(_speller_app)
