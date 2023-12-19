from aiohttp import web
import asyncio

async def hello(request):
    return web.Response(text="Hello, world")

async def bye(request):
    return web.Response(text="Bye bye, world")

def create_runner():
    app = web.Application()
    app.add_routes([
        web.get('/', hello),
        web.get('/bye', bye),
    ])
    return web.AppRunner(app)

async def start_server(host="0.0.0.0", port=8080):
    runner = create_runner()
    await runner.setup()

    site = web.TCPSite(runner, host, port)
    await site.start()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.run_forever()
