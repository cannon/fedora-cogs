import discord
from discord.ext import commands
from .utils.chat_formatting import *
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from urllib import parse
import aiohttp
import time
import os

class Fedora:
    def __init__(self, bot):
        self.bot = bot
        self.lasttime = 0

    @commands.command(pass_context=True,no_pm=True)
    async def image(self, ctx, *text):
        await fetch_image(self, ctx, ' '.join(text))

    @commands.command(pass_context=True,no_pm=True)
    async def gif(self, ctx, *text):
        await fetch_image(self, ctx, "gif "+( ' '.join(text) ))

async def fetch_image(self, ctx, text):
    server = ctx.message.server
    
    if (time.time() - self.lasttime) < 7:
        return
        
    self.lasttime = time.time()

    # Fetch the image or display an error
    try:
        async with aiohttp.request('post','https://swampservers.net/fedorabot/', data={'q':text}) as r:
            website = await r.text()

        url = website.split('url:')
        if len(url) > 1:
            safe = False
            if url[0].endswith("safe"):
                safe = True
            channame = ctx.message.channel.name.lower()
            if "nsfw" in channame or channame=="straight" or channame=="gay" or channame=="anything":
                safe = True

            if not safe:
                return await self.bot.say("NSFW result, go to an NSFW channel")

            numba = url[0].split(")")[0]+")"
            url = url[-1][:-1]
            return await self.bot.say(numba+" "+url)
        else:
            return await self.bot.say("No results.")

    except:
        return await self.bot.say("Error.")

def setup(bot):
    bot.add_cog(Fedora(bot))
