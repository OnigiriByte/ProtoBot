import arc
from datetime import datetime, timedelta

plugin = arc.GatewayPlugin("ping")


@plugin.include
@arc.slash_command("ping", "a ping command used for testing")
async def ping(
        ctx: arc.GatewayContext,
):

    heartbeat_latency_ms = ctx.client.app.heartbeat_latency * 1000
    await ctx.respond(f"**Pong!**\n`Hearbeat Latency: {heartbeat_latency_ms:.2f}ms`")


@arc.loader()
def loader(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)


@arc.unloader()
def unloader(client: arc.GatewayClient) -> None:
    client.remove_plugin(plugin)
