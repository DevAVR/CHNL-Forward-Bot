#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# By @TheUnusualPsychopath

import asyncio
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from translation import Translation

import pyrogram
from pyrogram import Client, Filters


@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_MSG,
        parse_mode='html'
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP,
        parse_mode='html'
    )    
   

@pyrogram.Client.on_message(Filters.private & Filters.media)
async def forward(bot, message):
    try:
        await message.forward(
            chat_id=Config.CHANNEL_ID,
            as_copy=True
        )
        await message.reply_text(
            text="<code>Forwaded Sucessfully</code>",
            parse_mode='html',
            quote=True
        )
    except:
        await message.reply_text(
            text="<code>Make Sure That I am Admin in Your Channel or Provided Channel ID is Correct.</code>",
            parse_mode='html',
            quote=True
        )
