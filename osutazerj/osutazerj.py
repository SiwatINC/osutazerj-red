from redbot.core import commands


BaseCog = getattr(commands, "Cog", object)


class osutazerj(BaseCog):
    """🏓"""

    async def red_delete_data_for_user(self, **kwargs):
        """ Nothing to delete """
        return

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def osutazerj(self, ctx):
        
        
        await ctx.send("OsuTazerJ BETA v0.1 by Siwat Sirichai")
    @commands.command()
    async def tazer(self, ctx, *arguments: str):
        pram = arguments.split(' ')
        msg = "ERROR!"
        if msg == "Siwat":
            msg = "Tazering "
        await ctx.send(str)