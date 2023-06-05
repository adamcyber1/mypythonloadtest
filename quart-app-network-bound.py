import asyncio
from random import randint

from quart import Quart

app = Quart(__name__)

@app.route('/')
async def simulated_request():
    await asyncio.sleep(randint(100, 1000) / 1000)
    return 'Returned!'


if __name__ == "__main__":
    app.run()