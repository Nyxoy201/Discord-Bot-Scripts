import discord
import asyncio
import aiohttp
import pystyle
from pystyle import Colors, Colorate

intents = discord.Intents.all()

print(Colorate.Horizontal(Colors.purple_to_blue, """
██████╗  ██████╗ ████████╗    ██╗███╗   ██╗██╗   ██╗██╗████████╗███████╗
██╔══██╗██╔═══██╗╚══██╔══╝    ██║████╗  ██║██║   ██║██║╚══██╔══╝██╔════╝
██████╔╝██║   ██║   ██║       ██║██╔██╗ ██║██║   ██║██║   ██║   █████╗  
██╔══██╗██║   ██║   ██║       ██║██║╚██╗██║╚██╗ ██╔╝██║   ██║   ██╔══╝  
██████╔╝╚██████╔╝   ██║       ██║██║ ╚████║ ╚████╔╝ ██║   ██║   ███████╗
╚═════╝  ╚═════╝    ╚═╝       ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝   ╚══════╝
                                                                        """))

async def create_bot_invite(token):
    client = discord.Client(intents=intents)

    try:
        await asyncio.shield(client.login(token))
        print(Colorate.Horizontal(Colors.purple_to_blue, f"Bot successfully connected : {client.user.name}"))

        invite_url = discord.utils.oauth_url(client.user.id)
        print(Colorate.Horizontal(Colors.purple_to_blue, f"""Invitation for the bot : 
{invite_url}
"""))

    except discord.errors.LoginFailure:
        print(Colorate.Horizontal(Colors.purple_to_blue, "Error during the connection, check bot's token."))

    await client.close()

async def main():
    token = input(Colorate.Horizontal(Colors.purple_to_blue, "Input bot's token : "))
    await create_bot_invite(token)

asyncio.run(main())
