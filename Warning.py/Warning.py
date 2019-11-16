import discord
from discord.ext import commands

#core import
from Files._json_handle import class_warnings as cls_w
#done



class Warning(commands.Cog):
    def init(self, bot):
        self.bot_object = bot


    @commands.command()
    async def warn(self, ctx, _user:discord.Member, *,_reason):
        try:
            await discord.Message.delete(ctx.message)
        except Exception:
            pass
        warn_user = str(_user.id)
        guild = str(ctx.message.guild.id)
        _staff = ctx.message.author
        await cls_w.object_determin_path_structure(self)
        await cls_w.function_create_user(self, warn_user)
        await cls_w.function_reason_guild(self, guild_warn=guild,user_warn=warn_user,reason_warn=_reason)
        embed = await cls_w.discord_embed_warn(self, _staff, _user, _reason)
        await ctx.send(_user.mention, embed=embed)

    @commands.command()
    async def get_warn(self, ctx, _user:discord.Member):
        user_warned = str(_user.id)
        returned_warnings = await cls_w._get_all_warnings(self, user_warned)
        await ctx.send(returned_warnings)



def setup(bot):
    cog = Warning(bot)
    bot.add_cog(cog)