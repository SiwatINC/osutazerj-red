from .osutazerj import OsuTazerJ

__red_end_user_data_statement__ = "I won't be responsible for death!"


def setup(bot):
    bot.add_cog(OsuTazerJ(bot))