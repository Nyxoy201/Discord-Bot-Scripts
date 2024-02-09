import discord
import asyncio
import aiohttp
import pystyle
from pystyle import Colors, Colorate

intents = discord.Intents.all()

print(Colorate.Horizontal(Colors.purple_to_blue, """
██████╗  ██████╗ ████████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗╚══██╔══╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██║   ██║   ██║       ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔══██╗██║   ██║   ██║       ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝   ██║       ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═════╝  ╚═════╝    ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                      """))

async def check_tokens(tokens):
    valid_tokens = []
    invalid_tokens = []

    async with aiohttp.ClientSession() as session:
        for token in tokens:
            client = discord.Client(intents=intents)

            try:
                await asyncio.shield(client.login(token))
                print(Colorate.Horizontal(Colors.purple_to_blue, f"Valid Token: {token}"))
                valid_tokens.append(token)

            except discord.errors.LoginFailure:
                print(Colorate.Horizontal(Colors.purple_to_blue, f"Invalid Token : {token}"))
                invalid_tokens.append(token)

            await asyncio.sleep(0)

    return valid_tokens, invalid_tokens

tokens_file = "tokens.txt" # Your tokens file

with open(tokens_file, "r") as file:
    tokens = [line.strip() for line in file.readlines()]

valid_tokens, invalid_tokens = asyncio.run(check_tokens(tokens))

delete_invalid_tokens = input(Colorate.Horizontal(Colors.purple_to_blue,
                                                 "Wanna delete invalids tokens ? (yes/no): ").lower())

if delete_invalid_tokens == "yes":
    with open(tokens_file, "w") as file:
        file.write("\n".join(valid_tokens))
    print(Colorate.Horizontal(Colors.purple_to_blue, "Invalids tokens deleted."))
else:
    print(Colorate.Horizontal(Colors.purple_to_blue, "No changes."))
