#!/usr/bin/env python
import logging
logging.basicConfig(level=logging.DEBUG)



from mmpy_bot import Bot, Settings
from fileplugin import MyPlugin

bot = Bot(
    settings=Settings(
        MATTERMOST_URL = "URL",
        MATTERMOST_PORT = 8065,
        BOT_TOKEN = "TOKEN",
        BOT_TEAM = "NAME",
        SSL_VERIFY = False,
    ),  # Either specify your settings here or as environment variables.
    plugins=[MyPlugin()],  # Add your own plugins here.
)
bot.run()