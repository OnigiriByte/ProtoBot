import arc
import hikari
import miru

with open(".token") as file:
    token = file.readline().strip()

bot = hikari.GatewayBot(token)
arc_client = arc.GatewayClient(bot)
client = miru.Client.from_arc(arc_client)

arc_client.load_extensions_from(dir_path="./src/extensions")

bot.run()
