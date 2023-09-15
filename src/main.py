import asyncio

import uvicorn

from src.build import build_app


async def main():
    app = await build_app()
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)

    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())



