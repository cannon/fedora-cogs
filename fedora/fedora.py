import discord
from discord.ext import commands
from .utils.chat_formatting import *
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from urllib import parse
import aiohttp
import os

class Fedora:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,no_pm=True)
    async def image(self, ctx, *text):
        """Retrieves the latest result from Derpibooru"""
        await fetch_image(self, ctx, text)

    @commands.command(pass_context=True,no_pm=True)
    async def gif(self, ctx, *text):
        """Retrieves a random result from Derpibooru"""
        await fetch_image(self, ctx, "gif "+text)

async def fetch_image(self, ctx, text):
    server = ctx.message.server

    # Fetch the image or display an error
    try:
        async with aiohttp.request('post','https://swampservers.net/fedorabot/', params={'q':text}) as r:
            website = await r.text()

        url = website.split('url:')
        if len(url) > 1:
            url = url[-1][:-1]
            return await self.bot.say(url)
        else:
            return await self.bot.say("Your search terms gave no results.")

    except:
        return await self.bot.say("Error.")

def setup(bot):
    bot.add_cog(Fedora(bot))
