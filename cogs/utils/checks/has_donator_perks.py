from discord.ext import commands
import voxelbotutils as utils

from cogs.utils.perks_handler import get_marriagebot_perks


def has_donator_perks(perk_name:str):
    async def predicate(ctx):
        return True  # ah

        perks = await get_marriagebot_perks(ctx.bot, ctx.author.id)
        v = getattr(perks, perk_name, False)
        if v:
            return v
        raise utils.errors.IsNotUpgradeChatSubscriber()
    return commands.check(predicate)
