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
    async def tazer(self, ctx, node_name: str, power: float):
        msg = "ERROR!"
        voltage = power/100.0*15 
        if node_name == "Siwat":
            msg = "Tazering "+node_name+" with "+voltage+" kV" 
        await ctx.send(msg)