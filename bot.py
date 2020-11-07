#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# By @TheUnusualPsychopath

import os
import pyrogram

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

#Base By Spechides Anydlbot


if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "CHNL-Forward-Bot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )
    app.run()
